import pandas

# Read from a file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create dictionary
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    user_input = input("Insert a word: ").upper()
    try:
        # Create list of phonetic code words from a user input
        phonetic_list = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only English letters are eligible")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()