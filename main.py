
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(cipher_direction, start_text, shift_amount):
    shift_amount = shift_amount % 26
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    if cipher_direction == "encode" or cipher_direction == "decode" and shift_amount % 1 == 0:
        for char in start_text:
            if char in alphabet:
                index = alphabet.index(char)
                index += shift_amount
                end_text += alphabet[index]
            else:
                end_text += char
        print("The {0}d text is {1}".format(cipher_direction, end_text))
    else:
        print("Please enter a valid instruction.")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
    answer = input("Type 'yes' if you want to go again. Else type 'no'.\n")
    if answer == 'no':
        should_continue = False
        print("Good Bye")


# def encrypt(plain_text, shift_amount):
#     cipher_text =""
#     for letter in plain_text:
#         index = alphabet.index(letter)
#         index += shift_amount
#         new_letter = alphabet[index]
#         cipher_text += new_letter
#     print("The encoded text is {}".format(cipher_text))
#
# def decrypt(cipher_text, shift_amount):
#     plain_text =""
#     for letter in cipher_text:
#         index = alphabet.index(letter)
#         index -= shift_amount
#         new_letter = alphabet[index]
#         plain_text += new_letter
#     print("The decoded text is {}".format(plain_text))
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Please enter a valid instruction.")
