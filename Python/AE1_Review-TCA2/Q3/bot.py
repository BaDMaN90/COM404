#program teakes user input of the whole number
no_of_zones = int(input("How many zones must I cross?\n"))
print("Crossing zones...")
#while loop will run until no_of_zones is different to 0
while no_of_zones != 0:
    #this will print "...crossed zone and number of zones left"
    print("...crossed zone",no_of_zones)
    #this will deduct 1 each time it loops through this commant
    no_of_zones -= 1
print("Crossed all zones. Jumanji!")
