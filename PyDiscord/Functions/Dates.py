# PyDiscord | Functions > Dates






#Imports
from calendar import timegm
from time import ctime, asctime, gmtime, strptime, timezone





#Public Functions
def creationDateUTC(given: int) -> str:
    return asctime(gmtime(float(int(bin(given)[2:][::-1][22:][::-1], 2) + 1420070400000) / 1000.0))



def creationDateLocal(given: int) -> str:
    return ctime(float(int(bin(given)[2:][::-1][22:][::-1], 2) + 1420070400000) / 1000.0)



def dateToEpoch(datetime: str) -> int:
    date: list = datetime.split('-')
    date[2] = date[2].split('T')[0]

    thetime: str = datetime.split('T')[1].split('+')[0]
    miliseconds: int = int(thetime.split('.')[1])
    thetime; str = thetime.split('.')[0]

    return ((timegm(strptime(('-'.join(date) + ' ' + thetime), '%Y-%m-%d %H:%M:%S')) * 1000) + miliseconds) + (timezone / -3600)



def dateToUTC(date: str) -> str:
    return asctime(gmtime(float(dateToEpoch(date) / 1000.0)))



def dateToLocal(date: str) -> str:
    return ctime(float(dateToEpoch(date) / 1000.0))