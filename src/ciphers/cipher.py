#from src.resources.consts import get_defaults as get_default_settings
from resources.consts import get_default_settings
from ciphers.objects import Settings

MIN_LENGTH = 26 # UPDATE TO WORK WITH IMPORTED CONSTS
MAX_LENGTH = 26 # UPDATE TO WORK WITH IMPORTED CONSTS
ALPHANUMPUNC = "a" # a, an, anp, ap [assuming alpha primary]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ACCEPTABLEALPHANUMPUNC = ["a", "an", "anp", "ap", "n"]

class Cipher():
    def __init__(self, settings=get_default_settings()):
        self.tight = settings.tight
        self.min_length = settings.min_length
        self.max_length = settings.max_length
        self.alpha_numeric_punctuation = settings.alpha_numeric_punctuation
        self.alphabet = settings.alphabet

    def get_settings(self):
        return Settings(alphabet=self.alphabet, tight=self.tight, min_length=self.min_length, alpha_numeric_punctuation=self.alpha_numeric_punctuation)

    def save_to_history(self, dir, filename):
        pass

    @property
    def tight(self):
        return self._tight
    
    @tight.setter
    def tight(self,new_tight):
        if new_tight not in [True,False]:
            raise ValueError("INVALID TIGHTNESS")
        else:
            self._tight = new_tight

    
    @property
    def min_length(self):
        return self._min_length
    
    @min_length.setter
    def min_length(self,new_min_length):
        # CHECK AGAINST TYPES ETC SANTIY CHECK
        self._min_length = new_min_length

    @property
    def max_length(self):
        return self._max_length
    
    @max_length.setter
    def max_length(self, new_max_length):
        # CHECK AGAINST TYPES ETC SANITY CHECK
        self._max_length = new_max_length


    @property
    def alphabet(self):
        return self._alphabet
    
    @alphabet.setter
    def alphabet(self, new_alphabet):
        if len(new_alphabet) >= MIN_LENGTH and len(new_alphabet) <= MAX_LENGTH:
            # match self.alpha_numeric_punctuation:
                #case "a":
                #case "an":
                # ...
                # check whether alphabet fits in criteria
            self._alphabet = new_alphabet
        else:
            raise ValueError(f"Alphabet of invalid length {len(new_alphabet)}, must be between {MIN_LENGTH} and {MAX_LENGTH}")
        
    @property
    def alpha_numeric_punctuation(self):
        return self._alpha_numeric_punctuation
    
    @alpha_numeric_punctuation.setter
    def alpha_numeric_punctuation(self, new_setting):
        if new_setting not in ACCEPTABLEALPHANUMPUNC:
            raise ValueError("Alphabet type not valid, must be one of: '" + "', '".join([val for val in ACCEPTABLEALPHANUMPUNC]) + "'")
        self._alpha_numeric_punctuation = new_setting
