import asyncio
import os
from pathlib import Path
from typing import List, Optional, Union

from bilix.sites.bilibili.downloader import DownloaderBilibili
from httpx import AsyncClient, Client, TransportError
from rich.traceback import install

from biliarchiver.archive_bvid import archive_bvid
from biliarchiver.config import config
from biliarchiver.config import BILIBILI_IDENTIFIER_PERFIX
from biliarchiver.utils.http_patch import HttpOnlyCookie_Handler
from biliarchiver.utils.version_check import check_outdated_version
from biliarchiver.utils.storage import get_free_space
from biliarchiver.utils.identifier import human_readable_upper_part_map, is_bvid
from biliarchiver.utils.ffmpeg import check_ffmpeg
from biliarchiver.version import BILI_ARCHIVER_VERSION

install()


def check_ia_item_exist(client: Client, identifier: str) -> bool:
    cache_dir = config.storage_home_dir / "ia_item_exist_cache"
    # check_ia_item_exist_from_cache_file:
    if (cache_dir / f"{identifier}.mark").exists():
        # print('from cached .mark')
        return True

    def create_item_exist_cache_file(identifier: str) -> Path:
        with open(cache_dir / f"{identifier}.mark", "w", encoding="utf-8") as f:
            f.write("")
        return cache_dir / f"{identifier}.mark"

    params = {
        "identifier": identifier,
        "output": "json",
    }
    # check_identifier.php API 响应快
    r = None
    for _ in range(3):
        try:
            r = client.get(
                "https://archive.org/services/check_identifier.php", params=params
            )
            break
        except TransportError as e:
            print(e, "retrying...")
    assert r is not None
    r.raise_for_status()
    r_json = r.json()
    assert r_json["type"] == "success"
    if r_json["code"] == "available":
        return False
    elif r_json["code"] == "not_available":  # exists
        cache_dir.mkdir(parents=True, exist_ok=True)
        create_item_exist_cache_file(identifier)
        return True
    else:
        raise ValueError(f'Unexpected code: {r_json["code"]}')


def _down(
    bvids: Union[Path, str, List[str]],
    skip_ia_check: bool,
    from_browser: Optional[str],
    min_free_space_gb: int,
    skip_to: int,
):
    assert check_ffmpeg() is True, "ffmpeg 未安装"

    bvids_list = None

    if isinstance(bvids, str):
        bvids = Path(bvids)
    if isinstance(bvids, list):
        bvids_list = bvids
    elif not bvids.exists() and bvids.name.startswith("BV"):
        if is_bvid(bvids.name):
            print("你输入的 bvids 不是文件，貌似是单个的 bvid，将直接下载...")
            bvids_list = [bvids.name]
        else:
            raise ValueError(f"你输入的 bvids 不是文件，貌似是单个的 bvid，但是不是合法的 bvid: {bvids.name}")
    else:
        with open(bvids, "r", encoding="utf-8") as f:
            bvids_list = f.read().splitlines()

    assert bvids_list is not None and len(bvids_list) > 0, "bvids 为空"
    del bvids
    for bvid in bvids_list:
        assert is_bvid(bvid), f"bvid {bvid} 不合法"

    check_outdated_version(
        pypi_project="biliarchiver", self_version=BILI_ARCHIVER_VERSION
    )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    d = DownloaderBilibili(
        hierarchy=True,
        sess_data=None,  # sess_data 将在后面装载 cookies 时装载 # type: ignore
        video_concurrency=config.video_concurrency,
        part_concurrency=config.part_concurrency,
        stream_retry=config.stream_retry,
    )

    # load cookies
    if from_browser is not None:
        update_cookies_from_browser(d.client, from_browser)
    else:
        update_cookies_from_file(d.client, config.cookies_file)
    client = Client(cookies=d.client.cookies, headers=d.client.headers)
    logined = is_login(client)
    if not logined:
        return

    def check_free_space():
        if min_free_space_gb != 0:
            if (
                get_free_space(
                    path=config.storage_home_dir) // 1024 // 1024 // 1024
                <= min_free_space_gb
            ):
                return False  # not pass
        return True  # pass

    d.progress.start()
    sem = asyncio.Semaphore(config.video_concurrency)
    tasks: List[asyncio.Task] = []

    def tasks_check():
        for task in tasks:
            if task.done():
                _task_exception = task.exception()
                if isinstance(_task_exception, BaseException):
                    print(f"任务 {task} 出错，即将异常退出...")
                    for task in tasks:
                        task.cancel()
                    raise _task_exception
                # print(f'任务 {task} 已完成')
                tasks.remove(task)
        if not check_free_space():
            print(f"剩余空间不足 {min_free_space_gb} GiB")
            for task in tasks:
                task.cancel()
            raise RuntimeError(f"剩余空间不足 {min_free_space_gb} GiB")

    for index, bvid in enumerate(bvids_list):
        if index < skip_to:
            print(f"跳过 {bvid} ({index+1}/{len(bvids_list)})", end="\r")
            continue
        tasks_check()
        if not skip_ia_check:
            upper_part = human_readable_upper_part_map(
                string=bvid, backward=True)
            remote_identifier = f"{BILIBILI_IDENTIFIER_PERFIX}-{bvid}_p1-{upper_part}"
            if check_ia_item_exist(client, remote_identifier):
                print(f"IA 上已存在 {remote_identifier} ，跳过")
                continue

        upper_part = human_readable_upper_part_map(string=bvid, backward=True)
        videos_basepath: Path = (
            config.storage_home_dir / "videos" / f"{bvid}-{upper_part}"
        )
        if os.path.exists(videos_basepath / "_all_downloaded.mark"):
            print(f"{bvid} 所有分p都已下载过了")
            continue

        if len(tasks) >= config.video_concurrency:
            loop.run_until_complete(
                asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            )
            tasks_check()

        print(f"=== {bvid} ({index+1}/{len(bvids_list)}) ===")

        task = loop.create_task(
            archive_bvid(d, bvid, logined=logined, semaphore=sem),
            name=f"archive_bvid({bvid})",
        )
        tasks.append(task)

    while len(tasks) > 0:
        loop.run_until_complete(
            asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        )
        tasks_check()

    print("DONE")


def update_cookies_from_browser(client: AsyncClient, browser: str):
    try:
        import browser_cookie3

        f = getattr(browser_cookie3, browser.lower())
        cookies_to_update = f(domain_name="bilibili.com")
        client.cookies.update(cookies_to_update)
        print(f"从 {browser} 品尝了 {len(cookies_to_update)} 块 cookies")
    except AttributeError:
        raise AttributeError(f"Invalid Browser {browser}")


def update_cookies_from_file(client: AsyncClient, cookies_path: Union[str, Path]):
    if isinstance(cookies_path, Path):
        cookies_path = cookies_path.expanduser()
    elif isinstance(cookies_path, str):
        cookies_path = Path(cookies_path).expanduser()
    else:
        raise TypeError(f"cookies_path: {type(cookies_path)}")

    assert os.path.exists(cookies_path), f"cookies 文件不存在: {cookies_path}"

    from http.cookiejar import MozillaCookieJar

    cj = MozillaCookieJar()

    with HttpOnlyCookie_Handler(cookies_path):
        cj.load(f"{cookies_path}", ignore_discard=True, ignore_expires=True)
        loadded_cookies = 0
        loadded_keys = []
        for cookie in cj:
            # only load bilibili cookies
            if "bilibili.com" not in cookie.domain:
                continue
            if cookie.name in loadded_keys:
                print(f"跳过重复的 cookies: {cookie.name}")
                # httpx 不能处理不同域名的同名 cookies，只好硬去重了
                continue
            assert cookie.value is not None
            client.cookies.set(
                cookie.name, cookie.value, domain=cookie.domain, path=cookie.path
            )
            loadded_keys.append(cookie.name)
            loadded_cookies += 1
        print(f"从 {cookies_path} 品尝了 {loadded_cookies} 块 cookies")
        if loadded_cookies > 100:
            print("吃了过多的 cookies，可能导致 httpx.Client 怠工，响应非常缓慢")

        assert client.cookies.get("SESSDATA") is not None, "SESSDATA 不存在"
        # print(f'SESS_DATA: {client.cookies.get("SESSDATA")}')


def is_login(cilent: Client) -> bool:
    r = cilent.get("https://api.bilibili.com/x/member/web/account")
    r.raise_for_status()
    nav_json = r.json()
    if nav_json["code"] == 0:
        print("BiliBili 登录成功，饼干真香。")
        print(
            "NOTICE: 存档过程中请不要在 cookies 的源浏览器访问 B 站，避免 B 站刷新"
            " cookies 导致我们半路下到的视频全是 480P 的优酷土豆级醇享画质。"
        )
        return True
    print("未登录/SESSDATA无效/过期，你这饼干它保真吗？")
    return False


if __name__ == "__main__":
    raise DeprecationWarning("已废弃直接运行此命令，请改用 biliarchiver 命令")
