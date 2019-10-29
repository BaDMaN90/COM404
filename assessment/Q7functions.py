#file function have 4 functions that will do a cool print play

#this function will print piramids on the left of the face
def left(emoji):
    print("/\/\/\\",emoji)

#this function will print piramids on the right of the face
def right(emoji):
    print(emoji,"/\/\/\\")

#this function will print face between piramids
def both(emoji):
    print("/\/\/\\",emoji,"/\/\/\\")

#this function will creat the grid of faces betweein piramids
#size of the grid will depend on the deifined size by the user
def grid(emoji,grid_size):
    #2 loops will helo to create a nice grid
    #first loop will define the height of the grid f.e. grid_size = 3 means that loop will creat 3 rows
    #second loop will print the correct patternt in the raw
    for x in range(grid_size):
        for operator in range(-1,grid_size):
            if operator <= -1 or operator == grid_size-1:
                print("/\/\/\\ ", end ="")
                if operator != grid_size-1:
                    print(emoji,"", end='')
                operator +=1
            else:
                print("/\/\/\/\/\\",emoji,"", end ="")
                operator +=1
        print("")

