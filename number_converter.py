#number converter

#Convert negative numbers

#def toBase(base1, base2)
# for decimal to any base
    #1) create an option to print all conversions
    #2) loop your program
    #3) return the binary number in terms of bytes as well as bits (8bits = 1 Byte)
        #-- if the binary number exceeds a certain value, only return in bytes

#Begin decimal script

def realNumber(userNumber):  #checks if the user inputs a real number (this wont be valind for hexadecimal conversions)
    try:
        int(userNumber)
    except ValueError:
        print("Invalid Input")
        return False
    else:
        return True

def under10(num10,userBase):  #for any base less than base 10
    digitInBase = []   #used to append each digit derived from the base change
    numInBase = ""
    while num10 > 0:    
        digitInBase.append(num10 % userBase)
        num10 = num10 // userBase   #division withour floating point
    for j in range(0, len(digitInBase)):
        numInBase = numInBase + (str(digitInBase[(len(digitInBase)-1)-j]))  #digitInBase is appended backwards
    return(numInBase)

def beyond10(num10,userBase): #for bases greater than base 10
    digitInBase = []
    numInBase = ""
    letters = ["A","B","C","D","E","F"]
    while num10 > 0:
        if (num10 % userBase) < 10:
            digitInBase.append(num10 % userBase)
        elif (num10 % userBase) >= 10:
            digitInBase.append(letters[(num10 % userBase) - 10])   #appends the letter coresponding to the number quantity
        num10 = num10 // userBase
    for j in range(0, len(digitInBase)):
        numInBase = numInBase + (str(digitInBase[(len(digitInBase)-1)-j]))
    return(numInBase)

#End Decimal Scrypt

#Begin Binary script

#Binary to base conversion:
    #1) have a checkpoint to make sure the number is indeed a binary number
        # for each bit, check that it equals 0 or 1 (check that it is less than 2)
    #2) convert the binary number to octal, decimal, and hexadecimal
        # you will have to split the binary number into 3 or 4 bits for octal and hexadecimal. for a number with n bits, intermediate to the splits, add zeros to the end
        # until you get the desired amout of bits
    #3) give the user the option to define the type of number they are converting
    #4) chain the binary conversion with the decimal conversion, so the user can convert directly from decimal to binary to any other base


def binaryCheckpoint(userBinary):
    check = True
    for m in range(0, len(userBinary)): 
        if int(userBinary[m]) > 1:
            check = False
    if check == False:
        print("Invalid Input")
        return False
    else:
        return True

def binaryTo8(userBinary):
    to_8 = ""
    not_3 = "0"
    threeBits = ""
    threeBitInt = 0
    while len(userBinary) % 3 != 0:
        userBinary = not_3 + userBinary
    for k in range(0, len(userBinary)):    #Goal: split number into 3 bits, and perform binary to 10 converson, then add strings
        threeBits = threeBits + userBinary[k]
        if (k + 1) % 3 == 0:
            for m in range(0,len(threeBits)):
                threeBitInt = threeBitInt + (int(threeBits[m]) * 2**((len(threeBits) - 1) - m))
            threeBits = ""
            to_8 = to_8 + str(threeBitInt)
        threeBitInt = 0
    return to_8

def binaryTo16(userBinary):
    to_16 = ""
    not_4 = "0"
    fourBits = ""
    fourBitInt = 0
    letters = ["A","B","C","D","E","F"]
    while len(userBinary) % 4 != 0:
        userBinary = not_4 + userBinary
    for k in range(0, len(userBinary)):    #Goal: split number into 4 bits, and perform binary to hexadecimal converson, then add strings
        fourBits = fourBits + userBinary[k]
        if (k + 1) % 4 == 0:
            for m in range(0,len(fourBits)):
                fourBitInt = fourBitInt + (int(fourBits[m]) * 2**((len(fourBits) - 1) - m))
            if fourBitInt > 9:
                to_16 = to_16 + letters[fourBitInt - 10]
            else:
                to_16 = to_16 + str(fourBitInt)
            fourBits = ""
        fourBitInt = 0
    return to_16
    
def binaryTo10(userBinary):
    to_10 = 0
    for k in range(0, len(userBinary)):
        power = int(userBinary[(len(userBinary)-1)-k]) * 2**k #bits is a string, convert to integer
        to_10 = to_10 + power #appending as such assignes each bit to the index of its corresponding power 2^n
        
    #take eack number and multiply it by 2^(index)
    return(str(to_10))  #"to_10" is not converted to a string in this function

#Ask user for the base of the number they are converting


while True:  # this loop allows the user to rerun the program
    print("What is the base of your number you are converting?: ")
    print("1) Decimal")
    print("2) Binary")
    numBaseInput = input("Enter your choice by corresponding number: ")
    while numBaseInput != "1" and numBaseInput != "2":
        print("Invalid Input")
        numBaseInput = input("Enter your choice by corresponding number: ")

    #Begin decimal computations
        
    if numBaseInput == "1":
        print("You have chosen Decimal")
        while True:
            decimal = input("Enter your number: ")
            if realNumber(decimal) == True:
                break

        decimal = int(decimal)
        print("Which base do you want to convert this number to?: ")
        print("1) Binary")
        print("2) Octal")
        print("3) Hexadecimal")
        print("4) All of the above")
        baseChoice = input("Enter your choice: ")

        while True:   #option select
            if baseChoice == "1":
                base = 2
                print(under10(decimal,base))
                break
            elif baseChoice == "2":
                base = 8
                print(under10(decimal,base))
                break
            elif baseChoice == "3":
                base = 16
                print(beyond10(decimal,base))
                break
            elif baseChoice == "4":
                base = 2
                print("Binary: " + under10(decimal,base))
                base = 8
                print("Octal: " + under10(decimal,base))
                base = 16
                print("Hexadecimal: " + beyond10(decimal,base))
                break
            else:
                print("Invalid Option")
                print("Which base do you want to convert this number to?: ")
                print("1) Binary")
                print("2) Octal")
                print("3) Hexidecimal")
                baseChoice = input("Enter your choice: ")

    #End Decimal Computation

    #Begine Binary Computations
    if numBaseInput == "2":
        print("You have chosen Binary")
        while True:
            binary = input("Enter your binary number: ")
            if realNumber(binary) == False:   #will print "invalid input"
                continue
            elif binaryCheckpoint(binary) == True: #checks if the user input is a binary number
                break

        print("Which base would you like to convert to?: ")
        print("1) Decimal")
        print("2) Octal")
        print("3) Hexadecimal")
        print("4) All of the above")
        binaryBaseChoice = input("Enter your choice: ")

        while True:
            if binaryBaseChoice == "1":
                print(binaryTo10(binary))
                break
            elif binaryBaseChoice == "2":
                print(binaryTo8(binary))
                break
            elif binaryBaseChoice == "3":
                print(binaryTo16(binary))
                break
            elif binaryBaseChoice == "4":
                print("Decimal: " + binaryTo10(binary))
                print("Octal: " + binaryTo8(binary))
                print("Hexadecimal: " + binaryTo16(binary))
                break
            else:
                print("Invalid Input")
                print("Which base would you like to convert to?: ")
                print("1) Decimal")
                print("2) Octal")
                print("3) Hexadecimal")
                print("4) All of the above")
                binaryBaseChoice = input("Enter your choice: ")

    #End binary computation

    computeAgain = input("Compute another number? (y/n): ")
    while computeAgain.lower() != "y" and computeAgain.lower() != "n":
        print("Invalid Input")
        computeAgain = input("Compute another number? (y/n): ")
    if computeAgain.lower() == "n":
        print("-------------------")
        print("End of program")
        print("-------------------")
        break
    elif computeAgain.lower() == "y":
        print("-------------------")
        print("Restarting Program")
        print("-------------------")
        continue
