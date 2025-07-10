#TODO 1. Create a dictionary in this format:
import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict={new_data["letter"]:new_data["code"] for (index,new_data) in data.iterrows()}
print(new_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("enter a word :").upper()
the_last=[new_dict[letters] for letters in word]
print(the_last)