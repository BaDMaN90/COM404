def ASCII_triangle(five_digit_number):
    for x in range(1,11,1):
        if x == 9:
            print("*",str(five_digit_number),"*")
            x +=1
        else:
            print("*" * x)
            x +=1

def left_triangle(five_digit_number):
    for y in range(0,len(five_digit_number)+1,1):
        print(str(five_digit_number[1,y]))
        y+=1

def right_triangle(five_digit_number):
    print("five_digit_number + five_digit_number")