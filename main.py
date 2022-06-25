import STAT as stat
import EV as ev

def computation_type(data):

    print("please input (1) for Status or (2) EV  calculation")
    opt = int(input())

    if(opt == 1):
        STAT (data)

    elif(opt == 2):
        EV (data)
    else:
        print("Invalid input") 

def STAT (stat_data): 
   
    total_hp = stat.compute.hp(stat_data)
    print("The total hp is: ")
    print(total_hp)

   
    other_stat = stat.compute.other_stat(stat_data)
    print("The other stat: ")
    print(other_stat)
    option(stat_data)


def EV (stat_data): 
    
    print("please enter your desired stat increase")    
    stat = int(input())
    stat_data["stat"] = stat

    eve_needed = EV.compute.ev_needed(stat_data)
    print("The ev needed: ")
    print(eve_needed)
    option(stat_data)

def start():

    print("input base hp")
    base = int(input())

    flag = 1
    while flag == 1:
        print("input the IV between 0-31")
        iv = int(input())
        if(iv >= 0 and iv <= 31):
            flag = 2


    flag2 = 1
    while flag2 == 1:
        print("input the EV between 0-255")
        ev = int(input())
        if(ev >= 0 and ev <= 255):
            flag2 = 2

    print("input level: ")
    level = int(input())


    print("selec nature: input (1) Benificial or (2) Hindering ")
    natureInput = int(input())

    if natureInput == 1:
        nature = 1.1
    elif natureInput == 2:
        nature = 0.9
    else: 
        nature = 1.1


    stat_data = {
        "base": base,
        "iv": iv,
        "ev": ev,
        "level": level,
        "nature": nature
    }

    computation_type(stat_data)


def option(data): 
    print("1. To choose other computation")
    print("2. To start again")

    x = int(input())

    if( x == 1): 
        computation_type(data)
    elif( x == 2):
        start()
    else:
        start()


start()