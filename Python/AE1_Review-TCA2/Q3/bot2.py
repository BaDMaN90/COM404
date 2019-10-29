#program teakes user input of the whole number
no_of_zones = int(input("How many zones must I cross?\n"))
print("Crossing zones...")
#for loop will run until no_of_zones is equal to 0
for zones in range(no_of_zones,0,-1):
    #this will print "...crossed zone and number of zones left"
    print("...crossed zone",no_of_zones)
    #this will deduct 1 each time it loops through this commant
print("Crossed all zones. Jumanji!")