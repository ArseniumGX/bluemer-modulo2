from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, jsonify, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_required, logout_user, login_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:3009/blue_modulo3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
login = LoginManager(app)

########################################################################
class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(85))
    image = db.Column(db.String)
    link = db.Column(db.String, nullable=False)
    last_login = db.Column(db.Date)


    def __init__(self, name, description, image, link) -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.image = image
        self.link = link
########################################################################

########################################################################
class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(103), nullable=False)
    last_login = db.Column(db.Date, nullable=True)

    def __init__(self, name, username, password) -> None:
        super().__init__()
        self.name = name
        self.username = username
        self.password = password
        self.last_login = None

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)
    
    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def set_date(self):
        from datetime import date
        self.last_login = date.today()

########################################################################

@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))

########################################################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        admin = Admin(
            request.json['name'],
            request.json['username'],
            request.json['password']
        )

        admin.set_password(request.json['password'])
        db.session.add(admin)
        db.session.commit()
        return jsonify({'Message': 'Administrator created!'}), 201

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('admin'))

    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        user = Admin.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user, remember=True)
            user.set_date()
            db.session.commit()
            return redirect(url_for('admin'))
        else:
            flash('Usuário ou senha inválidos!')
            return redirect(url_for('login'))


@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@app.route('/admin/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/<slug>')
def slug(slug):
    return render_template('notfound.html', slug=slug), 404

if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=3000)