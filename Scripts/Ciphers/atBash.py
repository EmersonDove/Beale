def performAtbash(input):
    output = ""
    for i in input:
        if (ord(i) >= 97 and ord(i) <= 122):
            output += chr((26 - (ord(i) - 97)) + 96)
        else:
            output += i
    return output