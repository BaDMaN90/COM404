#funtion visit have 1 variable "ghost"
def visit(ghost):
    #decision of output depends on the function visit call
    if ghost == "Ghost of Christmas Past":
        print("Humbug! I care not for these days of past celebration.")
    elif ghost == "Ghost of Christmas Present":
        print("Humbug! I care not for their suffering.")
    elif ghost == "Ghost of Christmas Future":
        print("Please no more. I will change my ways.")

#calling the function visit with different string input
visit("Ghost of Christmas Past") 
visit("Ghost of Christmas Present") 
visit("Ghost of Christmas Future")
