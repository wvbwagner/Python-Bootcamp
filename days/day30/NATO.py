import pandas

phonetic = pandas.read_csv('nato_phonetic_alphabet.csv')

alpha = {row.letter:row.code for (index, row) in phonetic.iterrows()}
phonetic_code = []

'''ESTE FOI O CÓDIGO DA YU

def generate_code():
    user_entry = input("Enter a word: ").upper()

    try:
        phonetic_code = [alpha.get(letter) for letter in user_entry]
    except KeyError:
            print("sorry, only letters in the alphabet please")
            generate_code()
    else:
        print(phonetic_code)
'''

#ESTE FOI O CÓDIGO QUE FIZ E TBM FUNCIONOU
#TIVE QUE LANÇAR UMA KEYERROR PORQUE MEU CÓDIGO NÃO GERAVA ESSE ERRO
#SOMENTE PRINTAVA [NONE] PARA CADA NÚMERO OU SÍMBOLO


while True:
    try:
        user_entry = input("Enter a word: ").upper()
        for letter in user_entry:
            if not letter.isalpha():
                raise KeyError
    except KeyError:
        print("sorry, only letters in the alphabet please")
    else:
        phonetic_code = [alpha.get(letter) for letter in user_entry]
        break
print(phonetic_code)


