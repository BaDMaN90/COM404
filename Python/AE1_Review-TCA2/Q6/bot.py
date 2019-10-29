# this program will help Batman to unite the league

# this function is checking if the league is united or not
def is_league_united(hero_one, hero_two):
    if hero_one == "Superman" and hero_two == "Wonder Woman":
        print("League is united.")
        run()
    else:
        print("League is not united.")
        run()

# this function is checking with the function is_league_united,  
# then printing the response
def decide_plan(hero_one, hero_two):
    is_league_united(hero_one, hero_two)
    if  hero_one == "Superman" and hero_two == "Wonder Woman":
        print("Time to save the world!")
    else:
        print("We must unite the league!")

# This is main function which ask for 3 inputs
# depend on action choosen it will execute different function
def run():
    hero_one = input("what is the name of first hero?\n")
    hero_two = input("what is the name of second hero?\n")
    action = input("what action should i take?\n")
    if action == "league":
        is_league_united(hero_one,hero_two)
    elif action == "plan":
        decide_plan(hero_one,hero_two)
    else:
        print("Invalid command. Please try again.")
        run()

# This will call the function run
run()
