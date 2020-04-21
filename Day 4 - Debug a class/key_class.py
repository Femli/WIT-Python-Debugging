class myshoplist():

    def __init__(self):
        self.list = []
        self.size = 0

    def add_items(self, item):
        #================
        # MEDIUM
        # How do we add items to the list? Hint: It's a single line of code. Google 'list methods' and find the right method to add, or 'append', items to the list.
        if item not in self.list:
            self.list.append(item)
            print("Item added.")
        else:
            print("Item is already in list.")

    def del_item(self, item):
        #================
        # MEDIUM
        # How do we remove items from the list? Hint: It's a single line of code. Google 'list methods' and find the right method to remove items.
        if item in self.list:
            self.list.remove(item)
            print("Item removed.")
        else:
            print("Item is not in list.")
    
    def list_summary(self):
        #================
        # HARD
        # How can we make this function: 1) print the amount of items we have, and 2) print each item we have in the list?
        self.size = len(self.list)
        print("Your shopping list has {} items.".format(self.size))
        print("Here are the list items:")
        for item in self.list:
            print(item)

def main():
    mylist = myshoplist()
    choice = 0
    print("Now that you are shopping, what would you like to do? Please select an option from below: ")
    #==================
    # MEDIUM
    # How can we get these options to print each time we make a new choice?
    while True:
        print("1 - Add items to list")
        print("2 - Remove items from list")
        print("3 - View list")
        print("4 - Done shopping")
        #================
        # EASY
        # The user needs to enter their choice. Note that the choice should be an integer. How can you do this? Start by creating a variable called 'choice'.
        choice = int(input())
        if choice in [1, 2, 3, 4]:
            if choice == 1:
                item = input("Please state item that add to your list: ")
                mylist.add_items(item)
            elif choice == 2:
                item = input("Please state item you want to remove from your list: ")
                mylist.del_item(item)
            elif choice == 3:
                mylist.list_summary()
            elif choice == 4:
                #===============
                # EASY
                # If the user is done shopping, we need to end the program. How do we get out of this while loop?
                print("Have a good day!")
                break
        else:
            print("Invalid option. Please try again")
        print("")
        print("Anything else?")

main()




    