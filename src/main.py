from flask import Flask,render_template,request,send_from_directory

from src.ciphers.objects import Settings
from src.ciphers.caesar_cipher import Caesar
from src.ciphers.shifting_caesar import ShiftingCaesar
from src.ciphers.monoalphabetic_substitution_cipher import MonoalphabeticSubstitution

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ciphers/caesar-cipher', methods=['GET', 'POST'])
def caesar_cipher():
    result = ""
    if request.method == 'POST':
        
        text = request.form['text']
        shift = int(request.form['shift'])
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',26), 
                            max_length=request.form.get('max_length',26)
                            )
        
        cipher_obj = Caesar(settings)

        if operation == 'encode':
            result = cipher_obj.encode(text,shift)
        elif operation == 'decode':
            result = cipher_obj.decode(text,shift)
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/caesar_cipher.html', result=result)

@app.route('/ciphers/shifting-caesar-cipher', methods=['GET', 'POST'])
def shifting_caesar_cipher():
    result = ""
    if request.method == 'POST':
        
        text = request.form['text']
        shift_length = int(request.form['shift_length'])
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',26), 
                            max_length=request.form.get('max_length',26)
                            )
        
        cipher_obj = ShiftingCaesar(settings)

        if operation == 'encode':
            result = cipher_obj.encode(text,shift_length, settings=settings)
        elif operation == 'decode':
            result = cipher_obj.decode(text,shift_length, settings=settings)
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/shifting_caesar_cipher.html', result=result)

@app.route('/ciphers/monoalphabetic-substitution-cipher', methods=['GET', 'POST'])
def monoalphabetic_substitution_cipher():
    result = ""
    if request.method == 'POST':
        
        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',26), 
                            max_length=request.form.get('max_length',26)
                            )

        cipher_obj = MonoalphabeticSubstitution(settings)

        text = request.form['text']
        key_alphabet = request.form.get('key',cipher_obj.invert_alphabet(request.form.get('inverse-key')))
        inverse_key = request.form.get('inverse-key',cipher_obj.invert_alphabet(request.form.get('key')))
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        if operation == 'encode':
            result = cipher_obj.encode(text,key_alphabet, settings=settings)
        elif operation == 'decode':
            result = cipher_obj.decode(text,key_alphabet, settings=settings, inverse_alphabet=inverse_key)
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/monoalphabetic_substitution_cipher.html', result=result)

@app.route('/tools/corpus-management', methods=['GET', 'POST'])
def corpus_management():
    result = ""
    if request.method == "POST":
        corpus = request.form['corpus']
        operation = request.form['operation']

    return render_template('/tools/corpus_management.html',result=result)

@app.route('/static/js/<path:filename>')
def js(filename):
    return send_from_directory('static/js', filename)

@app.route('/static/css/<path:filename>')
def css(filename):
    return send_from_directory('static/css', filename)

@app.route('/assets/images/<path:filename>')
def image(filename):
    return send_from_directory('static/images', filename)

if __name__ == "__main__":
    app.run(debug=True)