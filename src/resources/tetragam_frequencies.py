import re
from progress_bar import update_progress
import os
from math import log

MID_SEP = ":"
END_SEP = ","
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def possible_tetragrams(dict_or_list:str, alphabet:str=ALPHABET):
    if dict_or_list == "dict":
        tetragrams = {}
    if dict_or_list == "list":
        tetragrams = []

    print("GENERATING TETRAGRAMS")
    print()

    total_combs = len(alphabet)**4
    i = 0
    for char1 in alphabet:
            for char2 in alphabet:
                for char3 in alphabet:
                    for char4 in alphabet:
                        i += 1
                        tetra = f'{char1}{char2}{char3}{char4}'
                        update_progress(i,total_combs)
                        if "  " in tetra:
                            continue
                        
                        if dict_or_list == "dict":
                            tetragrams[tetra] = 0
                        if dict_or_list == "list":
                            tetragrams.append(tetra)

    return tetragrams

    

def count_tetragrams(text:str, order_by_alphabet_or_frequency:str="alphabet", case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False):
    '''Returns a dictionary of all tetragrams in the text (filtered according to args) ordered by alphabet or frequency'''

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

    frequencies = possible_tetragrams("dict",alphabet)
    num_tets = len(text)-3

    print("COUNTING TETRAGRAMS")
    print()

    for i in range(num_tets):
        frequencies[text[i:i+4]] += 1
        update_progress(i,num_tets)

    if order_by_alphabet_or_frequency == "alphabet":
        frequencies = dict(sorted(frequencies.items(), key=lambda x:x[0].replace(" ", "_")))
    if order_by_alphabet_or_frequency == "frequency":
        frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1], reverse=True))
            
    return frequencies

def count_tetragrams_file(directory:str, file:str, order_by_alphabet_or_frequency:str="alphabet", case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False, save:bool=False, save_dir:str="", save_file:str=""):
    '''returns or saves the tetragram frequencies from the words in a file'''

    with open(os.path.join(directory,file), "r") as f:
        tetragram_dict = count_tetragrams(f.read(), order_by_alphabet_or_frequency, case_insensitive, include_spaces, include_nums, include_punc)
    
    if save:
        with open(os.path.join(save_dir, save_file), "w") as f:
            for i, key in enumerate(tetragram_dict.keys()):
                if i < len(tetragram_dict.keys()) - 1:
                    f.write(f"{key}{MID_SEP}{tetragram_dict[key]}{END_SEP}")
                else:
                    f.write(f"{key}{MID_SEP}{tetragram_dict[key]}")
    else:
        return tetragram_dict

def convert_frequency_to_log(freq:int, total_freq:int):
    freq = max(freq, 1e-10)


if __name__ == "__main__":
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "alphabet"))
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "frequency"))
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "alphabet", include_spaces=True))
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "frequency", include_spaces=True))
    count_tetragrams_file("src/resources", "engcorp.txt", "alphabet", save=True, save_dir="src/resources", save_file="engcorptetfreqs.txt")
    count_tetragrams_file("src/resources", "engcorp.txt", "alphabet", include_spaces=True, save=True, save_dir="src/resources", save_file="engcorpspacetetfreqs.txt")