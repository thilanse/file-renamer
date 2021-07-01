import os
import re
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def rename_files(path, conf):
    os.chdir(path)

    for file in os.listdir():

        if not os.path.exists(file):
            continue

        target_file_names = [target_file["target_filename"] for target_file in conf]

        if file in target_file_names:
            continue

        if file.split(".")[1] not in ['csv']:
            continue

        print("Attempting to rename file...", file)

        time.sleep(0.1)

        try:
            for target in conf:
                file_name = target["target_filename"]
                if re.match(target["regex"], file):
                    os.rename(file, file_name)
                    print(f"Renamed {file} to {file_name}")

        except (FileExistsError, FileNotFoundError):
            pass


class MyHandler(FileSystemEventHandler):

    def __init__(self, path=None, rename_conf = None):
        super().__init__()
        self.path = path
        self.rename_conf = rename_conf

    def on_moved(self, event):
        super().on_moved(event)
        rename_files(self.path, self.rename_conf)

    def on_created(self, event):
        super().on_created(event)
        rename_files(self.path, self.rename_conf)

    def on_deleted(self, event):
        super().on_deleted(event)
        print("Deleted", event.src_path)
        rename_files(self.path, self.rename_conf)

    def on_modified(self, event):
        super().on_modified(event)
        rename_files(self.path, self.rename_conf)


def watch_dir(path, rename_conf):

    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
    else:
        print(f"Watching file modifications on path: {path}")
        event_handler = MyHandler(path, rename_conf)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        finally:
            observer.stop()
            observer.join()
