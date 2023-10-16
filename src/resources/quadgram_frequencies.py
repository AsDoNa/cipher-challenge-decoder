# import os

# class quadgram_score():
#     def __init__(self, dir, corpusfile, sep=" "):

#         self.ngrams = {}
#         with open(os.path.join(dir, corpusfile), "r") as f:
#             for line in f.readlines():
#                 key, count = line.split(sep)
#                 self.ngrams[key] = count
#             self.len = len(key) # 4 as quadgrams
#             self.