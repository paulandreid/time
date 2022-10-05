from asyncio.windows_events import NULL
from ctypes import sizeof
from datetime import date, time, datetime
import json
from operator import truediv
import sys

def newTask():
    f = open("entries.txt", "a")
    description = input("Description: ")
    f.write(str(datetime.now()) + ',' + description)
    f.close()


def add_task():
    description = input()

    if task_still_runnig() == True:
        end_task()

    startTime = str(datetime.now())

    f = open("entries.txt", "a", newline='')
    f.write('\n' + startTime + "," + description)
    f.close()


def last_line():
    with open("entries.txt") as f:
        for line in f:
            pass
        last_line = line
    return last_line


def end_task():

    line = last_line()
    startTime = line.split(",")[0]
    duration = datetime.now() - datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S.%f")
    f = open("entries.txt", "a", newline='')
    f.write(","+str(round(duration.seconds / 3600, 2)))


def task_still_runnig():

    line = last_line()
    line = line.split(",")
    if len(line) == 2:
        print("current task: " + line[1])
        return True
    return False


if __name__ == "__main__":
    # start()
    decision = input("1: End current task \n" +
                     "2: Start new task ")
    if decision == '1':
        if task_still_runnig() == True:
            end_task()
        else:
            print("no task running")
    else:
        add_task()
