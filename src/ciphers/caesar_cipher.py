from cipher import Cipher
from objects import Settings

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Caesar(Cipher):
    def __init__(self, settings=Settings(ALPHABET, "a", 26, 26)):
        # do init stuff
        super().__init__(settings)

    def encode(self, plaintext, shift, settings=None):
        plaintext_array = [char for char in plaintext]
        ciphertext_array = []

        for char in plaintext_array:
            ciphertext_array.append(ALPHABET[(ALPHABET.index(char)+shift) % len(ALPHABET)])

        ciphertext = "".join(ciphertext_array)

        return ciphertext

        

    def decode(self, ciphertext, shift, settings=None):
        ciphertext_array = [char for char in ciphertext]
        plaintext_array = []

        for char in ciphertext_array:
            plaintext_array.append(ALPHABET[(ALPHABET.index(char)-shift) % len(ALPHABET)])

        plaintext = "".join(plaintext_array)

        return plaintext