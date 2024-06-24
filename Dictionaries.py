# Define the NATO phonetic alphabet dictionary
nato_alphabet = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
}
def spell_word(word):
    for letter in word:
        upper_letter = letter.upper()
        if upper_letter in nato_alphabet:
            print(nato_alphabet[upper_letter])
        else:
            print(f"'{letter}' is not a valid letter in the English alphabet")

def main():
    word = input("Please enter a word: ")
    spell_word(word)

if __name__ == "__main__":
    main()
