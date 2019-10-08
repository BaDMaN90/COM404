number = int(input("Please enter a number? "))
factorial = 1

while number !=0:
    factorial = factorial * number
    number = number - 1
print("the factorial is ", factorial)