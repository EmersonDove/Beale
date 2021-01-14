#Just include this file to convert between the two datatypes. Converting from string to array just adds one character to each array index

def arrayToString(s):
    new = ""
    for x in s:
        new += str(x)
    return new

def stringToArray(s):
    returnArray = []
    for i in range(len(s)):
        returnArray.append(s[i])
    return returnArray