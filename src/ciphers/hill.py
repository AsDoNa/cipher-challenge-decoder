from ciphers.cipher import Cipher
from ciphers.objects import Settings
from ciphers.useful import filter as filteranp

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Hill(Cipher):
    def __init__(self, settings=Settings(ALPHABET, True, "a", 26, 26)):
        super().__init__(settings)

    def encode(self, )

