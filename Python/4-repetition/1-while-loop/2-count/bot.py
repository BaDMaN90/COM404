#-- importing the time will allow the time delay in the code
#-- progtram will print out the message and ask for input
#-- 2 variables are created to run in the while loop to count down the avoided live cables and count up how many have avoided
import time
print("Oh no, you are tangle up in these cables :(, how many live cables are you wrpped in?")
no_cables = int(input())
live_cable = 1

#-- while loop will run as long as no_cables are different then 0
while no_cables !=0:
    print("Avoiding...")
    no_cables = no_cables - 1
    time.sleep(1)
    print(str(live_cable) + " live cable avoided")
    live_cable = live_cable + 1
    time.sleep(1)
print("All live cable avoided")