import re
from progress_bar import update_progress
import os

MID_SEP = ":"
END_SEP = ","
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def possible_monograms(dict_or_list:str, alphabet:str=ALPHABET):
    if dict_or_list == "dict":
        monograms = dict([(char,0) for char in alphabet])
    if dict_or_list == "list":
        monograms = [char for char in alphabet]

    return monograms

def count_monograms(text:str, order_by_alphabet_or_frequency:str="alphabet", case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False):
    '''Returns a dictionary of all monograms in the text (filtered according to args) ordered by alphabet or frequency'''

    alphabet = ALPHABET
    if include_spaces:
        alphabet += " "
    
    text = re.sub("\n", " ", text)
    
    if case_insensitive:
        text = text.upper()

    if not include_punc:
        text = re.sub("[^A-Za-z0-9 ]+", "", text)
    
    if not include_nums:
        text = re.sub("[^A-Za-z ]+", "", text)
    
    if not include_spaces:
        text = re.sub(" ", "", text)

    text = re.sub(r"\s+", " ", text)

    frequencies = possible_monograms("dict", alphabet)
    num_chars = len(text)
    i = 0

    print("COUNTING MONOGRAMS")
    print()

    for char in text:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
        i += 1
        update_progress(i,num_chars)

    if order_by_alphabet_or_frequency == "alphabet":
        frequencies = dict(sorted(frequencies.items(), key=lambda x:x[0].replace(" ", "_")))
    if order_by_alphabet_or_frequency == "frequency":
        frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1], reverse=True))
            
    return frequencies

def count_monograms_file(directory:str, file:str, order_by_alphabet_or_frequency:str="alphabet", case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False, save:bool=False, save_dir:str="", save_file:str=""):
    '''returns or saves the monogram frequencies from the words in a file'''

    with open(os.path.join(directory,file), "r") as f:
        monogram_dict = count_monograms(f.read(), order_by_alphabet_or_frequency, case_insensitive, include_spaces, include_nums, include_punc)
    
    if save:
        with open(os.path.join(save_dir, save_file), "w") as f:
            for i, key in enumerate(monogram_dict.keys()):
                if i < len(monogram_dict.keys()) - 1:
                    f.write(f"{key}{MID_SEP}{monogram_dict[key]}{END_SEP}")
                else:
                    f.write(f"{key}{MID_SEP}{monogram_dict[key]}")
    else:
        return monogram_dict
    
def load_monogram_count(directory:str,file:str, mid_sep:str=MID_SEP, end_sep:str=END_SEP):
    '''Loads from a file the monogram dictionary generated and saved by count_monograms_file'''
    with open(os.path.join(directory,file), "r") as f:
        monogram_dict = {}
        monogram_dict_array = f.read().split(end_sep)
        for monogram_freq in monogram_dict_array:
            if len(monogram_freq) != 0:
                monogram,freq = monogram_freq.split(mid_sep)
                monogram_dict[monogram] = freq
    
    return monogram_dict

if __name__ == "__main__":
    count_monograms_file("src/resources", "engcorp.txt", save=True, save_dir="src/resources", save_file="engcorpmonofreqs.txt")
    count_monograms_file("src/resources", "engcorp.txt", include_spaces=True, save=True, save_dir="src/resources", save_file="engcorpspacemonofreqs.txt")
    # print(load_monogram_count("src/resources", "engcorpspacemonofreqs.txt"))