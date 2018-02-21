
###########################
#
# Pruebas de concepto
#
###########################
from loginfo import LogInfo
import os
import scriptchecker
import xlsxwriter

path = os.getcwd() + "\logs_to_treat\\"

logsList = os.listdir(path)

listLogInfo = []


def load_loginfo():
    for logfolder in logsList:
        click_images = os.path.join(path, logfolder+"\\click_images\\")
        detailed_log = os.path.join(path, logfolder+"\\detailed_log\\")
        system_log = os.path.join(path, logfolder + "\\system_log\\")
        timed_screenshot = os.path.join(path, logfolder + "\\timed_screenshots\\")

        clickbool = True
        detailedbool = True

        click_images_files = [f for f in os.listdir(click_images) if f.endswith('.txt')]
        if click_images_files.__len__() == 1:
            click_fn = os.path.join(click_images, click_images_files[0])
        elif click_images_files.__len__() == 2 and click_images_files[1].__contains__("_new.txt"):
            click_fn = os.path.join(click_images, click_images_files[0])
            clickbool = False
        else:
            print("Failed to locate the file click_images")
            exit()

        detailed_log_files = [f for f in os.listdir(detailed_log) if f.endswith('.txt')]
        if detailed_log_files.__len__() == 1:
            keys_fn = os.path.join(detailed_log, detailed_log_files[0])
        elif detailed_log_files.__len__() == 2 and detailed_log_files[1].__contains__("_new.txt"):
            keys_fn = os.path.join(detailed_log, detailed_log_files[0])
            detailedbool = False
        else:
            print("Failed to locate the file detailed_log")
            exit()

        if clickbool and detailedbool:
            scriptchecker.arranger(keys_fn, click_fn)
        keys_fn_new = keys_fn.replace(".txt", "_new.txt")
        click_fn_new = click_fn.replace(".txt", "_new.txt")

        system_log_files = [f for f in os.listdir(system_log) if f.endswith('.txt')]
        if system_log_files.__len__() == 1:
            system_fn = os.path.join(system_log, system_log_files[0])

        elif system_log_files.__len__() == 2 and system_log_files[1].__contains__("_new.txt"):
            system_fn = os.path.join(system_log, system_log_files[1])

        else:
            print("Failed to locate the file system_log")
            exit()

        timed_screenshot_files = [f for f in os.listdir(timed_screenshot) if f.endswith('.txt')]
        if timed_screenshot_files.__len__() == 1:
            screenshoots_fn = os.path.join(timed_screenshot, timed_screenshot_files[0])

        elif timed_screenshot_files.__len__() == 2 and timed_screenshot_files[1].__contains__("_new.txt"):
            screenshoots_fn = os.path.join(timed_screenshot, timed_screenshot_files[1])

        else:
            print("Failed to locate the file timed_screenshot")
            exit()

        li = LogInfo(click_fn_new,  # Your click data file here
                     keys_fn_new,  # Your detailed log file here
                     screenshoots_fn,  # Your timed screenshot log file here
                     system_fn,  # Your system log data here"""
                     )

        listLogInfo.append(li)


def generate_data():
    for li in listLogInfo:
        # print "time by active active window", li.get_time_by_active_window()

        print "------------------------------"
        # Print clicks summary info.
        print "Unique pressed clicks:", li.get_unique_pressed_clicks()
        print
        print "In-order pressed clicks:", li.get_all_pressed_clicks()
        print
        print li.get_click_info()
        li.print_click_summary()

        print "------------------------------"
        # Print keys summary info.
        print "Unique pressed keys:", li.get_unique_pressed_keys()
        print
        print "In-order pressed keys:"
        for f in li.get_all_pressed_keys():
            keystroke, event_type, window, window_title = f
            print window, ":\t", window_title, "\t", event_type, "\t", keystroke
        for f in li.get_letter_info():
            print f
        li.print_key_summary()

        print "------------------------------"
        # Get the time spent in each window.
        print "Time spent in:"
        times_by_window = li.get_time_by_active_window()
        for k in times_by_window:
            print "\t * '%s' = %s ms" % (k, times_by_window[k])

        # Plots the keystroke progression graph.
        # li.plot_keystroke_progression_graph(1)

        # Plots the clicks progression graph.
        # li.plot_clicks_progression_graph(1)

        # Print pauses in interval [0, 5000000]
        # li.print_pauses(0, 5000000)
        # li.print_pause_summary(0, 5000000)


def write_excel():
    print "Hola Mundo"
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('myexcel.xlsx')
    worksheet = workbook.add_worksheet("hola")

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)

    # Insert an image.
    worksheet.insert_image('B5', 'logo.png')

    workbook.close()


#load_loginfo()
#generate_data()
write_excel()
