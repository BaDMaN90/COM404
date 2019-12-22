from random import randint
import math

def run_cipher(key_size):
    print("Alphabet:\n" + str(alphabet))
    for ay in range(0, key_size, 1):
        shifted_alphabet.append(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        letters =  []
        shift = randint(0, 26)
        for ax in range(0, shift, 1):
            letters.append(shifted_alphabet[ay][0])
            shifted_alphabet[ay].remove(letters[ax]) 
            shifted_alphabet[ay].append(letters[ax])
        print("\nShifted Alphabet #"+str(ay+1)+":  ("+ str(shift) + ")\n" + str(shifted_alphabet[ay]) )
        key.append(shift)
    print("\nKey:")

    for key_array in range(0, key_size, 1):
        print(str(key_map[int(key[key_array])]), end = "", sep = "")

    message = input("\n\nEnter your message to cipher\n>")
    message = message.lower()
    key_devision = int(math.ceil(len(message)/8))
    message_track = 0
    print("\n \nCiphered message: (char:" + str(len(message))+ ")\n")

    for ciphering in range(0, key_devision, 1):
        for cipher in range(0, key_size, 1):
            if message_track < len(message):
                if message[message_track] in alphabet:
                    print(shifted_alphabet[cipher][alphabet.index(message[message_track])], end = "", sep = "")
                elif message[message_track] in special: 
                    print(message[message_track], end = "")
            message_track += 1
    print("\n")

def run_decipher(key_size):
    key_input = input("\n\nEnter your unique Key\n>")
    print("Alphabet:\n" + str(alphabet))
    for decipher_y in range(0, key_size, 1):
        shift = 26 - key_map.index(key_input[decipher_y])
        shifted_alphabet.append(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        letters =  []
        for ax in range(0, shift, 1):
            letters.append(shifted_alphabet[decipher_y][0])
            shifted_alphabet[decipher_y].remove(letters[ax]) 
            shifted_alphabet[decipher_y].append(letters[ax])
        print("\nShifted Alphabet #"+str(decipher_y+1)+":  ("+ str(shift) + ")\n" + str(shifted_alphabet[decipher_y]) )

    message = input("\n\nEnter your message to decipher\n>")
    message = message.lower()
    key_devision = int(math.ceil(len(message)/8))
    message_track = 0
    print("\n \nDeciphered message: (char:" + str(len(message))+ ")\n")

    for deciphering in range(0, key_devision, 1):
        for decipher in range(0, key_size, 1):
            if message_track < len(message):
                if message[message_track] in alphabet:
                    print(shifted_alphabet[decipher][alphabet.index(message[message_track])], end = "", sep = "")
                elif message[message_track] in special: 
                    print(message[message_track], end = "")
            message_track += 1
  
    print("\n")

# This are main variable -------------------------------------------------------------------

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shifted_alphabet = [["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]
special = [" ", ",",".", "!", "?", ""]
key = []
key_size = 8
key_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "#", "@", "?", "!", "£", "$", "&"]
ciphered_message = ""

for x in range(0,10,1):
    print("\n")

print("Welcome to the shift cipher tool!\n")
option = input("What would you like to do? \n1)cipher  \n2)decipher\n\n>")
if option == "cipher" or option == "1":
    run_cipher(key_size)
elif option == "decipher" or option == "2":
    run_decipher(key_size)