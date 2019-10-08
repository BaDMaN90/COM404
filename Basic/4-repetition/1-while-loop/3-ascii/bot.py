batter = "█"
charge = 1
required_charge = int(input("how much charge do you require?\n> "))
while charge <= required_charge:
    print("charging:" + batter * charge)
    charge = charge + 1
print("batter is fully charged.")