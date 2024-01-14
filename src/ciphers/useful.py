import re
import itertools
from resources.useful import string_to_square_matrix as make_matrix

def hard_divide(a:int, b:int, round_up:bool=True):
    hard_result = 0 
    hard_result += a // b
    if a % b > 0 and round_up:
        hard_result += 1
    return int(hard_result)

def space_by(text:str, interval:int):
    num_of_blocks = hard_divide(len(text),interval, False)
    blocks = []
    for i in range(0,num_of_blocks*5,interval):
        blocks.append(text[i:i+interval])
    return " ".join(blocks)

def filter(text, spaces:bool=True, punctuation:bool=True, nums:bool=True, case:bool=True):
    if spaces:
        text = re.sub(r"\s+", "", text)
    if punctuation:
        text = re.sub("[^A-Za-z0-9 ]+","", text)
    if nums:
        text = re.sub(r"[\d+]","",text)
    if case:
        text = text.upper()
    return text

def generate_all_grids(size:int, alphabet:str):
    all_alphabets = list(itertools.permutations([char for char in alphabet], size**2))
    return [make_matrix(alphabet, size) for alphabet in all_alphabets]

def generate_deranged_alphabet(keyword:str,alphabet:str):
    keyword,alphabet = keyword.upper(),alphabet.upper()
    
    deranged_alphabet = ""
    for char in keyword:
        if char not in deranged_alphabet:
            deranged_alphabet += char

    starting_indx = alphabet.index(keyword[-1])
    for i in range(starting_indx,starting_indx+len(alphabet)):
        if alphabet[i%len(alphabet)] not in deranged_alphabet:
            deranged_alphabet += alphabet[i%len(alphabet)]

    return deranged_alphabet