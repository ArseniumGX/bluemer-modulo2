from flask import Flask, render_template, jsonify
from cryptography.fernet import Fernet
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:3009/blue_modulo3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

########################################################################
class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(85))
    image = db.Column(db.String)
    link = db.Column(db.String, nullable=False)

    def __init__(self, name, description, image, link) -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.image = image
        self.link = link
########################################################################

########################################################################
class Acesso(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    key = db.Column(db.String(50), nullable=False)

    def __init__(self, name, username, password) -> None:
        super().__init__()
        self.name = name
        self.username = username
        self.password = cryptPass(password)
        self.key = Fernet.generate_key()

    def cryptPass(self, password):
        return 
########################################################################

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        acess = Acesso(
            request.json['name'],
            request.json['username'],
            request.json['password'],
        )


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=3000)