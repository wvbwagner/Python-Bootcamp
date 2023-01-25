import pandas

phonetic = pandas.read_csv('nato_phonetic_alphabet.csv')

alpha = {row.letter:row.code for (index, row) in phonetic.iterrows()}
user_entry = input("Enter a word: ").upper()
phonetic_code = [alpha.get(letter) for letter in user_entry]
print(phonetic_code)

