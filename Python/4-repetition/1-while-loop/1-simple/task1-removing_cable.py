import time
print("Oh no, you are tangle up in these cables :(, how many cables are you wrpped in?")
no_cables = int(input())

while no_cables !=0:
    print("cable removed...")
    no_cables = no_cables - 1
    time.sleep(1)
print("job done :)")