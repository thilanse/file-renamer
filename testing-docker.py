import os
import re
import time


def rename_files(path):
    os.chdir(path)

    for file in os.listdir():

        if not os.path.exists(file):
            continue

        if file in ['lookup.csv', 'keyword.csv', 'label_split.csv',
                    'is.csv', 'basic.csv', 'basic_regex.csv']:
            continue

        if file.split(".")[1] not in ['csv']:
            continue

        print("Attempting to rename file...", file)

        time.sleep(0.1)

        try:
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
        except FileExistsError:
            pass


if __name__ == '__main__':
    dir_path = os.getcwd() + "/test"
    # dir_path = "F:\\github-projects\\file-renamer\\test"
    print("Listening...")
    rename_files(dir_path)
