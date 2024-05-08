from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
