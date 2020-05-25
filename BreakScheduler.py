import webbrowser
import time


def breakscheduler():

    m = int(input("Enter the number of times you want break = "))
    n = 2 #after how many hours you want break
    gettime = time.localtime()  # get struct_time
    hours = gettime.tm_hour
    # time_string = time.strftime("%m/%d/%Y, %H:%M:%S", gettime)

    for i in range(m):
        track_of_time = hours + n  #keeps the track of hours after which you want break

        # if n equals the current time then it's the break time
        if track_of_time == time.localtime().tm_hour:
            link = input("Enter a website link you want to open : ")
            activity = webbrowser.open_new_tab(link)
        else:
            print("Wait till break time......")


breakscheduler()







