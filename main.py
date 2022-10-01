from datetime import time, datetime

#description = input()
#account = input()
start = datetime.now()

#input()
timeElapsed = datetime.now() - start
#print(datetime.datetime.)
#print(str(datetime.datetime.date(datetime.datetime.now())) + " " + description + "\n   " + account +" " +str(timeElapsed))
input()



def toHours(dateStart, dateEnd):

    timeDelta = dateEnd - dateStart # returnes timedalte
    seconds = timeDelta.total_seconds()
    return round(seconds / 3600, 2)

print(toHours(start, datetime.now()))