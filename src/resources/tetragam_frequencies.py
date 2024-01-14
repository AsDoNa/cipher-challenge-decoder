import re
from resources.progress_bar import update_progress
from resources.useful import construct_dict as dict_from_file
# from progress_bar import update_progress
# from useful import construct_dict as dict_from_file
import os
from math import log

MID_SEP = ":"
END_SEP = ","
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MIN_VALUE = 1/4745366

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

    for key in frequencies.keys():
        frequencies[key] /= num_tets

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

def convert_frequencies_to_log(freqs:list):
    '''Calculates the log of the tetragram frequencies in a list and returns them'''
    # total_freq = sum([int(freq) for freq in freqs])
    log_freqs = []

    for freq in freqs:
        # log_freq = log(max(freq, 1e-10),total_freq)
        log_freq = log(max(float(freq), MIN_VALUE))
        log_freqs.append(log_freq)

    return log_freqs

def calc_log_frequencies_from_file(directory:str,file:str,save:bool=False,save_directory:str="",save_file:str=""):
    '''returns or saves the table of logarithms of frequencies of tetragrams from a file of tetragram frequencies'''
    with open(os.path.join(directory,file), "r") as f:
        tetra_dict = dict_from_file(f.read(),MID_SEP,END_SEP)
        tetra_log_dict = {}
        log_freqs = convert_frequencies_to_log(tetra_dict.values())
        for i, key in enumerate(tetra_dict.keys()):
            tetra_log_dict[key] = log_freqs[i]

    if save:
        with open(os.path.join(save_directory,save_file), "w") as f:
            for i, key in enumerate(tetra_log_dict.keys()):
                if i < len(tetra_log_dict.keys()) - 1:
                    f.write(f"{key}{MID_SEP}{tetra_log_dict[key]}{END_SEP}")
                else:
                    f.write(f"{key}{MID_SEP}{tetra_log_dict[key]}")

    else:
        return tetra_log_dict
        

if __name__ == "__main__":
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "alphabet"))
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "frequency"))
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "alphabet", include_spaces=True))
    # print(count_tetragrams_file("src/resources", "engcorp.txt", "frequency", include_spaces=True))
    # count_tetragrams_file("src/resources", "engcorp.txt", "alphabet", save=True, save_dir="src/resources", save_file="engcorptetfreqs.txt")
    # count_tetragrams_file("src/resources", "engcorp.txt", "alphabet", include_spaces=True, save=True, save_dir="src/resources", save_file="engcorpspacetetfreqs.txt")
    calc_log_frequencies_from_file("src/resources", "engcorptetfreqs.txt",True,"src/resources","engcorptetlogfreqs.txt")
    calc_log_frequencies_from_file("src/resources", "engcorpspacetetfreqs.txt",True,"src/resources","engcorpspacetetlogfreqs.txt")
    pass