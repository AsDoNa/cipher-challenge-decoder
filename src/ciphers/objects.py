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
        self._min_length = new_min_length

    @property
    def max_length(self):
        return self._max_length
    
    @max_length.setter
    def max_length(self, new_max_length):
        # CHECK AGAINST TYPES ETC SANITY CHECK
        self._max_length = new_max_length

    @property
    def alpha_numeric_punctuation(self):
        return self._alpha_numeric_punctuation
    
    @alpha_numeric_punctuation.setter
    def alpha_numeric_punctuation(self, new_anr):
        # SANITY CHECK AGAINST VALID
        self._alpha_numeric_punctuation = new_anr

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, new_alphabet):
        # CHECK AGAINST SETTINGS
        self._alphabet = new_alphabet

    def get_settings(self):
        return {
            "min-length": self.min_length,
            "max-length": self.max_length,
            "anp": self.alpha_numeric_punctuation,
            "alphabet": self.alphabet
        }
    
    def __iter__(self):
        return self

    def __next__(self):
        attrs = ['min_length', 'max_length', 'alpha_numeric_punctuation', 'alphabet']
        if not attrs:
          raise StopIteration
        attr = attrs.pop(0) 
        return attr, getattr(self, attr)