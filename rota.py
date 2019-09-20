from datetime import *

f=open("rota.csv", "w+")


def printingDates(count):
# Prints 1 year of dates - Including time (Get rid of the time)
    dateCount = (datetime.now().date() + timedelta(days=count))
    f.write(f"Work, {dateCount}, FALSE\n")



# Excel Calender Format
# SUBJECT    START DATE   START TIME    END DATE   END TIME    ALL DAY EVENT   DESCRIPTION   PRIVATE
count = int(input())

def counting(count):
    inc = 0
    while inc < 4:
        count += 1
        printingDates(count)
        inc += 1

    inc = 0
    while inc < 4:
        count+= 1
        inc += 1
    inc = 0
    while inc < 4:
        count += 1
        printingDates(count)
        inc += 1

f.write('Subject, '+'Start Date, ' +'Private\n')
counting(count)
