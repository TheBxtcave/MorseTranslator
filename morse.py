import os

def english_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    }
    morse_code = []
    for char in text.upper():
        if char == ' ':
            morse_code.append(' ')
        elif char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(' ')
    return ' '.join(morse_code)


def morse_to_english(morse_code):
    reverse_morse_dict = {value: key for key, value in morse_code_dict.items()}
    morse_words = morse_code.split(' ')
    english_text = []
    for word in morse_words:
        if word == '':
            english_text.append(' ')
        elif word in reverse_morse_dict:
            english_text.append(reverse_morse_dict[word])
    return ''.join(english_text)


# Dictionary to map characters to their respective Morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}


def clear_terminal():
    # Clear terminal screen using ANSI escape codes
    print("\033c", end='')

def display_menu():
    menu = """ Welcome to   
  __  __                    ___         _     
 |  \/  |___ _ _ ___ ___   / __|___  __| |___ 
 | |\/| / _ \ '_(_-</ -_) | (__/ _ \/ _` / -_)
 |_|  |_\___/_| /__/\___|  \___\___/\__,_\___|
                                              
1. Translate English to Morse code
2. Translate Morse code to English
3. Exit
"""
    print(menu)

def main():
    while True:
        clear_terminal()  # Clear the terminal at the start of each loop
        display_menu()

        choice = input()

        if choice == '1':
            english_text = input("Enter the English text to translate to Morse code: ")
            morse_code = english_to_morse(english_text)
            print("Morse code:", morse_code)
            input("Press Enter to continue...")

        elif choice == '2':
            morse_code = input("Enter the Morse code to translate to English: ")
            english_text = morse_to_english(morse_code)
            print("English text:", english_text)
            input("Press Enter to continue...")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
