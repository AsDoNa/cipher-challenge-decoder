import requests
import re
import os
from src.resources.progress_bar import update_progress

MID_SEP = ":"
END_SEP = ","

def load_corpora(save:bool=False, filename:str="", directory:str=""):
    '''Loads the brown corpus from online, returns or saves an uppercase punctuation-less version'''

    brown_url = "http://www.sls.hawaii.edu/bley-vroman/brown.txt"

    response = requests.get(brown_url)
    brown = response.text

    brown_punctless = re.sub('[^A-Za-z0-9 \n]+', '', brown)
    brown_punctless = re.sub(' +', ' ', brown_punctless)
    brown_punctless_upper = brown_punctless.upper()

    if save and len(filename) != 0 and len(directory) != 0:
        with open(os.path.join(directory, filename), "w",) as f:
            f.write(brown_punctless_upper)
    else:
        return brown_punctless_upper

def find_unique_words(search_text:str, word_list:list=[]):
    '''Returns an alphabetically-sorted list of unique words in a text (assuming non-punctuation)'''
    
    words = re.sub("[ \n]+", " ", search_text)
    words = words.split(" ")

    print("SEARCHING WORDS")
    print()

    num_words = len(words)
    i = 0
    for word in words:
        if word not in word_list:
            word_list.append(word)
        i += 1
        update_progress(i, num_words)

    word_list = sorted(word_list)

    return word_list

def find_unique_words_file(directory:str, file:str, save:bool=False, save_dir:str="", save_file:str=""):
    '''Creates an alphabetically-sorted list of unique words in a file and returns or saves it'''

    unique_words = []
    word_list = []

    if save:
        try:
            with open(os.path.join(save_dir, save_file), "r") as f:
                word_list = f.read().split(" ")
        except FileNotFoundError:
            pass

    with open(os.path.join(directory,file), "r") as f:
        words = " ".join(f.readlines()) # Convert newline chars to spaces
        unique_words = find_unique_words(words, word_list)
    
    if save:
        with open(os.path.join(save_dir, save_file), "w") as f:
            f.write(" ".join(unique_words))
    else:
        return unique_words

def count_words(search_text:str):
    '''Returns a dictionary of words and frequencies in a text in descending order'''

    words = re.sub("[ \n]+", " ", search_text)
    words = words.split(" ")
    word_dict = {}

    print("SEARCHING WORDS")
    print()

    num_words = len(words)
    i = 0
    for word in words:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1
        i += 1
        update_progress(i, num_words)

    word_dict = dict(sorted(word_dict.items(), key=lambda x:x[1], reverse=True))

    return word_dict

def count_words_file(directory:str, file:str, save:bool=False, save_dir:str="", save_file:str=""):
    '''Creates a list of words in a file and their frequencies (in descending order) and returns or saves it'''

    word_freqs_dict = {}

    with open(os.path.join(directory,file), "r") as f:
        words = " ".join(f.readlines())
        word_freqs_dict = count_words(words)

    if save:
        print("SAVING WORD FREQUENCIES")
        print()
        with open(os.path.join(save_dir,save_file), "w") as f:
            num_words = len(word_freqs_dict)
            i = 0
            for word in word_freqs_dict.keys():
                if len(word) != 0:
                    if i < len(word_freqs_dict.keys()) - 2:
                        f.write(f'{word}{MID_SEP}{word_freqs_dict[word]}{END_SEP}')
                    else:
                        f.write(f'{word}{MID_SEP}{word_freqs_dict[word]}')

                i += 1
                update_progress(i,num_words)

    else:
        return word_freqs_dict

def read_frequency_file(directory:str,file:str,mid_sep:str=MID_SEP,end_sep:str=END_SEP):
    '''Reads the word frequencies from a file [created with count_words_file()]'''

    word_freq_dict = {}

    with open(os.path.join(directory,file), "r") as f:
        word_freq_array = f.read().split(end_sep)
        for word_freq in word_freq_array:
            # print(word_freq)
            if len(word_freq) != 0:
                word,freq = word_freq.split(mid_sep)
                word_freq_dict[word] = freq

    return word_freq_dict

if __name__ == "__main__":
    # load_corpora(True, "engcorp.txt", "src/resources")
    # corpus = load_corpora(False)
    # find_unique_words_file("src/resources","engcorp.txt",True,"src/resources","engcorpunique.txt")
    count_words_file("src/resources","engcorp.txt",True,"src/resources","engcorpcounts.txt")
    # word_freq_dict = read_frequency_file("src/resources","engcorpcounts.txt")