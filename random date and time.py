import random
import time
def getRandomDate ( startdate , enddate ):
    print("Printing random date", startdate, "and" , enddate )
    randomGenerator = random.random()
    dateformat = '%m/%d/%Y'

    starttime = time.mktime(time.strptime (startdate,dateformat))
    endtime = time.mktime(time.strptime (enddate,dateformat))

    randomTime = starttime + randomGenerator *(endtime - starttime)
    randomDate = time.strftime(dateformat.time.localtime(randomTime))
    return randomDate
print("Random Date = ", getRandomDate ("1/1/2016" , "1/13/2018") )