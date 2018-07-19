class DateMaker(object):
    year = 0
    month = 0
    day = 0
    monthCount = 0
    leap = 0
    vLength = False
    vFormat = False
    vIllegals = False
    vMonth = False
    vDay = False
date = DateMaker()

def Error(): #tracks and reports errors
    x = 0
    if date.vLength == True or date.vFormat == True or date.vIllegals == True or date.vMonth == True or date.vDay == True:
        print("An error has occured:")
    else:
        x = x + 1
    if date.vLength == True:
        print("The date is too short")
    else:
        x = x + 1
    if date.vFormat == True:
        print("The date is misfromated")
    else:
        x = x + 1
    if date.vIllegals == True:
        print("There are illegal characters")
    else:
        x = x + 1
    if date.vMonth == True:
        print("There is an invalid number of months")
    else:
        x = x + 1
    if date.vDay == True:
        print("Invalid number of days")
    else:
        x = x + 1
    if x == 6:
        print("This is a valid date.")
    GetDate()
    
    
def GetDate():#organizes variables
    date.year = 0
    date.month = 0
    date.day = 0
    date.monthCount = 0
    date.leap = 0
    date.vLength = False
    date.vFormat = False
    date.vIllegals = False
    date.vMonth = False
    date.vDay = False



    
    print("Please enter a date formated MM/DD/YYYY.")
    userDate = input()
    
    if len(userDate) < 7:
        date.vLength = True
        Error()#checks for impossible date
    elif userDate[2] != "/" or userDate[5] != "/":
        date.vFormat = True
        Error()#checks date format
        
    i = 0
    while i < len(userDate):
        if userDate[i] == "0":
            b = 0
            

        elif userDate[i] == "1":
            b = 0

        elif userDate[i] == "2":
            b = 0

        elif userDate[i] == "3":
            b = 0

        elif userDate[i] == "4":
            b = 0

        elif userDate[i] == "5":
            b = 0

        elif userDate[i] == "6":
            b = 0

        elif userDate[i] == "7":
            b = 0

        elif userDate[i] == "8":
            b = 0

        elif userDate[i] == "9":
            b = 0

        elif userDate[i] == "/":
            b = 0

        else:
            date.vIllegals = True
            Error()
        i = i + 1
        #checks for invalid characters
    
    
    date.month = int(userDate[0:2])
    date.day = int(userDate[3:5])
    if len(userDate) > 7:
        date.year = int(userDate[6:-1])# sets values for month day and year and makes them int
    else:
        date.year = int(userDate[6])
                        
    if (date.year % 4) == 0:
        if (date.year % 100) == 0:
            if (date.year % 400) == 0:
                date.leap = True
            else:
                date.leap = False
        else:
            date.leap = True
            
    else:
        date.leap = False
# checks leap year
    

    
    if date.month > 12 or date.month <= 0:
        date.vMonth = True#checks month
    
    
    if date.month == 1:
        if date.day > 31 or date.day < 0:
            date.vDay = True
    elif date. month == 2:
        if date.leap == True:
            if date.day > 29 or date.day < 0:
                date.vDay = True
        elif date.leap == False:
            if date.day > 28 or date.day < 0:
                date.vDay = True
    elif date. month == 3:
        if date.day > 31 or date.day < 0:
            date.vDay = True
    elif date. month == 4:
        if date.day > 30 or date.day < 0:
            date.vDay = True
    elif date. month == 5:
        if date.day > 31 or date.day < 0:
            date.vDay = True
    elif date. month == 6:
        if date.day > 30 or date.day < 0:
            date.vDay = True
    elif date. month == 7:
        if date.day > 31 or date.day < 0:
            date.vDay = True
    elif date. month == 8:
        if date.day > 31 or date.day < 0:
            date.vDay = True
    elif date. month == 9:
        if date.day > 30 or date.day < 0:
            date.vDay = True
    elif date. month == 10:
        if date.day > 31 or date.day < 0:
            date.vDay = True
    elif date. month == 11:
        if date.day > 30 or date.day < 0:
            date.vDay = True
    elif date. month == 12:
        if date.day > 31 or date.day < 0:
            date.vDay = True
    # checks for a valid number days in the month
    
    
    
    Error()
    GetDate()

GetDate()

    




