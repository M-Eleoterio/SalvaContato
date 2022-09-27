from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodados.db'

db = SQLAlchemy(app)

class Contato(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

@ app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        contato = Contato(request.form['nome'], request.form['email'])
        db.session.add(contato)
        db.session.commit()
        return redirect('https://salvacontato.rj.r.appspot.com/lista')
    return render_template('add.html')

@ app.route('/lista')
def lista():
    return render_template('lista.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
