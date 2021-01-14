class BookCipher:
    global file
    def __init__(self, path):
        global file
        file = open(path)
        self.__loadfile()

    global rawText
    def __loadfile(self):
        global text
        global rawText
        text = file.read()
        rawText=text
        text = text.split(" ")

    def __characterFinder(self,index):
        return text[index - 1][0:1]


    def __characterGrabber(index):
        return text[index]


    def doBookCipher(self,cipher):
        firstDecryption = []
        print("Book Cipher Errors:")
        for i in range(len(cipher)):
            # Grab the first letter of each word at the array index
            try:
                character = self.__characterFinder(cipher[i])
                if (character is "&"):
                    character = "a"
                firstDecryption.append(character.lower())
                #print(ord(character.lower())-97, end="\n")
            except Exception as e:
                firstDecryption.append("_")
                print("\t",end="")
                print(e, end="")
                print(" | at index ", end="")
                print(i)

        print("-")
        for i in firstDecryption:
            print(i, end="")
        print()
        #this is the array
        return firstDecryption