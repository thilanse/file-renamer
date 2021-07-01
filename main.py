from threading import Thread

from src.utils import read_json
from src.watcher import watch_dir


if __name__ == '__main__':

    configurations = read_json("rename_conf.json")

    for conf in configurations:
        path = conf["path"]
        Thread(target=watch_dir, args=(path, conf["renaming_rules"])).start()
