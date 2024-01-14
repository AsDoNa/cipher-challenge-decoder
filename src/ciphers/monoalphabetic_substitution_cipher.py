from ciphers.cipher import Cipher
from ciphers.objects import Settings
from ciphers.useful import filter as filteranp

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class MonoalphabeticSubstitution(Cipher):
    def __init__(self,settings=Settings(alphabet=ALPHABET,tight=True,alpha_numeric_punctuation="a",min_length=26,max_length=26)):
        # Do stuff
        super().__init__(settings)

    def encode(self, plaintext:str, alphabet_key:str, settings:Settings=None):

        if not isinstance(settings,Settings):
            settings = self.settings

        if settings.tight:
            plaintext = filteranp(plaintext)

        plaintext_array = [char for char in plaintext]
        ciphertext_array = []

        encoding_dict = {}
        if len(settings.alphabet) != len(alphabet_key):
            raise ValueError(f"INVALID ALPHABET KEY LENGTH: ALPHABET IS {len(settings.alphabet)} CHARS, KEY IS {len(alphabet_key)} chars")
        for i in range(len(alphabet_key)):
            encoding_dict[settings.alphabet[i]] = alphabet_key[i]

        for char in plaintext_array:
            if settings.tight:
                ciphertext_array.append(encoding_dict[char])
            else:
                if char not in settings.alphabet:
                    ciphertext_array.append(char)
                else:
                    ciphertext_array.append(encoding_dict[char])

        ciphertext = "".join(ciphertext_array)

        return ciphertext
    
    def invert_alphabet(self,alphabet_key:str,settings:Settings=None):
        if not isinstance(settings,Settings):
            settings = self.settings
        if len(alphabet_key) != len(settings.alphabet):
            raise ValueError(f"INVALID KEY ALPHABET LENGTH, KEY ALPHABET IS {len(alphabet_key)}, ALPHABET IS {len(settings.get_settings()['alphabet'])}")

        alphabet_to_key_alphabet = {}
        for indx, char in enumerate(settings.alphabet):
            alphabet_to_key_alphabet[char] = alphabet_key[indx]

        inverse_alphabet = dict(sorted(alphabet_to_key_alphabet.items(),key=lambda x:x[1].replace(" ", "_")))

        return "".join(list(inverse_alphabet.keys()))

    def decode(self, ciphertext:str, alphabet_key:str, settings:Settings=None, inverse_alphabet:str=None):
        if not isinstance(settings,Settings):
            settings = self.settings
        
        if inverse_alphabet is None or len(inverse_alphabet) == 0:
            new_alphabet = self.invert_alphabet(alphabet_key, settings)
        else:
            new_alphabet = inverse_alphabet

        return self.encode(ciphertext,new_alphabet,settings)
    
if __name__ == '__main__':
    mono_sub_engine = MonoalphabeticSubstitution()
    # print(mono_sub_engine.invert_alphabet("KNOFPEUCARBMGXQIZWYSTJVDHL"))
    # print(mono_sub_engine.encode('''Sally sells seashells by the seashore''', "ATSPWGKHVXDLCJZEMFBRYUONIQ"))
    # print(mono_sub_engine.decode('''PFAFIPGPFIPGKLFTCPFKLHVPGKLEFTPFPPFIZ''', "CSKTFVRMGQLEXDHPJIZANBOUWY"))