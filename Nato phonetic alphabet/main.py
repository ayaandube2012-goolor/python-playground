import pandas
def nato_phonetic_alphabet():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    user_word = input("give me a word: ").upper()
    try:
        natofised_word = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Please type letters only")
        nato_phonetic_alphabet()
    else:
        print(natofised_word)
nato_phonetic_alphabet()
