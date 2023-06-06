
import random
import csv

#First name Pool 50
nameFirstMale = [
 "Liam"
,"Noah"
,"Oliver"
,"James"
,"Elijah"
,"William"
,"Henry"
,"Lucas"
,"Benjamin"
,"Theodore"
,"Mateo"
,"Levi"
,"Sebastian"
,"Daniel"
,"Jack"
,"Michael"
,"Alexander"
,"Owen"
,"Asher"
,"Samuel"
,"Ethan"
,"Leo"
,"Jackson"
,"Mason"
,"Ezra"
,"John"
,"Hudson"
,"Luca"
,"Aiden"
,"Joseph"
,"David"
,"Jacob"
,"Logan"
,"Luke"
,"Julian"
,"Gabriel"
,"Grayson"
,"Wyatt"
,"Matthew"
,"Maverick"
,"Dylan"
,"Isaac"
,"Elias"
,"Anthony"
,"Thomas"
,"Jayden"
,"Carter"
,"Santiago"
,"Ezekiel"
,"Charles"]

nameFirstFemale = ["Olivia"
,"Emma"
,"Charlotte"
,"Amelia"
,"Sophia"
,"Isabella"
,"Ava"
,"Mia"
,"Evelyn"
,"Luna"
,"Harper"
,"Camila"
,"Sofia"
,"Scarlett"
,"Elizabeth"
,"Eleanor"
,"Emily"
,"Chloe"
,"Mila"
,"Violet"
,"Penelope"
,"Gianna"
,"Aria"
,"Abigail"
,"Ella"
,"Avery"
,"Hazel"
,"Nora"
,"Layla"
,"Lily"
,"Aurora"
,"Nova"
,"Ellie"
,"Madison"
,"Grace"
,"Isla"
,"Willow"
,"Zoe"
,"Riley"
,"Stella"
,"Eliana"
,"Ivy"
,"Victoria"
,"Emilia"
,"Zoey"
,"Naomi"
,"Hannah"
,"Lucy"
,"Elena"
,"Lillian"]

#Last name Pool 20
nameLast = ["Smith"
,"Johnson"
,"Williams"
,"Brown"
,"Jones"
,"Garcia"
,"Miller"
,"David"
,"Rodriguez"
,"Martinez"
,"Hernandez"
,"Lopez"
,"Gonzalez"
,"Wilson"
,"Anderson"
,"Thomas"
,"Taylow"
,"Moore"
,"Jackson"
,"Martin"]

#Base Year for calculating
baseYear = 2018

#Table Column names
fNameColumn = "First_Name"
lNameColumn = "Last_Name"
dateBirthData = "DOB"
dateColumn = "Date"
SSNColumn = "SNN"

#Taple
tableName = "Test1"
tableHeader = []
tableData = []

def main():
    header = [fNameColumn, lNameColumn, dateBirthData, SSNColumn, dateColumn]
    tableData.append(header)

    for x in range(20):        
       dateData = MakeDate()      
       nameData = MakeName()
       SSNData = MakeSSN()
       BirthdayData = MakeAge()

       row = [nameData[0], nameData[1],  BirthdayData, SSNData, dateData]
       tableData.append(row)

    WrightToFile()
    #print(tableHeader)
    #print(tableData)
       

def MakeDate():
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


    return str(month)+"/"+str(day)+"/"+str(year)

def MakeName():
    male_female = RandomeIndex(2)
    index = RandomeIndex(49)
    name = []

    if male_female == 1:
        name.append(nameFirstMale[index])
    else:
        name.append(nameFirstFemale[index])      

    index = RandomeIndex(19)
    name.append(nameLast[index])

    return name

def MakeSSN():
    return str(RandomeIndex(999)) + "-" + str(RandomeIndex(99)) + "-" + str(RandomeIndex(9999))

def MakeAge():
    age = RandomeIndex(88)

    #Get Year
    if age == 5:
        year = baseYear
    elif age < 5:
        year = baseYear + (5-age)
    else:
        year = baseYear - (age - 5)
    
    #Get Month
    month = RandomeIndex(12)
    #Get Day

    if month ==2:

        if year%4 ==0:
            day = RandomeIndex(29)
        else:
            day = RandomeIndex(28)
    elif month%2 == 0:
        day = RandomeIndex(30)

    else:
        day = RandomeIndex(31)

    return str(month) + "/" + str(day) + "/" + str(year)

def WrightToFile():

    with open((tableName+".csv"), 'w', newline='') as file:
        writer = csv.writer(file)

        #writer.writerow(tableHeader)

        for x in tableData:
            writer.writerow(x)
    
        


def RandomeIndex(max):
    return random.randrange(1,max+1)



if __name__ == "__main__":
    main()