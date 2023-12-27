alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

def caesar(plain_text,plain_shift,plain_direction):
    encoded_text = ""
    while plain_shift > 26:
        plain_shift -= 26
    if plain_direction == "decode":
        plain_shift *= -1
    for i in plain_text:
        if ord(i) < 97 or ord(i) > 122:
            encoded_text += i
        elif ord(i) + plain_shift > 122:
            new_char = chr(ord(i) + plain_shift - 26)
            encoded_text += new_char
        else:
            new_char = chr(ord(i) + plain_shift)
            encoded_text += new_char
    print(encoded_text)

print(logo)

cont = True
while cont == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    restart = input("Would you like to restart the program? Type 'yes' or 'no'.\n")
    if restart == 'no':
        cont = False
