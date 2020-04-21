def list_ten():
    #================
    #   Write a function that will print numbers from 1 to 10
    #   Tip: you will need the 'range(start, end, step)' function, where the arguements will be 'range(1, 11)
    for x in range(1, 11):
        print(x)
    #=============

def count_by_three():
    #================
    #   Write a function that will print numbers from 3 - 30, counting by threes
    for x in range(3, 33, 3):
        print(x)
    #=============

def main():
    list_ten()
    print('')
    count_by_three()
    print("Objective complete :)")

main()