print("Welcome to the Planet of the Apes... ")
human_no = 0
ape_no = 0
event_no = 7

for episode in range(event_no):
    human_or_ape = input("...be ye human or be ye ape?")

    if human_or_ape == "human":
        print("I did not start this war. But I will finish it.")
        human_no +=1
    elif human_or_ape == "ape":
        print("Apes together strong!")
        ape_no +=1
    else:
        print("You should choose your side quick")

print("Total humans encountered:", human_no)
print("Total apes encountered:", ape_no)