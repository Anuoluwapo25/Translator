from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from app import translate_text

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['input-text']
    target_language = request.form['target_language']

    if not text or not target_language:
	return jsonify({'error': 'Invalid request'})

    translation = translate_text(text, target_language)

    return render_template('translate.html', text=text, translation=translation)

if __name__ == '__main__':
    app.run(debug=True)

