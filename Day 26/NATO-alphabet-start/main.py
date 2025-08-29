import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:

nato_dict = {value.iloc[0]:value.iloc[1] for (key,value) in nato_df.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word - ").upper()
#
output_list = [nato_dict[letter] for letter in word]
print(output_list)

phonetic_keys = {letter: nato_dict[letter] for letter in word}
print(phonetic_keys)
