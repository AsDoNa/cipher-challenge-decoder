from src.resources.consts import ACCEPTABLEALPHANUMPUNC,ALPHABET,TIGHT,ALPHANUMPUNC,MINLENGTH,MAXLENGTH

class Settings():
    def __init__(self, alphabet:str=None, tight:bool=None, alpha_numeric_punctuation:str=None, min_length:int=None, max_length:int=None):
        self.tight = tight
        self.min_length = min_length
        self.max_length = max_length
        self.alpha_numeric_punctuation = alpha_numeric_punctuation
        self.alphabet = alphabet

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
        self._min_length = int(new_min_length)

    @property
    def max_length(self):
        return self._max_length
    
    @max_length.setter
    def max_length(self, new_max_length):
        # CHECK AGAINST TYPES ETC SANITY CHECK
        self._max_length = int(new_max_length)


    @property
    def alphabet(self):
        return self._alphabet
    
    @alphabet.setter
    def alphabet(self, new_alphabet):
        if len(new_alphabet) >= self.min_length and len(new_alphabet) <= self._max_length:
            # match self.alpha_numeric_punctuation:
                #case "a":
                #case "an":
                # ...
                # check whether alphabet fits in criteria
            self._alphabet = new_alphabet
        else:
            raise ValueError(f"Alphabet of invalid length {len(new_alphabet)}, must be between {self.min_length} and {self.max_length}")
        
    @property
    def alpha_numeric_punctuation(self):
        return self._alpha_numeric_punctuation
    
    @alpha_numeric_punctuation.setter
    def alpha_numeric_punctuation(self, new_setting):
        if new_setting not in ACCEPTABLEALPHANUMPUNC:
            raise ValueError("Alphabet type not valid, must be one of: '" + "', '".join([val for val in ACCEPTABLEALPHANUMPUNC]) + "'")
        self._alpha_numeric_punctuation = new_setting

    def get_settings(self):
        return {
            "min-length": self.min_length,
            "max-length": self.max_length,
            "anp": self.alpha_numeric_punctuation,
            "alphabet": self.alphabet
        }
    
    @classmethod
    def get_default_settings(cls):
        return Settings(alphabet=ALPHABET, tight=TIGHT, alpha_numeric_punctuation=ALPHANUMPUNC, min_length=MINLENGTH, max_length=MAXLENGTH)
    
    def __iter__(self):
        return self

    def __next__(self):
        attrs = ['min_length', 'max_length', 'alpha_numeric_punctuation', 'alphabet']
        if not attrs:
          raise StopIteration
        attr = attrs.pop(0) 
        return attr, getattr(self, attr)