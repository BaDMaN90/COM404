def cipher_tool():
    shift = int(input("what shift of letter do you want to apply? choose from 1 to 26\n"))
    run_tool(shift)

def decipher_tool():
    shift = 26 - int(input("what shift of letter was applied? choose from 1 to 26\n"))
    run_tool(shift)

def run_tool(shift):
    letters =  []
    ciphered_message = ""

    for remove in range(0, shift, 1):
        letters.append(shifted_alphabet[0])
        shifted_alphabet.remove(letters[remove]) 
        shifted_alphabet.append(letters[remove])
    print("Alphabet:\n" + str(alphabet) + "\nShifted Alphabet: \n" + str(shifted_alphabet) )

    if option == "cipher" or option == "1":
        message = input("\nEnter your message to cipher\n>")
        print("\n \nCiphered message:")
    elif option == "decipher" or option == "2":
        message = input("\nEnter your message to decipher\n>")
        print("\n \nDeciphered message:")
    message = message.lower()

    for cipher in range(0, len(message),1):
        if message[cipher] in alphabet:
            print(shifted_alphabet[alphabet.index(message[cipher])], end = "", sep = "")
        elif message[cipher] in special:
            print(message[cipher], end = "")
    print("\n")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shifted_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
special = [" ", ",",".", "!", "?", ""]

for x in range(0,10,1):
    print("\n")

print("Welcome to the shift cipher tool!\n")
option = input("What would you like to do? \n1)cipher  \n2)decipher\n\n>")
if option == "cipher" or option == "1":
    cipher_tool()
elif option == "decipher" or option == "2":
    decipher_tool()