import re
# from resources.progress_bar import update_progress
from progress_bar import update_progress
import os

MID_SEP = ":"
END_SEP = ","
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def possible_bigrams(dict_or_list:str, alphabet:str=ALPHABET):
    if dict_or_list == "dict":
        bigrams = {}
        monograms = [char for char in alphabet]
        for monogram1 in monograms:
            for monogram2 in monograms:
                bigrams["".join([monogram1,monogram2])] = 0
    if dict_or_list == "list":
        bigrams = []
        monograms = [char for char in alphabet]
        for monogram1 in monograms:
            for monogram2 in monograms:
                bigrams += "".join([monogram1,monogram2])

    return bigrams

def count_bigrams(text:str, order_by_alphabet_or_frequency:str="alphabet", case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False, percent_or_count:str="percent"):
    '''Returns a dictionary of all bigram probabilties in the text (filtered according to args) ordered by alphabet or frequency'''

    alphabet = ALPHABET
    if include_spaces:
        alphabet += " "
    
    text = "".join([char for char in text if char in alphabet])

    text = re.sub(r"\s+", " ", text)

    newText = ""
    for char in text:
        if char not in " ":
            newText += char

    print(newText)

    frequencies = possible_bigrams("dict", alphabet)
    num_chars = len(text)
    i = 0

    print("COUNTING BIGRAMS")
    print()

    for i in range(0,num_chars,2):
        if text[i:i+2] not in frequencies:
            print(text[i:i+2])
            frequencies[text[i:i+2]] = 1
        else:
            frequencies[text[i:i+2]] += 1
        # update_progress(i,num_chars)

    if percent_or_count == "percent":
        for key in frequencies.keys():
            frequencies[key] /= num_chars
    elif percent_or_count == "count":
        pass
    else:
        raise ValueError

    if order_by_alphabet_or_frequency == "alphabet":
        frequencies = dict(sorted(frequencies.items(), key=lambda x:x[0].replace(" ", "_")))
    if order_by_alphabet_or_frequency == "frequency":
        frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1], reverse=True))
            
    return frequencies

def count_bigrams_file(directory:str, file:str, order_by_alphabet_or_frequency:str="alphabet", case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False, save:bool=False, save_dir:str="", save_file:str=""):
    '''returns or saves the bigram frequencies from the words in a file'''

    with open(os.path.join(directory,file), "r") as f:
        bigram_dict = count_bigrams(f.read(), order_by_alphabet_or_frequency, case_insensitive, include_spaces, include_nums, include_punc)
    
    if save:
        with open(os.path.join(save_dir, save_file), "w") as f:
            for i, key in enumerate(bigram_dict.keys()):
                if i < len(bigram_dict.keys()) - 1:
                    f.write(f"{key}{MID_SEP}{bigram_dict[key]}{END_SEP}")
                else:
                    f.write(f"{key}{MID_SEP}{bigram_dict[key]}")
    else:
        return bigram_dict
    
def load_bigram_count(directory:str,file:str, mid_sep:str=MID_SEP, end_sep:str=END_SEP):
    '''Loads from a file the monogram dictionary generated and saved by count_monograms_file'''
    with open(os.path.join(directory,file), "r") as f:
        bigram_dict = {}
        bigram_dict_array = f.read().split(end_sep)
        for bigram_freq in bigram_dict_array:
            if len(bigram_freq) != 0:
                monogram,freq = bigram_freq.split(mid_sep)
                bigram_dict[monogram] = freq
    
    return bigram_dict

if __name__ == "__main__":
    # count_bigrams_file("src/resources", "engcorp.txt", save=True, save_dir="src/resources", save_file="engcorpbifreqs.txt")
    # count_bigrams_file("src/resources", "engcorp.txt", include_spaces=True, save=True, save_dir="src/resources", save_file="engcorpspacebifreqs.txt")
    # print(load_bigram_count("src/resources", "engcorpspacebifreqs.txt"))
    pass