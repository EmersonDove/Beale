class Vigenere:
    global key
    def __init__(self,decryptKey):
        global key
        key=decryptKey

    def decrypt(self,text):
        global key
        output = ""
        currentKeyIndex = 0
        for i in range(len(text)):
            output += chr(((ord(text[i].lower()))-(ord(key[currentKeyIndex].lower()))) % 26 + 97)
            currentKeyIndex += 1
            if currentKeyIndex is len(key):
                currentKeyIndex = 0
        return output