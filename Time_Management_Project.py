import time
import sys
import calendar
import tkinter as tk
from tkinter.ttk import *
from datetime import date
import os

print('------------- Welcome -------------')

# Calender
def get_calendar():
    year = int(input("Enter year: "))
    #month = int(input("Enter month: "))
    #print(calendar.month(year, month)) # print month
    print(calendar.calendar(year))

def get_today():
    today = date.today() # today's date
    # today.isoformat()
    today_string = today.strftime("%m/%d/%Y")
    print("today is: ", today_string)
    t = today.timetuple()
    this_year = t[0]
    this_month = t[1]
    this_day = t[2]
    this_date = t[6]  # 0 is Monday
    i_th_day= t[7]

def create_file():
    fileName = input("Enter file name: ") + ".txt"
    myFile = open(fileName, 'w')  #write mode -  overwrite
    myFile.close()

def write_file():
    get_date = input("Please enter date you want to save to in yyyy/mm/dd: ")
    total_list = []
    year_list = []
    month_list = []
    date_list = []
    content = []

    for i in get_date:
        if i != '/':  # remove '/'
            total_list.append(i)
    #total_list = [int(j) for j in date_list]  # convert list of string to list of int -- not necessary
    year = ''.join(total_list[0:4])  #string, can use int() to convert
    month = ''.join(total_list[4:6])
    day = ''.join(total_list[6:8])
    L = ["Year: ", year, " Month: ", month, " Day: ", day, "\n"]
    print("Your Diary begins here: \n")

    # can input multiple lines (ref 1)
    while True:
        content_in = input()
        if content_in:
            content.append(content_in)
        else:
            break
    text = '\n'.join(content)

    myFile = open("Diary.txt",'a')
    myFile.writelines(L)
    myFile.write(text)
    myFile.close()

    ans = input("Would like to view your diary ?(Y/N): ")
    if ans == 'Y':
        myFile = open("Diary.txt",'r')
        content = myFile.readlines()
        for x in content:
            print(x)
        myFile.close()
    else:
        exit()

def create_timer():
    seconds = 0
    minutes = 0

    choice = input("a)Regular Timer \n b)Tomato Method Timer\n")

    if choice == 'a':
        ans = input("Timer starts ?(Y/N): ")

        if ans == 'N':
            pass
        if ans == 'Y':
            while True:
                # method 2
                try:
                    time.sleep(1)
                    seconds += 1
                    if seconds >= 60:
                        minutes += 1
                        seconds = 0
                    print(minutes, " minutes and ", seconds," seconds")
                except KeyboardInterrupt: # works well in IDLE, not here
                    break

            #total_min = minutes
            #total_sec = seconds
            print("Total time: ", minutes, " minutes and ", seconds, " seconds.")

            '''method 1
            print("{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
            #sys.stdout.flush() # write everything in the buffer to terminal
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            if seconds >= 60:
                minutes += 1
               seconds = 0  ##### while loop never exit
            '''
    if choice == 'b':
        tomato_short = 25 #usually 25 mins + 5 min break as a cycle
        break_short = 5
        break_long = 30 # long break after every 4 tomatos
        short_list = [tomato_short, break_short, break_long]
        count = 0 # count number of tomato
        start = time.time()
        total_short = 0
        total_long = 0

        while True:
            try:
                if count == 0:
                    for j in range(4):
                        for i in short_list[0:2]:
                            time.sleep(i)
                        count += 1
                        total_short += 1
                        print(count)
                if count == 4:
                    for x in short_list[0::2]:
                        time.sleep(x)
                    count = 0
                    total_long += 1
                    print(count)

                print(time.time() - start)
                ans = input("Enter 'e'to exit: ")
                if ans == 'e':
                    break
                else:
                    pass
            except KeyboardInterrupt:
                break

    answer =  input("Would you like to save your record? (Y/N): ")
    if answer == "Y":
        today = date.today()  # today's date
        today_string = today.strftime("%m/%d/%Y")
        myFile = open("TimeRecord.txt", 'a')
        myFile.write(today_string)
        if choice == 'a':
            total_time = ["\rTotal time today: ", str(minutes), " minutes ", str(seconds), " seconds\n"]
        if choice == 'b':
            # Here is 4 short + 1 long
            # short = 30 min, long = 55 min
            total_time = ["\rTotal time today: ", str(total_short * 30 + total_long * 55), " minutes \n"]
        myFile.writelines(total_time)
        myFile.close()
    if answer == "N":
        exit()

def digital_clock():  # ref 2
    string_time = time.strftime('%H:%M:%S %p')
    lbl.config(text = string_time)
    lbl.after(1000, digital_clock)

def timer():
    d = str(t.get())
    h, m, s = map(int, d.split(":"))
    h = int(h)
    m = int(m)
    s = int(s)
    if (s < 59):
        s += 1
    elif (s == 59):
        s = 0
        if (m < 59):
            m += 1
        elif (m == 59):
            h += 1
    if (h < 10):  ############format#############
        h = str(0) + str(h)
    else:
        h = str(h)
    if (m < 10):
        m = str(0) + str(m)
    else:
        m = str(m)
    if (s < 10):
        s = str(0) + str(s)
    else:
        s = str(s)
    d = h + ":" + m + ":" + s
    t.set(d)
    root.after(1000, timer)

def countdown_timer():
    d = str(t.get())
    h, m, s = map(int, d.split(":"))
    h = int(h)
    m = int(m)
    s = int(s)
    print(h, m, s)
    if (h == 0):
        if (m == 0):
            if (s == 0):
                exit()
        if (s == 0):
            s = 59
            if (m == 0):
                m = 59
                h -= 1
                print(h, m)
            elif (m <= 59):
                m -= 1
                print("new min:", m)
        elif (s <= 59):
            s -= 1
    else:
        if (s == 0):
            s = 59
            if (m == 0):
                m = 59
                h -= 1
                print(h, m)
            elif (m <= 59):
                m -= 1
                print("new min:", m)
        elif (s <= 59):
            s -= 1
            
    if (h < 10):  ############format#########
        h = str(0) + str(h)
    else:
        h = str(h)
    if (m < 10):
        m = str(0) + str(m)
    else:
        m = str(m)
    if (s < 10):
        s = str(0) + str(s)
    else:
        s = str(s)
    d = h + ":" + m + ":" + s
    t.set(d)
    root.after(1000, countdown_timer)

def dialog_box():
    root = tk.Tk()
    root.title('Calendar')
    Label(root, text = 'Year').grid(row = 0)
    e1 = Entry(root)
    e1.grid(row = 0, column = 1)
    button = tk.Botton(root, text = 'Show', width = 20).grid(row = 1, column = 1)
    button.pack()
    root.mainloop()


#################################################
print("Menu:\n 1)Calendar \n 2)Today's date\n 3)Create a new file\n "
      "4)Write a diary\n 5)Timer\n 6)Show timer \n 7)Count Down timer\n 0)Exit")
print("--------------------------------------")
answer = int(input("Please enter your choice: "))

while (answer != 0):
    if answer == 1:
        get_calendar()
    if answer == 2:
        get_today()
    if answer == 3:
        create_file()
    if answer == 4:
        write_file()
    if answer == 5:
        create_timer()
        # GUI local timer
        '''
        root = tk.Tk()
        root.title('Clock')
        lbl = Label(root, font = ('calibri', 40, 'bold'),
                background = 'white',
                foreground = 'black')
        lbl.pack(anchor = 'center')
        digital_clock()
        root.mainloop()
        '''
    if answer == 6:
        root = tk.Tk()
        root.title("Stop Watch")
        root.resizable(False, False)
        t = tk.StringVar()
        t.set("00:00:00")
        lb = Label(root, textvariable=t)
        lb.config(font=("Courier 40 bold"))
        timer()
        lb.pack()
        root.mainloop()
    if answer == 7:
        root = tk.Tk()
        root.title("Stop Watch")
        root.resizable(False, False)
        t = tk.StringVar()
        t.set("02:00:00")
        lb = tk.Label(root, textvariable=t)
        lb.config(font=("Courier 40 bold"))
        countdown_timer()
        lb.pack()
        root.mainloop()
    else:
        print("Invalid input 0w0")

    print("Menu:\n 1)Calendar \n 2)Today's date\n 3)Create a new file\n "
          "4)Write a diary\n 5)Timer\n 6)Show Timer \n 7)Count Down Timer \n 0)Exit")
    answer = int(input("Please enter your choice: "))



'''
ref 1: https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user
ref 2: https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/
'''
