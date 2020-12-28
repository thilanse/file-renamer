import os
import re
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def rename_files(path):
    os.chdir(path)

    for file in os.listdir():

        if not os.path.exists(file):
            continue

        if file in ['lookup.csv', 'keyword.csv', 'label_split.csv',
                    'is.csv', 'basic.csv', 'basic_regex.csv']:
            continue

        print("Attempting to rename file...", file)

        time.sleep(0.1)

        if re.match(".*lookup.*", file):
            os.rename(file, "lookup.csv")
            print("Renamed", file, "to lookup.csv")

        if re.match(".*keyword.*", file):
            os.rename(file, "keyword.csv")
            print("Renamed", file, "to keyword.csv")

        if re.match(".*intent_specific.*", file):
            os.rename(file, "is.csv")
            print("Renamed", file, "to is.csv")

        if re.match(".*label_split.*", file):
            os.rename(file, "label_split.csv")
            print("Renamed", file, "to label_split.csv")

        if re.match(".*basic.*", file):
            if re.match(".*basic_regex.*", file):
                os.rename(file, "basic_regex.csv")
                print("Renamed", file, "to basic_regex.csv")
            else:
                os.rename(file, "basic.csv")
                print("Renamed", file, "to basic.csv")


class MyHandler(FileSystemEventHandler):

    def __init__(self, path=None):
        super().__init__()
        self.path = path

    def on_moved(self, event):
        super().on_moved(event)
        rename_files(self.path)

    def on_created(self, event):
        super().on_created(event)
        rename_files(self.path)

    def on_deleted(self, event):
        super().on_deleted(event)
        what = 'directory' if event.is_directory else 'file'
        print("Deleted", event.src_path)

    def on_modified(self, event):
        super().on_modified(event)
        rename_files(self.path)


def watch_dir(path):
    event_handler = MyHandler(path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == '__main__':
    # path = os.getcwd() + '/test'
    path = "F:\\github-projects\\file-renamer\\test"
    print("Listening...")
    watch_dir(path)
