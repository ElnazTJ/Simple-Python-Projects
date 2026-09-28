import random
import string

chars = list(string.punctuation + string.digits + string.ascii_letters + " ")
key = chars.copy()
random.shuffle(key)


def encrypt():
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {cipher_text}")


def decrypt():
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted message: {cipher_text}")
    print(f"Original message: {plain_text}")


def main():
    while True:
        user = input("Encrypt (1) or Decrypt (2)? ")

        if user == "1":
            encrypt()
        elif user == "2":
            decrypt()
        else:
            print("Please enter 1 or 2.")
            continue

        ask = input("Do you want to continue? (y/n): ").lower()

        if ask == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()