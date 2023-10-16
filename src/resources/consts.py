import os
from ciphers.objects import Settings

# Default values for settings
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHANUMPUNC = "a"
MINLENGTH = 2 # Minimum alphabet length - two letters?
MAXLENGTH = 40 # Maximum alphabet length
TIGHT = True # Tightness

history_directory = os.path.relpath('cipher-challenge-decoder/src/history')

def get_default_settings():
    return Settings(alphabet=ALPHABET, tight=TIGHT, alpha_numeric_punctuation=ALPHANUMPUNC, min_length=MINLENGTH, max_length=MAXLENGTH)

def create_log_file():
    pass

def get_default_log_file(log_id):
    return os.path.relpath('cipher-challenge-decoder/src/history') + f'log-{log_id}'
