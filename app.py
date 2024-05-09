from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__, template_folder='./template')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('sign.html')


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    text = request.json['text']
    target_language = request.json['target_language']

    translator = Translator()
    translations = {}
    translations[target_language] = translator.translate(text, dest=target_language).text

    return jsonify(translations)

if __name__ == '__main__':
    app.run(debug=True)
