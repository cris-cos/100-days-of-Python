alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cripted = ""
    for letter in text:
        if letter not in alphabet:
            cripted += letter
        else:
            position = alphabet.index(letter)
            if position + shift > len(alphabet) - 1:
                shifted_position = (position + (shift%len(alphabet))) - len(alphabet)
                cripted += alphabet[shifted_position]
            else:
                shifted_position = position + shift
                cripted += alphabet[shifted_position]
    print(f"the encrypted text is {cripted}")

def decrypt(text, shift):
    decripted = ""
    for letter in text:
        if letter not in alphabet:
            decripted += letter
        else:
            position = alphabet.index(letter)
            if position - shift < 0:
                shifted_position = (position - (shift%len(alphabet)))
                decripted += alphabet[shifted_position]
            else:
                shifted_position = position - shift
                decripted += alphabet[shifted_position]
    print(f"the original text was {decripted}")
    
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)