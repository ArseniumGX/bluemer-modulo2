from flask import Flask, render_template, request, redirect

app = Flask(__name__)
lista = list()

@app.route('/')
def index():
    return render_template('index.html',  lista = lista)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item = request.form['item']
        lista.append(item)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')
