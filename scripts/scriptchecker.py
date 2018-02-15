#!/usr/bin/python3

import adminfile
import sys


def arranger():

    keyspath = '.\..\Kit_ResearchLogger\ResearchLogger\logs-USER-1518205759\detailed_log\detailedlogfile_USER.txt'
    keysfile = adminfile.readfile(keyspath)
    keysfile = keysfile.replace("key down", "key_down")
    keysfile = keysfile.replace("key up", "key_up")
    print keysfile
    adminfile.writefile("detailedlogfile_USER_new.txt", keysfile)

    print("\n")
    print("clicks")
    clickspath = ".\..\Kit_ResearchLogger\ResearchLogger\logs-USER-1518119622\click_images\clickimagelogfile_USER.txt"
    clicksfile = adminfile.readfile(clickspath)
    clicksfile = clicksfile.replace("mouse left up", "mouse_left_up")
    clicksfile = clicksfile.replace("mouse left down", "mouse_left_down")
    adminfile.writefile("clickimagelogfile_USER_new.txt", clicksfile)
    print(clicksfile)


def main():
    """args = sys.argv[1:]

    if '--chequear' in args:
        foo()
    """
    arranger()


if __name__ == "__main__":
    main()
