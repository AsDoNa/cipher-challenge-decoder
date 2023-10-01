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