class DateMaker(object):
    year = 0
    month = 0
    day = 0
    monthCount = 0
    leap = 0
def GetDate():
    print("Please enter a date formated MM/DD/YYYY.")
    userDate = input()
    if len(userDate) > 10:
        print("Error: Date is too long.")
        GetDate()#checks date length
    elif len(userDate) <10:
        print("Error: Date is too short.")
        GetDate()
    elif userDate[2] != "/" or userDate[5] != "/":
        print("Error: Date is incorectly formated, \"/\" is missing or misplaced.")
        GetDate()#checks date format
        
    i = 0
    while i < 10:
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
            print("Error: Invalid character entry.")
            GetDate()
        i = i + 1
        #checks for invalid characters
    
    date = DateMaker()
    date.month = int(userDate[0:2])
    date.day = int(userDate[3:5])
    date.year = int(userDate[6:10])# sets values for month day and year and makes them int
    
    if (date.year % 4) == 0 :
        if (date.year % 100) == 0:
            if (date.year % 400) == 0:
                date.leap = True
            else:
                date.leap = False
        else:
            date.leap = True
            #checks leap year
    else:
        date.leap = False
# checks leap year
    

    
    if date.month > 12 or date.month <= 0:
        print("Error: Invalid month.")
        GetDate()#checks month

    
    
    
    if date.month == 1:
        if date.day > 31 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 2:
        if date.leap == True:
            if date.day > 29 or date.day < 0:
                print("Error: Invalid number of days.")
                GetDate()
        elif date.leap == False:
            if date.day > 28 or date.day < 0:
                print("Error: Invalid number of days.")
                GetDate()
    elif date. month == 3:
        if date.day > 31 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 4:
        if date.day > 30 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 5:
        if date.day > 31 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 6:
        if date.day > 30 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 7:
        if date.day > 31 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 8:
        if date.day > 31 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 9:
        if date.day > 30 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 10:
        if date.day > 31 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 11:
        if date.day > 30 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    elif date. month == 12:
        if date.day > 31 or date.day < 0:
            print("Error: Invalid number of days.")
            GetDate()
    # checks for a valid number days in the month
    
    print("This is a valid date")
    GetDate()
    
    
GetDate()

    




