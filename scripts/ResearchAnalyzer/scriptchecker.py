
import adminfile


def arranger(detailed_log_path, click_images_log_path):

    #keyspath = '.\logs_to_treat\logs-USER-1518205759\detailed_log\detailedlogfile_USER.txt'
    keysfile = adminfile.readfile(detailed_log_path)
    keysfile = keysfile.replace("key down", "key_down,-1,-1")
    keysfile = keysfile.replace("key up", "key_up,-1,-1")
    #print keysfile
    detailed_log_path = detailed_log_path.replace(".txt", "_new.txt")
    adminfile.writefile(detailed_log_path, keysfile)

    clicksfile = adminfile.readfile(click_images_log_path)
    clicksfile = clicksfile.replace("mouse left up", "left_up")
    clicksfile = clicksfile.replace("mouse left down", "left_down")

    pipe = 0
    comma = 0
    clicksfile_adds = ""
    for i in range(0, clicksfile.__len__()):
        char = clicksfile[i]
        if char == "\n":
            pipe = 0
            clicksfile_adds += char
        elif pipe == 5 and clicksfile[i-1] == "|":
            if char == "|":
                pipe += 1
                clicksfile_adds += "Abrir|"
            else:
                clicksfile_adds += char
        elif pipe == 7:
            if comma == 4:
                if char == "g":
                    temp = clicksfile[i-3] + clicksfile[i-2] + clicksfile[i-1] + char
                    if temp == ".png":
                        comma = 0
                        clicksfile_adds += char
                    else:
                        clicksfile_adds += char
                elif char == " ":
                    clicksfile_adds += "_"
                else:
                    clicksfile_adds += char
            elif char == ",":
                clicksfile_adds += char
                comma += 1
            else:
                clicksfile_adds += char
        elif char == "|":
            pipe += 1
            clicksfile_adds += char
        else:
            clicksfile_adds += char

    click_images_log_path = click_images_log_path.replace(".txt", "_new.txt")
    adminfile.writefile(click_images_log_path, clicksfile_adds)
    #print(clicksfile)


"""def main():
    arranger("w", ".\logs_to_treat\logs-USER-1518205759\click_images\clickimagelogfile_USER.txt")


if __name__ == "__main__":
    main()"""
