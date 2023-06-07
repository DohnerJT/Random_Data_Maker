import random
import datetime

#Month formats
monthString = [
    ["Jan","January"],
    ["Feb","February"],
    ["Mar","March"],
    ["Apr","April"],
    ["May","May"],
    ["June","June"],
    ["July","July"],
    ["Aug","August"],
    ["Sept","September"],
    ["Oct","October"],
    ["Nov","November"],
    ["Dec","December"],
    ]

#Base Year for calculating
baseYear = 2018


def MakeDate(format):
    #Create Year Month Day values
    year = baseYear + RandomeIndex(5)    

    month = RandomeIndex(12)

    if month == 2:
        if year%4 == 0:
            day = RandomeIndex(29)
        else:
            day = RandomeIndex(28)
    elif month%2 == 0:
        day = RandomeIndex(30)
    else:
        day = RandomeIndex(31)

    #Format the Values

    yearFormated = FormatYear(format[0], year)
    monthFormated = FormatMonth(format[2:], month)
    dayFormated = FormatDay(format[2], day)
    dateFormated = FormatDate(format[1]+format[4], monthFormated, dayFormated, yearFormated)
    
    #print(dateFormated)

    return dateFormated

def MakeAge(format):
    age = RandomeIndex(85)
    today = datetime.date.today()

    #Create Year Month Day values
    year = today.year - age    


    month = RandomeIndex(12)

    if month == 2:
        if year%4 == 0:
            day = RandomeIndex(29)
        else:
            day = RandomeIndex(28)
    elif month%2 == 0:
        day = RandomeIndex(30)
    else:
        day = RandomeIndex(31)

    #Format the Values

    yearFormated = FormatYear(format[0], year)
    monthFormated = FormatMonth(format[2:], month)
    dayFormated = FormatDay(format[2], day)
    dateFormated = FormatDate(format[1]+format[4], monthFormated, dayFormated, yearFormated)
    
    #print("age: " + str(age) + " Year: " + str(year))

    return dateFormated

def FormatYear(f,y):

    y = str(y)
    if f == "+":
        return y
    else:        
        return y[2:]

def FormatMonth(f,m):

    if(f[1] == "1"):
        m=str(m)
        if f[0] == "+" and len(m)<2:
            return "0"+m
        else:
            return m
    elif f[1] == "2":
        return monthString[m-1][0]
    else:
        return monthString[m-1][1]
  
def FormatDay(f,d):

    d = str(d)

    if f == "+" and len(d)<2:
        return "0"+d
    else:
        return d
   
def FormatDate(f, m, d, y):

    match f[0]:
        #M D Y
        case "1":
            #delimit
            if f[1] == "+":
                if len(m) > 2:
                    return m + " " + d + ", " + y
                else: 
                    return m + "/" + d + "/" + y
            else:
                return m+d+y
                 
        #D M Y
        case "2":
            if f[1] == "+":
                if len(m) > 2:
                    return d + " " + m + ", " + y
                else:
                    return d + "/" + m + "/" + y
            else:
                return d+m+y
        #Y M D
        case "3":
            if f[1] == "+":
                if len(m) > 2:
                    return y + ", " + m + " " + d
                else:
                    return y + "/" + m + "/" + d
            else:
                return y+m+d
       

def RandomeIndex(max):
    return random.randrange(1,max+1)