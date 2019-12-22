print("How many shadows must we defeat?")
shadow_no = int(input())

print("It's Turtle time...")
for shadow_no in range(shadow_no-1,0,-1):
    print("...kalabanga dude!")
    print("..."+str(shadow_no), "shadows to go.")
    shadow_no -=1

print("All the shadows have been defeated! Time to take on Shreddar!")