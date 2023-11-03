from src.ciphers.objects import Settings

MIN_LENGTH = 26 # UPDATE TO WORK WITH IMPORTED CONSTS
MAX_LENGTH = 26 # UPDATE TO WORK WITH IMPORTED CONSTS
ALPHANUMPUNC = "a" # a, an, anp, ap [assuming alpha primary]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ACCEPTABLEALPHANUMPUNC = ["a", "an", "anp", "ap", "n"]

class Cipher():
    def __init__(self, settings=Settings.get_default_settings()):
        self.settings = settings

    @property
    def settings(self):
        return self._settings
    
    @settings.setter
    def settings(self,new_settings):
        if isinstance(new_settings, Settings):
            self._settings = new_settings
        else:
            raise ValueError("INVALID SETTINGS TYPE")

    def save_to_history(self, dir, filename):
        pass
