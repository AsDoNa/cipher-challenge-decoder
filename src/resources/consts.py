import os

# Default values for settings
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHANUMPUNC = "a"
MINLENGTH = 2 # Minimum alphabet length - two letters?
MAXLENGTH = 40 # Maximum alphabet length
TIGHT = True # Tightness
ACCEPTABLEALPHANUMPUNC = ["a","an","anp","ap"]

history_directory = os.path.relpath('cipher-challenge-decoder/src/history')

def create_log_file():
    pass

def get_default_log_file(log_id):
    return os.path.relpath('cipher-challenge-decoder/src/history') + f'log-{log_id}'
