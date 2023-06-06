import random

#Event date maker

# MM/DD/YYYY
#def MakeDate():
#    year = baseYear + RandomeIndex(5)
#    month = RandomeIndex(12)

#    if month == 2:
#        if year%4 == 0:
#            day = RandomeIndex(29)
#        else:
#            day = RandomeIndex(28)

#    elif month%2 == 0:
#        day = RandomeIndex(30)

#    else:
#        day = RandomeIndex(31)

#    #parse to String and Add Leading 0's
#    month = str(month)
#    if len(month) <2:
#        month = "0"+month

#    day = str(day)
#    if len(day)<2:
#        day = "0"+day
#    year = str(year)

#    date = month+"/"+day+"/"+year
#    return date

#YYYY/MM/DD
def MakeDate():
    year = 2018 + RandomeIndex(5)
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

    #parse to String and Add Leading 0's
    month = str(month)
    if len(month) <2:
        month = "0"+month

    day = str(day)
    if len(day)<2:
        day = "0"+day
    year = str(year)

    date = year + "/" + month +"/" + day
    return date

def RandomeIndex(max):
    return random.randrange(1,max+1)