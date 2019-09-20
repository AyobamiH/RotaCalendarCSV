# Author - Liam Edwards
from datetime import *

def printingDates(count):
# Prints 1 year of dates - Including time (Get rid of the time)
    dateCount = (datetime.now().date() + timedelta(days=count))
    f.write(f"Work, {dateCount}, FALSE\n")


# CSV Calendar Format
# SUBJECT    START DATE   START TIME    END DATE   END TIME    ALL DAY EVENT   DESCRIPTION   PRIVATE

def counting(count):
    i = 0
    while i < shiftCount:
        inc = 0
        while inc < 4:
            count += 1
            printingDates(count)
            inc += 1

        inc = 0
        while inc < 4:
            count+= 1
            inc += 1
        i += 1
# Open a file
with open("rota.csv", "w+") as f:


    print("WARNING - CURRENTLY NO WAY TO UNDO AFTER IMPORTING TO GOOGLE CALENDAR")
    print("Enter a number to offset the script. e.g. -1 = Today or 0 = Tomorrow")
    count = int(input())
    print("How many 4 day shift period do you want to generate?")
    shiftCount = int(input())

    # Write to a file
    f.write('Subject, '+'Start Date, ' +'Private\n')
    counting(count)
