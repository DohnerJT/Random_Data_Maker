
import random
import csv

import DateMake
import PersonMaker


#Date formating Veriables

# a: 4 digit or 2 digit Year
# + = YYYY
# - = YY
a = "+"

# b: Date value order 
# 1 = M D Y
# 2 = D M Y
# 3 = Y M D 
b = "3"

# c: leding or no neding 0's
# + = Leading 0's
# - + no Leading 0's
c = "+"

# d: number, Abreveated, or full month name
# 1 = MM
# 2 = Mon
# 3 = Month
d = "2"

# e: Dilimited or not
# + = Dilimited "/", ",", " "
# - = no Dilimiting
e = "+"

dateFormat = a+b+c+d+e #(a)(b)(c)(d)

#Table Column names
fNameColumn = "First_Name"
lNameColumn = "Last_Name"
dateBirthData = "DOB"
dateColumn = "Date"
SSNColumn = "SNN"

#Taple
rowCount = 20 #Number of iterations of data
tableName = "Test_A" #File Name
tableData = []

def main():
    #Table Header Column Names
    header = [fNameColumn, lNameColumn, SSNColumn, dateBirthData,  dateColumn]
    tableData.append(header)

    #Creates Data
    for x in range(rowCount):        
       dateData = DateMake.MakeDate(dateFormat)    
       BirthdayData = DateMake.MakeAge(dateFormat)
       personData = PersonMaker.MakePerson()
       
       row = [personData[0], personData[1], personData[2], BirthdayData, dateData]
       #print(personData[0] + " " +personData[1] + ": "+ personData[2])     
       tableData.append(row)

    WrightToFile()
    
    #for x in tableData:
    #     print(x)
          

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