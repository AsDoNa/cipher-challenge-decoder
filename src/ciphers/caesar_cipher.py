from ciphers.cipher import Cipher
from ciphers.objects import Settings
from ciphers.useful import filter as filteranp

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Caesar(Cipher):
    def __init__(self, settings=Settings(ALPHABET, True, "a", 26, 26)):
        # do init stuff
        super().__init__(settings)

    def encode(self, plaintext:str, shift:int, settings:Settings=None):
        if not isinstance(settings, Settings):
            settings = self.settings
        if settings.tight:
            plaintext = filteranp(plaintext) # ALLOW FOR CUSTOMISATION
        plaintext_array = [char for char in plaintext]
        ciphertext_array = []

        for char in plaintext_array:
            if settings.tight:
                ciphertext_array.append(settings.alphabet[(settings.alphabet.index(char)+shift) % len(settings.alphabet)])
            else:
                if char not in settings.alphabet:
                    ciphertext_array.append(char)
                else:
                    ciphertext_array.append(settings.alphabet[(settings.alphabet.index(char)+shift) % len(settings.alphabet)])

        ciphertext = "".join(ciphertext_array)

        return ciphertext 

    def decode(self, ciphertext, shift, settings=None):
        if not isinstance(settings, Settings):
            settings = self.settings
        if settings.tight:
            # ciphertext = filteranp(ciphertext) # ALLOW FOR CUSTOMISATION
            ciphertext = "".join([char for char in ciphertext if char in settings.alphabet])
        
        ciphertext_array = [char for char in ciphertext]
        plaintext_array = []

        for char in ciphertext_array:
            if settings.tight:
                plaintext_array.append(settings.alphabet[(settings.alphabet.index(char)-shift) % len(settings.alphabet)])
            else:
                if char not in settings.alphabet:
                    plaintext_array.append(char)
                else:
                    plaintext_array.append(settings.alphabet[(settings.alphabet.index(char)-shift) % len(settings.alphabet)])

        plaintext = "".join(plaintext_array)

        return plaintext