import os
from src.ciphers.objects import Settings

# Default values for settings
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHANUMPUNC = "a"
MINLENGTH = 2 # Minimum alphabet length - two letters?
MAXLENGTH = 40 # Maximum alphabet length

history_directory = os.path.relpath('cipher-challenge-decoder/src/history')

def get_default_settings():
    return Settings(ALPHABET, ALPHANUMPUNC, MINLENGTH, MAXLENGTH)

def create_log_file():
    pass

def get_default_log_file(log_id):
    return os.path.relpath('cipher-challenge-decoder/src/history') + f'log-{log_id}'
