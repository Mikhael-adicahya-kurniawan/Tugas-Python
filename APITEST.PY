from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world! <br> Ini Pertemuan 4 AP2B"

@app.route('/about')
def about():
    return "Hello, world! <br> Ini Pertemuan AP2B <br> Murid : Mikhael Adicahya Kurniawan"

if __name__ == '__main__':
    app.run(debug = True)
    