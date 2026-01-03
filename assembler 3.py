letters = "abcdef"
commands = ["ADD", "MUL", "LDR", "STR"]

def decToBinary(num):
    if num == 0 : 
        return ""
    else :
        if num % 2 == 1 :
            return decToBinary(num//2) + "1"
        else :
            return decToBinary(num//2) + "0"
        
def binaryToDec(num):
    adder = 1
    ret = 0
    for i in range(len(num)-1,-1,-1):
        if num[i] == "1":
            ret += adder
        adder*=2
    return ret

def binaryToHex16bit(num):
    ret = ""
    for i in range(4):
        temp = binaryToDec(num[i*4:(i+1)*4])
        if(temp < 10):
            ret += str(temp)
        else:
            ret += letters[temp-10]
    return ret
        
def decToBinaryTwoBit(num):
    if num == 0:
        return "00"
    elif num < 2:
        return "0" + decToBinary(num)
    else:
        return decToBinary(num)

def ADD(values):
    ret = "00011"
    ret += decToBinaryTwoBit(int(values[1][1:]))
    ret += decToBinaryTwoBit(int(values[2][1:]))
    ret += decToBinaryTwoBit(int(values[3][1:]))
    ret += "00000"
    return ret
def MUL(values):
    ret = "00010"
    ret += decToBinaryTwoBit(int(values[1][1:]))
    ret += decToBinaryTwoBit(int(values[2][1:]))
    ret += decToBinaryTwoBit(int(values[3][1:]))
    ret += "00000"
    return ret
def LDR(values):
    ret = "10110"
    ret += decToBinaryTwoBit(int(values[1][1:]))
    ret += decToBinaryTwoBit(int(values[2][1:]))
    temp = decToBinaryTwoBit(int(values[3]))
    if((len(ret)+len(temp))<16):
        ret += (16-(len(ret)+len(temp)))*"0"
    ret += temp
    return ret
def STR(values):
    ret = "01000"
    ret += decToBinaryTwoBit(int(values[1][1:]))
    ret += decToBinaryTwoBit(int(values[2][1:]))
    temp = decToBinaryTwoBit(int(values[3]))
    if((len(ret)+len(temp))<16):
        ret += (16-(len(ret)+len(temp)))*"0"
    ret += temp
    return ret

with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(0, len(lines)):
    lines[i] = lines[i].strip()

file.close()

machineCode = []
for line in lines:
    values = line.split(", ")
    if values[0] == "ADD":
        machineCode += [ADD(values)]
    elif values[0] == "MUL":
        machineCode += [MUL(values)]
    elif values[0] == "LDR":
        machineCode += [LDR(values)]
    elif values[0] == "STR":
        machineCode += [STR(values)]

hexMachineCode = []
for line in machineCode:
    hexMachineCode += [binaryToHex16bit(line)]

writing = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
flag = False
for i in range(0,16):
    if(i < 10):
        writing[i] += str(i)
    else:
        writing[i] += letters[i-10]
    writing[i] += "0: "
    if(flag):
        writing[i] += "0000 " * 15 + "0000"
        continue
    for j in range(0,16):
        if(hexMachineCode[i*16+j:] == []):
            flag = True
            writing[i] += "0000"
        else:
            writing[i] += hexMachineCode[i*16+j]
        if i != 15:
            writing[i] += " "
        

outputFile = open("image", "w")
outputFile.write("v3.0 hex words addressed\n")
for line in writing:
    outputFile.write(line)
    outputFile.write("\n")
outputFile.close()