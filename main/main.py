from asyncio.windows_events import NULL
from datetime import date, time, datetime
import json

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

def start():
    description = input()
    startTime = str(datetime.now())
    dictJson = {
        "description" : description,
        "start" : startTime
    }

    print(json.dumps(dictJson))

    f = open("entries.txt", "a")
    f.write(startTime + "," + description) #
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
    f.write(","+str(round(duration.seconds / 60 ,2))+"\n")



if __name__ == "__main__":  
    #start()
    decision = input()
    if decision == '1':
        read_last_entry()
    else:
        start()