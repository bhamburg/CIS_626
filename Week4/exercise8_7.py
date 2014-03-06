# Phone keypads
# Author: Brian Hamburg

def main():
    number = list(input("Enter a string: "))
   
    print(getNumber(number))
        
# Convert to a number
def getNumber(number):
    for i in range(len(number)):
        if number[i].isalpha():
            if number[i] == "a" or number[i] == "A" or number[i] == "b" or number[i] == "B" or number[i] == "c" or number[i] == "C":
                number[i] = str(2)
            elif number[i] == "d" or number[i] == "D" or number[i] == "e" or number[i] == "E" or number[i] == "f" or number[i] == "F":
                number[i] = str(3)
            elif number[i] == "g" or number[i] == "G" or number[i] == "h" or number[i] == "H" or number[i] == "i" or number[i] == "I":
                number[i] = str(4)
            elif number[i] == "j" or number[i] == "J" or number[i] == "k" or number[i] == "K" or number[i] == "l" or number[i] == "L":
                number[i] = str(5)
            elif number[i] == "m" or number[i] == "M" or number[i] == "n" or number[i] == "N" or number[i] == "o" or number[i] == "O":
                number[i] = str(6)
            elif number[i] == "p" or number[i] == "P" or number[i] == "q" or number[i] == "Q" or number[i] == "r" or number[i] == "R" or number[i] == "s" or number[i] == "S":
                number[i] = str(7)
            elif number[i] == "t" or number[i] == "T" or number[i] == "u" or number[i] == "U" or number[i] == "v" or number[i] == "V":
                number[i] = str(8)
            elif number[i] == "w" or number[i] == "W" or number[i] == "x" or number[i] == "X" or number[i] == "y" or number[i] == "Y" or number[i] == "z" or number[i] == "Z":
                number[i] = str(9)
    number = "".join(number)
    return number

main()
