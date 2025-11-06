# Create a Python program that can encode text into Morse code and decode Morse code back into text. 
# The program will use a dictionary to map letters, numbers, and basic punctuation to their Morse code equivalents.

morse_code_dict = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
}

def encode_to_morse(text):
    """Encode text to morse code."""
    encoded_message = ""
    text = input("Enter text to encode to morse code: ")
    for char in text.upper():
        if char == " ":
            encoded_message += " "
        elif char in morse_code_dict:
            encoded_message += morse_code_dict[char] + " "
    return encoded_message
    
def lookup_key_by_value(value):
    """Helper function to lookup dictionary key by its value."""
    for key, val in morse_code_dict.items():
        if val == value:
            return key
    return ""

def decode_from_morse(morse_code):
    """Decode morse code to text."""
    decoded_message = ""
    morse_code = input("Enter morse code to decode: ")
    morse_words = morse_code.split("   ")
    for morse_word in morse_words:
        morse_chars = morse_word.split(" ")
        for morse_char in morse_chars:
            decoded_message += lookup_key_by_value(morse_char)
        decoded_message += " "
    return decoded_message.strip()


if __name__ == "__main__":
    choice = input("Type 'e' to encode or 'd' to decode: ").lower()
    if choice == 'e':
        print("Encoded Morse Code:", encode_to_morse(""))
    elif choice == 'd':
        print("Decoded Text:", decode_from_morse(""))
    else:
        print("Invalid, type 'e' or 'd'.")