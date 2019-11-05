def under(word):
    print(word)
    print(len(word) * "*")

def over(word):
    print(len(word) * "*")
    print(word)

def both(word):
    print(len(word) * "*")
    print(word)
    print(len(word) * "*")

def grid(word,grid_size):
    x = grid_size
    y = grid_size
    for grid in range(x,0,-1):
        if grid == grid_size:
            for a in range(y,0,-1):
                print(len(word) * "*","  ", end ="")
            print("")

        for a in range(y,0,-1):
            if a <= 1:
                print(word, end ="")
            else:
                print(word ,"| ", end ="")
        print("")

        for a in range(y,0,-1):
            print(len(word) * "*","  ", end ="")
        print("")

