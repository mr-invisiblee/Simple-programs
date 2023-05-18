import base64

def encode_base64(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def decode_base64(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

def text_to_morsecode(text):
    morsecode_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
                      '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                      ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
                      '$': '...-..-', '@': '.--.-.', ' ': '/'}
    morsecode = []
    for char in text.upper():
        if char == ' ':
            morsecode.append(' ')
        elif char in morsecode_dict:
            morsecode.append(morsecode_dict[char])
    return ' '.join(morsecode)

def morsecode_to_text(morsecode):
    morsecode_dict = {' ': '/', '@': '.--.-.', '$': '...-..-', '"': '.-..-.', '_': '..--.-', '-': '-....-', '+': '.-.-.', '=': '-...-', ';': '-.-.-.', ':': '---...', '&': '.-...', ')': '-.--.-', '(': '-.--.', '/': '-..-.', '!': '-.-.--', "'": '.----.', '?': '..--..', ',': '--..--', '.': '.-.-.-', '9': '----.', '8': '---..', '7': '--...', '6': '-....', '5': '.....', '4': '....-', '3': '...--', '2': '..---', '1': '.----', '0': '-----', 'Z': '--..', 'Y': '-.--', 'X': '-..-', 'W': '.--', 'V': '...-', 'U': '..-', 'T': '-', 'S': '...', 'R': '.-.', 'Q': '--.-', 'P': '.--.', 'O': '---', 'N': '-.', 'M': '--', 'L': '.-..', 'K': '-.-', 'J': '.---', 'I': '..', 'H': '....', 'G': '--.', 'F': '..-.', 'E': '.', 'D': '-..', 'C': '-.-.', 'B': '-...', 'A': '.-'}
    text = []
    words = morsecode.split(' / ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in morsecode_dict:
                text.append(morsecode_dict[letter])
        text.append(' ')
    return ''.join(text)

while True:
    print("Options:")
    print("1. Encode using Base64")
    print("2. Decode using Base64")
    print("3. Convert text to Morse code")
    print("4. Convert Morse code to text")
    print("5. Special Encode")
    print("6. Special Decode")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        text = input("Enter the text to encode: ")
        encoded_text = encode_base64(text)
        print("Encoded text:", encoded_text)

    elif choice == '2':
        encoded_text = input("Enter the text to decode: ")
        decoded_text = decode_base64(encoded_text)
        print("Decoded text:", decoded_text)

    elif choice == '3':
        text = input("Enter the text to convert to Morse code: ")
        morsecode = text_to_morsecode(text)
        print("Morse code:", morsecode)

    elif choice == '4':
        morsecode = input("Enter the Morse code to convert to text: ")
        text = morsecode_to_text(morsecode)
        print("Text:", text)

    elif choice == '5':
        text = input("Enter the text to coded morsecode: ")
        encoded_text = encode_base64(text)
        morsecode = text_to_morsecode(encoded_text)
        print("Encoded text:", morsecode)
        
        
    elif choice == '6':
        morsecode = input("Enter the coded morsecode to decode: ")
        morsede_text = morsecode_to_text(morsecode)
        decoded_text = decode_base64(morsede_text)
        print("Decoded text:", decoded_text)


    elif choice == '7':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 7.")
