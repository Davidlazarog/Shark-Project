def fatality(x):
    if x == "Y":
        return True
    elif x == "N":
        return False
    elif x == " N":
        return False
    elif x == "N ":
        return False
    elif x == "y":
        return True
    return 'Unknown'

def Type(x):
    if x == "Unprovoked":
        return 'Unprovoked'
    elif x == "Provoked":
        return 'Provoked'
    elif x == "Sea Disaster":
        return 'Unprovoked' 
    return 'Unknown'

import re
arms = ["(.*)?arms(.*)?", "(.*)?hand(.*)?" ]
leg = ["(.*)leg(.*)?", "(.*)?foot(.*)?" ]
fatal = ["(.*)?atal(.*)?", "(.*)?ody(.*)?" ]
ribs = ["(.*)?ribs(.*)?"]
noinjury = ["(.*)?o injur(.*)?"]

def menu (x) :
    Arms = "ARMS"
    Leg = 'LEGS'
    Fatal = 'FATAL'
    Ribs = 'RIBS'
    Noinjury = 'NO INJURY'
    x = x.lower()
    if type(x) != str:
        return 'Unknown'
    else:
        for a in arms:
            if re.search (a,x):
                x = Arms
                return x
        for l in leg:
            if re.search (l,x):
                x = Leg
                return x
        for i in fatal:
            if re.search (i,x):
                x = Fatal
                return x 
        for r in ribs:
            if re.search (r,x):
                x = Ribs
                return x
        for n in noinjury:
            if re.search (n,x):
                x = Noinjury
                return x
        return 'Unknown'

pizza = ["(.*)?no injury(.*)?" ]
human = ["(.*)?fatal(.*)?", "(.*)?legs(.*)?", "(.*)?arms(.*)?", "(.*)?ribs(.*)?"]

def pizzavshuman (x):
    Pizza = 'PIZZA'
    Human = 'HUMAN'
    x = x.lower()
    for p in pizza:
        if re.search (p,x):
            x = Pizza
            return x
    for h in human:
        if re.search (h,x):
            x = Human
            return x
    return 'UNKNOWN'