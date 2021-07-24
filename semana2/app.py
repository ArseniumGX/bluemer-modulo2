from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from mail_settings import mail_settings
from contato import Contato

app = Flask(__name__)

lista = list()

app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html',  lista = lista)

@app.route('/form')
def formulario():
    return render_template('formulario.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato()
        formContato.name = request.form['name']
        formContato.email = request.form['email']
        formContato.message = request.form['message']

        msg = Message(
            subject='Contato do seu portifólio',
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[app.config.get("MAIL_USERNAME")],
            body=f'''O {formContato.name} enviou a seguinte mensagem:\n\n{formContato.message}'''
        )

        mail.send(msg)
        return redirect('/form')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item = request.form['item']
        lista.append(item)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')
