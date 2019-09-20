# Author - Liam Edwards
from datetime import datetime, timedelta


def printingDates(count):
    # Prints 1 year of dates - Including time (Get rid of the time)
    dateCount = (datetime.now().date() + timedelta(days=count))
    f.write(f"Work, {dateCount}, FALSE\n")


# CSV Calendar Format
# SUBJECT    START DATE   START TIME    END DATE   END TIME    ALL DAY EVENT

def counting(count):
    # Prints the date 4 times, then counts up 4 days.
    i = 0
    while i < shiftCount:
        j = 0
        while j < 4:
            count += 1
            printingDates(count)
            j += 1

        j = 0
        while j < 4:
            count += 1
            j += 1
        i += 1


# Open a file
with open("rota.csv", "w+") as f:

    # User input
    print("CURRENTLY NO WAY TO UNDO AFTER IMPORTING TO GOOGLE CALENDAR")
    print("Enter a number to offset. e.g. -1 = Today - 0 = Tomorrow")
    count = int(input())
    print("How many 4 day shift periods do you want to generate?")
    shiftCount = int(input())

    # Write to a file
    f.write('Subject, ' + 'Start Date, ' + 'Private\n')
    counting(count)
