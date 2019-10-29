print("How many numbers should I sum up?")
no_of_cal = int(input())
number = 0
operator = 0
no_of_sum = no_of_cal


while no_of_cal !=0:
    print("Please enter number ", operator + 1, "of ", no_of_sum)
    no_of_cal = no_of_cal - 1
    operator = operator + 1
    num_to_add = int(input())
    number = number + num_to_add
print("your total sum of ", no_of_sum, "numbers is: ", number)