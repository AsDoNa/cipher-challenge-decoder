from math import sqrt
from src.resources.progress_bar import update_progress

def construct_dict(text:str, mid_sep:str, end_sep:str):
    text_arr = text.split(end_sep)
    return_dict = {}

    for line in text_arr:
        if len(line) != 0:
            key,value = line.split(mid_sep)
            return_dict[key] = value

    return return_dict

def dot_product(vector1:list, vector2:list):
    if len(vector1) != len(vector2):
        raise ValueError("VECTORS ARE NOT SAME DIMENSIONALITY")
    
    result = 0
    for i in range(len(vector1)):
        result += vector1[i]*vector2[i]
    
    return result

def cos_angle_between_vectors(vector1:list, vector2:list):
    if len(vector1) != len(vector2):
        raise ValueError("VECTORS ARE NOT SAME DIMENSIONALITY")

    cos_value = dot_product(vector1,vector2)/sqrt(dot_product(vector1,vector1)*dot_product(vector2,vector2))

    return cos_value

def strip_to_alphabet(text:str,alphabet:str):
    return "".join([char for char in text if char in alphabet])

def generate_possible_ngrams(n:int,alphabet:str):
    '''Returns a list of all possible (n)-grams in the given alphabet'''
    possible_ngrams = list(alphabet)
    possible_ngrams_temp = []
    total_ngrams = 0
    for i in range(1,n+1):
        total_ngrams+=len(alphabet)**i

    i=0
    print(f"GENERATING POSSIBLE {n}-GRAMS")
    print()
    update_progress(i,total_ngrams)
    for _ in range(1,n):
        for item in possible_ngrams:
            for char in alphabet:
                possible_ngrams_temp.append(str(item+char))
                i+=1
                update_progress(i,total_ngrams)
        possible_ngrams = possible_ngrams_temp
        possible_ngrams_temp = []

    return possible_ngrams

def calculate_nonoverlapping_ngrams(text:str,n:int,alphabet:str,generate_ngrams:bool=False):
    
    if generate_ngrams:
        possible_ngrams = dict([(ngram,0) for ngram in generate_possible_ngrams(n,alphabet)])
    else:
        possible_ngrams = {}

    num_chars = len(text)
    i = 0

    print(f"COUNTING {n}-GRAMS IN TEXT")
    print()
    for i in range(0,len(text),n):
        try:
            ngram = text[i:i+n]
            if len(ngram) < n:
                raise IndexError
        except IndexError: # END OF TEXT (IF LEN NOT DIVISIBLE BY N)
            break
        if generate_ngrams:
            possible_ngrams[ngram] += 1
        else:
            if ngram in possible_ngrams:
                possible_ngrams[ngram] += 1
            else:
                possible_ngrams[ngram] = 1
        update_progress(i,num_chars)

    possible_ngrams = dict(sorted(possible_ngrams.items(), key=lambda x:x[0].replace(" ", "_")))

    return possible_ngrams

if __name__ == '__main__':
    # calculate_nonoverlapping_ngrams("IUGHEFWUGIGBWEBIGEWUOGBOUEWBFOUWEBROUFBNWEOFBOUWEBFVOUEWBNVOUWENVOIJMREDOINOUBNGIUOBIUREOGBIOUREBNGIOUERNGOJENROUVBEIORUJBNVERVBERIUVBEIRUBVREIOUWBVOUEWQBNOUEWRNVOIENROIVNMIOWERMVOIEWNVOINEWOUVBEOUWINVIUBWEOUVBEWIUOBVIUEWVIUEWBVIUBWEIUBV",3,"ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    pass