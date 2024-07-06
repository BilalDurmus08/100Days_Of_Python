alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print(len(alphabet))


def cript(text1, shift1, type1):
    if type1 == "encode":
        encrypted_message = ""
        print(text1)
        for value in range(0, len(text1)):
            index = alphabet.index(text1[value])
            index += shift1
            index = index % 26
            encrypted_message += alphabet[index]

        print(encrypted_message)

    else:
        encrypted_message = ""
        for value in range(0, len(text1)):
            index = alphabet.index(text1[value])
            shift1 = shift1 % 26
            index -= shift1
            if index < 0:
                index = 26 + index
            encrypted_message += alphabet[index]

        print(encrypted_message)

    process = input("Do you wanna continue 'Y' or 'N' ")
    if process == 'Y':
        direction2 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text2 = input("Type your message:\n").lower()
        shift2 = int(input("Type the shift number:\n"))
        cript(text2, shift2, direction2)
    else:
        print("Bye bye")


cript(text, shift, direction)
