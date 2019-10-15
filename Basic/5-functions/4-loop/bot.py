def no_steps(steps):
    if steps >= 5:
        for x in range(4):
            print("Crossed step")
            steps -= 1
        print("The bridge is collapsing!")
    while steps != 0:
        print("Crossed step")
        steps -= 1
    print("We must keep going!")
no_steps(10)