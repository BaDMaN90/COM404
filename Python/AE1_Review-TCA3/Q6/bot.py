def isFusionShot(slug_one, slug_two):
    if slug_one == slug_two:
        return True
    else:
        return False

def isDefectiveShot(slug_one, slug_two):
    if isFusionShot(slug_one, slug_two) is True:
        print("It is not a defective shot.")
        return
    elif slug_one == "Infurnus" and slug_two == "AquaBeek" or slug_one == "AquaBeek" and slug_two == "Infurnus":
        return True
    else:
        return False

# Run the program
def run():
    slug_one = input("select the type of first slug\n")
    slug_two = input("select the type of second slug\n")
    fusion_or_defective = input("\'fusion\' or \'defective\'.\n")

    if fusion_or_defective == "fusion":
        isFusionShot(slug_one, slug_two)
        if isFusionShot(slug_one, slug_two) is True:
            print("The fusion was succesful.")
        else:
            print("The fusion was not succesful.")
    elif fusion_or_defective == "defective":
        isDefectiveShot(slug_one, slug_two)
        if isFusionShot(slug_one, slug_two) is True:
            return
        elif isDefectiveShot(slug_one, slug_two) is True:
            print("The defective shot was succesful.")
        else:
            print("The defective shot was not succesful.")
    else:
        print("Invalid input.")
run()
#Slug types "Infurnus", "AquaBeek"