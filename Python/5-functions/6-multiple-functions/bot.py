def display_ladder(steps):
    if steps >= 1:
        while steps != 0:
            print("| |")
            print("***")
            steps -= 1
    print("| |")
display_ladder(5)
    
