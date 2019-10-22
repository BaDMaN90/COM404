#Health of the Gene value
health = 100
#health value had to be converted to string to be printed next to % sign
print("Your health is", str(health) +"%. Escape is in progress...")
#for loop will run 5 times
for Gene in range(5):
    print("…Oh dear, who is that?")
    response = input()
    #depends on response it will deducts 20% of health, add 20 health or print the message
    if response == "Smiler's Bot":
        health = health - (health*0.2)
        print("Time to jam out of here.")
    elif response == "Hacker":
        health = health + 20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")
        
#to display health as a whole number it had to be re-converted to integer
health = int(health)
print("Escaped! Health is", str(health) + "%.")