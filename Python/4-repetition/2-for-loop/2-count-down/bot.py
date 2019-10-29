steps = int(input("How far are we from the cave? "))
for x in range(steps):
    if steps >= 2:
        print(steps ," steps remaining")
        steps = steps - 1
    elif steps == 1:
        print(steps ," step remaining")
        steps = steps - 1
print("We have reached the cave!")