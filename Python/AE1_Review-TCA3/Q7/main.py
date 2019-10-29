from functions import ASCII_triangle, left_triangle, right_triangle

def program(five_digit_number, action):
    if action == "ASCII":
        ASCII_triangle(five_digit_number)
    elif action == "left":
        left_triangle(five_digit_number)
    elif action == "right":
        right_triangle(five_digit_number)
    else:
        print("Invalid input.")

print("Input five digit number:")
five_digit_number = str(input())
print("Please select the option of display: \'ASCII\' or \'left\' or \'right\'")
action = input()
program(five_digit_number, action)

