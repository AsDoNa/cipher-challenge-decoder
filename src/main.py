from flask import Flask,render_template,request,send_from_directory

from ciphers.objects import Settings
from ciphers.caesar_cipher import Caesar

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/caesar-cipher', methods=['GET', 'POST'])
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
        
    return render_template('caesar_cipher.html', result=result)

@app.route('/assets/scripts/<path:filename>')
def script(filename):
    return send_from_directory('assets/scripts', filename)

@app.route('/assets/stylesheets/<path:filename>')
def stylesheet(filename):
    return send_from_directory('assets/stylesheets', filename)

if __name__ == "__main__":
    app.run(debug=True)