#this function will take 2 parameters to identify the pokemon name and ablity
def identify_specie(pokemon_name, pokemon_ability):
    #if ablity if fire then is will print that it is a fire type and return boolen value True
    if pokemon_ability == "Fire" or pokemon_ability == "fire":
        print(pokemon_name,"is a Fire Pokemon")
        return True
    #otherwise it will say that the pokemon is cool
    else:
        print(pokemon_name,"is a cool Pokemon")

#
def can_catch(pokemon_name, pokemon_ability):
    if identify_specie(pokemon_name,pokemon_ability) is True:
        print("Can be caught!")
    else:
        print("this pokemon is too cool to catch")

def run():
    pokemon_name = input("What is the name of the Pokemon\n")
    pokemon_ability = input("What is the ablility of the Pokemon\n")
    action = input("What action would you like to perform? \'identify\' or \'catch\'\n")
    if action == "identify":
        identify_specie(pokemon_name, pokemon_ability)
    elif action == "catch":
        can_catch(pokemon_name, pokemon_ability)
    else:
        print("Invalid input.")

#run the program
run()