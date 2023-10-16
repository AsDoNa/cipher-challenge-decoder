import re

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