
def check_password(phrase):
    password = "meow123"

    #==========================
    # Update the code below so that if the phrase and password are the same, return True.
    # Otherwise, return False

    if password:
        return True

    #
    #==========================


def main():
    attempt = input("Please enter your password: ")
    while True:
        if check_password(attempt):
            print("Password is correct!")
            break
        else:
            attempt = input("Password is false! Try again: ")
    print("Objective complete :)")

main()