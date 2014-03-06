# Check password
# Author: Brian Hamburg

def main():
    password = input("Enter your password: ").strip()
   
    if isValid(password): 
        print("Valid Password")
    else:
        print("Invalid Password")
        
# Check validity
def isValid(password):
    # check length
    if len(password) < 8:
        return False
    else:
        # check number of digits
        numberOfDigits = 0
        for i in range(len(password)):
            if password[i].isdigit():
                numberOfDigits += 1
        if numberOfDigits < 2:
            return False
        else:
            # check alphanumeric
            numberOfNonchars = 0
            for i in range(len(password)):
                if password[i].isdigit() != 1 and password[i].isalpha() != True:
                    numberOfNonchars += 1
            if numberOfNonchars > 0:
                return False
            else:
                return True                    

main()
