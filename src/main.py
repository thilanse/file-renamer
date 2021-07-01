import os
from os.path import dirname, abspath
from threading import Thread

from utils import read_yaml
from watcher import watch_dir

CONF_DIRECTORY = os.path.join(dirname(dirname(abspath(__file__))), "conf")

if __name__ == '__main__':

    configurations = read_yaml(os.path.join(CONF_DIRECTORY, "rename_conf.yml"))

    for conf in configurations:
        renaming_rules = conf["renaming_rules"]

        if "paths" in conf: # If multiple paths with same renaming rules
            for path in conf["paths"]:
                Thread(target=watch_dir, args=(path, renaming_rules)).start()

        elif "path" in conf:
            path = conf["path"]
            Thread(target=watch_dir, args=(path, conf["renaming_rules"])).start()
