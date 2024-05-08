from flask import Flask

app = Flask(__name__)

@app.route('/')
def landing():
    return "Welcome to the landing page"


@app.route('/signup')
def signup():
    return "<h1>Signup Page</h1><p>This is the signup page. Please fill out the form to sign up.</p>"

if __name__ == '__main__':
    app.run(debug=True)
