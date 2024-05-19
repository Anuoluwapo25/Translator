from flask import Flask, render_template, request, jsonify
from main import translate_text


app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

#@app.route('/signupage', methods=["POST", "GET"])
#def signupage():
 #   name = request.form['name']
  #  email = request.form['email']
   # password = request.form['password']
   # hashedpassword = bcrypt.generate_password_hash(password)
    
    
    #userExist = User.query.filter_by(email=email).first() is not None
    #if userExist:
     #   return jsonify({
     #       "error":"User already exist"
    #    }), 409
    
   # new_user = User(name=name, email=email, password=hashedpassword)
    #db.session.add(new_user)
   # db.session.commit()
    #return jsonify({
       # 'name':new_user.name,
      #  'email': new_user.email,
     #   'id': new_user.id
    #})

@app.route('/login')
def login():
    return render_template('login.html')

#@app.route('/loginpage', methods=["POST"])
#def loginpage():
    #email = request.form['email']
    #password = request.form['password']
    
    #user =  User.query.filter_by(email=email).first()
    
    #if user is None:
       # return jsonify({
      #      "error": "user doesnt exist"
     #   }), 401
        
    #if not bcrypt.check_password_hash(user.password, password):
        
        #return jsonify({
       #     "error": "check your password"
      #  }), 401

    #return jsonify({
      #  "name": user.name,
     #   "email": user.email,
    #    "id":user.id
   # })

@app.route('/translate')
def translator():
    return render_template('translate.html')

@app.route('/translator', methods=['POST'])
def translate():
    text = request.form['input-text']
    target_language = request.form['target_language']

    if not text or not target_language: 
        return jsonify({'error': 'Invalid request'})

    translation = translate_text(text, target_language)

    return render_template('translate.html', text=text, translation=translation)

if __name__ == '__main__':
    #with app.app_context():
      #  db.create_all()
    app.run(debug=True)

