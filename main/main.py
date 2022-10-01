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
    f.write(startTime + "," + description + "\n") #
    f.close()


#def read_last_entry:




if __name__ == "__main__":  
    start()