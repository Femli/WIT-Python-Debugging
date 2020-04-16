def area_of_square(length, height):
    return length * height

def area_of_triangle(base, height):
    return 0.5 * base * height

def convert_hours_to_mins(hours):
    return hours * 60


def main():
    square_length = 7
    square_height = 7
    square_area = area_of_square(square_length, square_height)
    print(square_area)

    triangle_base = 10
    triangle_height = 15
    triangle_area = area_of_triangle(triangle_base, triangle_height)
    print(triangle_area)

    hours = 39.6
    mins = convert_hours_to_mins(hours)
    print(mins)

    if square_area == 49 and triangle_area == 75 and mins == 2376:
        print("Objective complete! :)")

main()