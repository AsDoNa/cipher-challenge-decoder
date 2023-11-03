from src.resources.monogram_frequencies import load_monogram_count,count_monograms
from src.resources.tetragam_frequencies import count_tetragrams
from src.resources.chi_squared import chi_squared
from src.resources.useful import cos_angle_between_vectors, construct_dict
import os
import re

MID_SEP = ":"
END_SEP = ","
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_monograms_chi_squared(text:str, mono_directory:str,mono_file:str, case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False):
    '''Checks monograms against english using chi-squared test'''
    monogram_dict = load_monogram_count(mono_directory,mono_file)
    monogram_dict = dict(sorted(monogram_dict.items(), key=lambda x:x[0].replace(" ", "_")))
    for key in monogram_dict.keys():
        monogram_dict[key] = float(monogram_dict[key])

    text_dict = count_monograms(text,"alphabet",case_insensitive=case_insensitive, include_spaces=include_spaces, include_nums=include_nums,include_punc=include_punc)

    return 1/float(chi_squared(list(text_dict.values()), list(monogram_dict.values())))

def check_monograms_angle_vectors(text:str, mono_directory:str, mono_file:str,case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False):
    '''Checks monograms against english using angle between vectors'''
    monogram_dict = load_monogram_count(mono_directory,mono_file)
    monogram_dict = dict(sorted(monogram_dict.items(), key=lambda x:x[0].replace(" ", "_")))
    for key in monogram_dict.keys():
        monogram_dict[key] = float(monogram_dict[key])

    expected_vector = list(monogram_dict.values())

    text_dict = count_monograms(text,"alphabet",case_insensitive=case_insensitive,include_spaces=include_spaces,include_nums=include_nums,include_punc=include_punc)

    text_vector = list(text_dict.values())

    return cos_angle_between_vectors(expected_vector,text_vector)

def check_tetragrams(text:str, quad_directory:str, quad_file:str,case_insensitive:bool=True, include_spaces:bool=False, include_nums:bool=False, include_punc:bool=False):
    '''Checks fitness of text by using logs of frequencies of tetragrams, english ~> -10'''
    with open(os.path.join(quad_directory,quad_file), "r") as f:
        quadgrams_dict = construct_dict(f.read(),mid_sep=MID_SEP,end_sep=END_SEP)
    
    quadgrams_dict = dict(sorted(quadgrams_dict.items(), key=lambda x:x[0].replace(" ", "_")))

    fitness = 0

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


    for i in range(len(text)-3):
        tetragram = text[i:i+4]
        if tetragram in quadgrams_dict:
            f_english = float(quadgrams_dict[tetragram])
            fitness += f_english
        
    num_terms = len(text)-3
    if num_terms > 0:
        fitness /= num_terms
    else:
        fitness = float('-inf')

    return fitness

if __name__ == '__main__':
    text = '''From Zanzibar to Zambia to Zaire, ozone zones make zebras run zany zigzags'''
    # print(check_monograms_chi_squared(text,"src/resources","engcorpmonofreqs.txt"))
    print(check_tetragrams(text, "src/resources","engcorptetlogfreqs.txt"))