bop = "bop "
input_string = input("Please enter a phrase: ")
count = 0

for c in input_string:
    if c.isspace() != True:
        count = count + 1
print(bop * count)