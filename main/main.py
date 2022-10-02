from asyncio.windows_events import NULL
from ctypes import sizeof
from datetime import date, time, datetime
import json
from operator import truediv

#description = input()
#account = input()
start = datetime.now()

#input()
timeElapsed = datetime.now() - start
#print(datetime.datetime.)
#print(str(datetime.datetime.date(datetime.datetime.now())) + " " + description + "\n   " + account +" " +str(timeElapsed))




def toHours(dateStart, dateEnd):

    timeDelta = dateEnd - dateStart # returnes timedalte
    seconds = timeDelta.total_seconds()
    return round(seconds / 3600, 2)

def newTask():
    f = open("entries.txt", "a")   
    description = input("Description: ")
    f.write( str(datetime.now()) + ',' + description)
    f.close()
    

def start():
    description = input()

    if task_still_runnig() == False:
        read_last_entry()
    startTime = str(datetime.now())

    f = open("entries.txt", "a", newline='')
    f.write('\n' + startTime + "," + description) #
    f.close()


def read_last_entry():


    with open("entries.txt") as f:
        for line in f:
          pass
        last_line = line

    startTime = last_line.split(",")[0]
    duration = datetime.now() - datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S.%f") 
    print(round(duration.seconds / 60,2))
    f = open("entries.txt", "a", newline='')    
    f.write(","+str(round(duration.seconds / 60 ,2)))

def task_still_runnig():
    with open("entries.txt") as f:
        for line in f:
            pass
        last_line = line
        f.close()
        last_line = last_line.split(",")
        if len(last_line) == 2 :
            print("current task: " + last_line[1])
            return True
    return False




if __name__ == "__main__":  
    #start()
    decision = input("1: End current task \n" +
                     "2: Start new task ")
    if decision == '1':
        if task_still_runnig()==True:
            read_last_entry()
        else:
            print("no task running")
    else:
        start()