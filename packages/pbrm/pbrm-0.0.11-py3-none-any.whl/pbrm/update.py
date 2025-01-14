import json

from pbrm import spider
from pbrm import save_illust
from pbrm import utils
import os
from pbrm import delete


def work_exists(pid: str, path: str, unavailable: bool, is_gif: bool, num: int):
    if os.path.exists(path + "/" + pid) and os.path.isdir(path + "/" + pid):
        # 判断是否保存完全(防止因网络原因导致的下载中断)
        if len(os.listdir(path + "/" + pid)) >= (1 if unavailable else (num + 4 if is_gif else num + 2)):
            return True
        else:
            return False

    return False


# 失效的作品的id和userId是整形而不是字符串
def update(cookie: str, path: str, skip_download: bool, skip_meta: bool, force_update: bool, force_update_illust: bool
           , force_update_meta: bool, auto_remove: bool, save_gif: bool):

    if not (os.path.exists(path) and os.path.isdir(path)):
        os.mkdir(path)

    # 合并force_update_illust和force_update_meta
    if force_update_meta is True and force_update_illust is True:
        force_update = True
    user = spider.cookie_verify(cookie)
    bookmarks = spider.get_bookmarks(cookie, user["userId"])
    log = {"updateTime": utils.get_time(), "total": bookmarks["total"], "updated": 0, "unavailable": 0}
    print("userId: {} userName: {} total: {}".format(user["userId"], user["userName"], bookmarks["total"]))

    i = 0
    all_illust = []
    for illust in bookmarks["illust"]:
        i = i + 1
        all_illust.append(str(illust["id"]))
        print("update: " + str(illust["id"]) + " process: {}/{}".format(str(i), bookmarks["total"]))
        if not force_update:
            if work_exists(str(illust["id"]), path, illust["userId"] == 0, save_gif and (illust["illustType"] == 2), illust["pageCount"]):
                if force_update_meta != force_update_illust and illust["userId"] != 0:
                    # 将force当skip用
                    log["updated"] += 1
                    save_illust.save_illust(illust["id"], path + "/" + illust["id"], cookie, save_gif
                                            , not force_update_illust, not force_update_meta)
                continue

        if not (os.path.exists(path + "/" + str(illust["id"])) and os.path.isdir(path + "/" + str(illust["id"]))):
            os.mkdir(path + "/" + str(illust["id"]))

        if illust["userId"] == 0:
            log["unavailable"] += 1
            save_illust.save_unavailable(illust, path + "/" + str(illust["id"]))
            continue

        log["updated"] += 1
        save_illust.save_illust(illust["id"], path + "/" + illust["id"], cookie, save_gif, skip_download, skip_meta)

    if auto_remove:
        illusts = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        for i in illusts:
            if i not in all_illust:
                delete.delete(os.path.join(path, i))

    with open(os.path.join(path, "log.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False))

    with open(os.path.join(path, "bookmarks.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(bookmarks, ensure_ascii=False))

