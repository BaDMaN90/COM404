#prints a message
print("You have 0 Avengers. Assembling...")

#sets variable number_of_avengers to 0 which will be called out in the loop and at the end of program
number_of_avengers = 0

#loop will run 5 times and request response of the user
#depend on the response it will add, subtrack or do nothing to the variable number_of_avengers
for avengers in range(5):
    question = input("...Do we have an Avenger?\n")
    if question == "yes":
        print("An Avenger has been assembled.")
        number_of_avengers +=1

    elif question =="No. A fake":
        print("We had an imposter in our midst.")
        number_of_avengers -=1
    else:
        print("Better find a nother.")

#this will print the number_of_avengers variable final value followed by a rest of the print
print(number_of_avengers,"Avengers have been assembled.")