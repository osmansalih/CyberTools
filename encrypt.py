def encrypt():
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the key: "))

    letters = {
        "A": "[A]", "B": "[AA]", "C": "[AAA]", "D": "[B]", "E": "[BB]", "F": "[BBB]",
        "G": "[C]", "H": "[CC]", "I": "[CCC]", "J": "[D]", "K": "[DD]", "L": "[DDD]",
        "M": "[E]", "N": "[EE]", "O": "[EEE]", "P": "[F]", "Q": "[FF]", "R": "[FFF]",
        "S": "[G]", "T": "[GG]", "U": "[GGG]", "V": "[H]", "W": "[HH]", "X": "[HHH]",
        "Y": "[I]", "Z": "[II]"
    }

    message = message.upper()

    encrypted_message = ""

    for char in message:
        if char in letters:
            encrypted_message += letters[char]
        else:
            encrypted_message += char

    print("Encrypted message:", encrypted_message)




if __name__ == "__main__":
    encrypt()
