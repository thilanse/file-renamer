import os
import re


def rename_files(path):
    os.chdir(path)

    for file in os.listdir():

        if re.match(".*lookup.*", file):
            os.rename(file, "lookup.csv")

        if re.match(".*keyword.*", file):
            os.rename(file, "keyword.csv")

        if re.match(".*intent_specific.*", file):
            os.rename(file, "is.csv")

        if re.match(".*label_split.*", file):
            os.rename(file, "label_split.csv")

        if re.match(".*basic.*", file):
            if re.match(".*basic_regex.*", file):
                os.rename(file, "basic_regex.csv")
            else:
                os.rename(file, "basic.csv")


if __name__ == '__main__':
    path = "F:\\github-projects\\test-dir"
    rename_files(path)
