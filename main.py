import sys
from encrypt import encrypt
from decrypt import decrypt

def menu():
    print("===================================")
    print("Welcome to the Encryptor/Decryptor!")
    print("===================================")
    print("\n")
    print("Please choose an option:")
    print("\n")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        print("Goodbye!")
        sys.exit()
        
    else:
        print("Invalid choice")
        menu()


if __name__ == '__main__':
    menu()