# vigenere cipher

def check_option(choice):
    if choice == "encrypt":
        return 1
    elif choice == "decrypt":
        return -1
    else:
        return check_option(input("Invalid option! Please select 'encode' or 'decode': ").lower())


def caesar_cipher(secret, key, cipher_option):
    cipher_note = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    for char in secret.lower():
        if not char.isalpha():
            cipher_note += char
        else:
            key_char = key[index % len(key)]
            key_index = alphabet.find(key_char) * cipher_option
            char_index = alphabet.find(char)
            cipher_char = alphabet[(char_index + key_index) % 26]
            cipher_note += cipher_char
            index += 1
    return convert_upper(cipher_note, secret)


def convert_upper(coded_message, initial_message):
    coded_message, initial_message = list(coded_message), list(initial_message)
    for index in range(len(initial_message)):
        if initial_message[index].isupper():
            coded_message[index] = coded_message[index].upper()

    return "".join(coded_message)


option = check_option(input("Would you like to 'encrypt' or 'decrypt' ").lower())
message = input(f"Enter the secret message you wish to encrypt/decrypt: ")
cipher_key = input("Please enter a cipher key: ")
cipher_message = caesar_cipher(message, cipher_key, option)
print(cipher_message)
