from cipher import Cipher
from objects import Settings

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Affine(Cipher):
    def __init__(self, settings=Settings(ALPHABET, "a", 26, 26)):
        
