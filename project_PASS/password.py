from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    if length < 8:
        length = 8
    if length > 30:
        length = 30
    
    password_chars = [
        random.choice(string.ascii_uppercase),  # 1 большая буква
        random.choice(string.digits),           # 1 цифра
        random.choice(string.punctuation),      # 1 специальный символ
    ]
    
    remaining_length = length - len(password_chars)
    characters = string.ascii_letters + string.digits + string.punctuation
    password_chars += random.choices(characters, k=remaining_length)
    
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
