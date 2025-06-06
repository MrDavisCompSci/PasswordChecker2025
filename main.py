# -------------------------------------------------------------------
# Password checker
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------

def checkPassword(passwordToCheck):

    # Add your code here
    # length check
    if len(passwordToCheck) < 8:
        return False
    
    # capital letter check
    capitalFound = False
    index = 0
    while not capitalFound and index < len(passwordToCheck):
        if passwordToCheck[index].isupper():
            capitalFound = True
        index = index + 1 # OR index += 1
    
    if not capitalFound:
        return False

    # lower case check
    

    return True


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
password = input("Enter a password to check: ")

while checkPassword(password) == False:
    print("Password does not meet requirements")
    password = input("Enter a password to check: ")

print("Password is OK")
