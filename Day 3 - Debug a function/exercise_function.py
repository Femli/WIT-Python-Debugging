def get_factors(number):
    number_list = []
    # ==== MEDIUM
    # How do you include the input number itself in the list? for example, 16 is also a factor of 16. code currently doesn't include it
    for num in range(number):
        if num < 1:
            continue
        if number % num == 0:
            number_list.append(num)
    return number_list

def main():
    # ==== EASY
    # input() by default returns a string. how can we make it an integer?

    # HARD
    # How will you handle numbers that are 0 or less?

    number = input("Please enter a number: ")
    factors = get_factors(number)
    print("The factors for {} are:".format(number))
    for numbers in factors:
        print(numbers)
main()
