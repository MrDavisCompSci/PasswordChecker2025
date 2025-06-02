# -------------------------------------------------------------------
# Username generator
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------

def checkPpassword(passwordToCheck):

    # Add your code here
    
    return False


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
password = input("Enter a password to check: ")

while checkPassword(password) == False:
    print("Password does not meet requirements")
    password = input("Enter a password to check: ")

print("Password is OK")
