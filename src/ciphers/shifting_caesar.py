from cipher import Cipher
from caesar_cipher import Caesar
from objects import Settings
from useful import space_by

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class ShiftingCaesar(Cipher):
    def __init__(self, settings=Settings(ALPHABET, "a", 26, 26)):
        super().__init__(settings)

    def encode(self,plaintext,shift_length=1, settings=None):
        caesar = Caesar(settings)
        plaintext_array = []
        for i in range(0,len(plaintext),shift_length):
            plaintext_array.append(plaintext[i:i+shift_length])
        ciphertext_array = []

        for shift, shift_sequence in enumerate(plaintext_array):
            ciphertext_array.append(caesar.encode(shift_sequence,shift))

        ciphertext = "".join(ciphertext_array)
        print(ciphertext)
        
        return ciphertext
    
    def decode(self,plaintext,shift_length=1, settings=None):
        caesar = Caesar(settings)
        plaintext_array = []
        for i in range(0,len(plaintext),shift_length):
            plaintext_array.append(plaintext[i:i+shift_length])
        ciphertext_array = []

        for shift, shift_sequence in enumerate(plaintext_array):
            ciphertext_array.append(caesar.decode(shift_sequence,shift))

        ciphertext = "".join(ciphertext_array)
        
        return ciphertext
            

sc = ShiftingCaesar()
plaintext = '''Welcome to my final challenge,
A message for long hidden in depths of darkness,
Now emerging for one last breath,
Before diving down deep into national competition.
A simpler fate this week awaits you,
Among the characters a simple pattern,
Though one shrouded in mystery,
perhaps look deeper and you’ll see.
A confusing tumbling mess of letters,
this way and that; back and forth,
though beauty can be seen through a lens,
and when pattern emerges it all comes clear.
Next week we will not meet together,
Though in halls online we see,
A hidden message pop up in code,
Unravelling a mystery leading to victory.
The Cipher Master for long now awaits,
Your success in paralleling competition’s greats.'''.upper()
for char in plaintext:
    if char not in ALPHABET:
        plaintext = plaintext.replace(char,"")
print(plaintext)
print(space_by(sc.encode(plaintext,3),5))