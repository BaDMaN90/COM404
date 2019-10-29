# Ask user for phrase
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...\nThe phrase is", end="")

reversed = ""

for letters in phrase:
    reversed = "" + reversed

print(reversed) 