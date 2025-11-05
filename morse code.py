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
    for char in text.upper():
        if char in morse_code_dict.keys():
            encoded_message +=(morse_code_dict[char])
            encoded_message +=(" ")
        elif char == " ":
            encoded_message+=("   ")
    return encoded_message
    
def lookup_key_by_value(value):
    for key, val in morse_code_dict.items():
        if val == value:
            return key
    return ""

def decode_from_morse(morse_code):
    """Decode morse code to text."""
    decoded_message = ""
    for code in morse_code.split(" "):
        if code == "":
            decoded_message += " "
        else:
            decoded_message += lookup_key_by_value(code)
    return decoded_message
    #accepting something like ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
    #split that input on the space
    #split takes a string and converts it to an array based on a separator. 
    #eg "hello world".split(" ") would be ["hello", "world"]

if __name__ == "__main__":
    text = "HELLO WORLD"
    morse_code = encode_to_morse(text)
    print(f"Encoded: {morse_code}")

    decoded_text = decode_from_morse(morse_code)
    print(f"Decoded: {decoded_text}")
