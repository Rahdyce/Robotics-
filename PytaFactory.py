CS = 0
IL = 1
IR = 0
IC = 1
#############Front/Back Distance Block#############  int 0:999
FL = 999
FR = 45
BL = 00
BR = 58
#############Side Distance Blocks################ int 0:999
LL = 0
LR = 0
RL = 0
RR = 1

RT = 0


def data():
    dataString = "A-CS=" + str(CS) + "-IL=" + str(IL) + "-IR=" + str(IR) + "-IC=" + str(IC) + "-FL=" + str(FL) + "-FR=" + str(FR) + "-BL=" + str(BL) + "-BR=" + str(BR) + "-LL=" + str(LL) + "-LR=" + str(LR) + "-RL=" + str(RL) + "-RR=" + str(RR) + "-RT=" + str(RT) + "-Z"
    return dataString


def interpret(data):
    i = data.index("-")
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = data[i+1:]
    index = 0
    #print("init")
    #print(data)
    #print("____________________________")
    while len(data) > 2 and data.index("=") > 0:
        length = len(data)
        i = data.index("=")
        #print(i)
        j = data.index("-")
        #print(j)
        num[index] = int(data[i+1:j])
        data = data[j+1:]
        #print("num = ")
        #print(num[index])
        #print(data)
        index += 1
    CS = num[0]
    IL = num[1]
    IR = num[2]
    IC = num[3]
    FL = num[4]
    FR = num[5]
    BL = num[6]
    BR = num[7]
    LL = num[8]
    LR = num[9]
    RL = num[10]
    RR = num[11]
    RT = num[12]


    return num

def read(prompt):
    match prompt:
        case "CS":
            return CS
        case "IL":
            return IL
        case "IR":
            return IR
        case "IC":
            return IC
        case "FL":
            return FL
        case "FR":
            return FR
        case "BL":
            return BL
        case "BR":
            return BR
        case "LL":
            return LL
        case "LR":
            return LR
        case "RL":
            return RL
        case "RR":
            return RR
        case "RT":
            return RT
        case _:
            return 0

line = data()
#print(line)
length = interpret(line)
print(length)
