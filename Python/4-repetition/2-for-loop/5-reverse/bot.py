print("What phrase do you see?")
phrase = input()
reversed_phrase = ""
print("Reversing...")
len_phrase = len(phrase)
for x in range(0,len_phrase,1):
    reversed_phrase = reversed_phrase + (phrase[len(phrase)-x-1])
print("The phrase is: ", reversed_phrase)
