import random



#First name Pool's 50
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

def MakePerson():
     
    person = []
    gender = RandomeIndex(2)
  
    if gender == 1:
        person.append(nameFirstMale[RandomeIndex(50) - 1])
    else:
        person.append(nameFirstFemale[RandomeIndex(50) - 1])

    person.append(nameLast[RandomeIndex(20) - 1])

    person.append(MakeSNN())
    
    #print(person[0] + " " +person[1] + ": "+ person[2])

    return person

def MakeSNN():
    return str(RandomeIndex(999)) + "-" + str(RandomeIndex(99)) + "-" + str(RandomeIndex(9999))

def RandomeIndex(max):
    return random.randrange(1,max+1)