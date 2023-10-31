from flask import Flask, render_template, request, redirect, url_for, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    def __repr__(self) -> str:
        return self.nome
    
class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Bruno', 'BD', 'Alohomora')
usuario2 = Usuario('Camila', 'Mila', 'Pao')
usuario3 = Usuario('Guilherme', 'Gui', '4123')
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')

usuarios = {usuario1.nickname : usuario1, 
            usuario2.nickname : usuario2, 
            usuario3.nickname : usuario3}
jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = ["key"]

@app.route('/')
def index():
    return render_template("lista.html", title='Jogos', jogos=jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template("novo.html", title="Novo jogo")

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html', title="Login")


@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    nickname = request.form['usuario']
    if nickname in usuarios:
        senha = request.form['senha']
        if senha == usuarios[nickname].senha:
            session['usuario_logado'] = request.form['usuario']
            flash("Logado com sucesso", category='info')
        return redirect(url_for('index'))
    flash("Usuário/Senha incorretos", category='warning')
    return redirect(url_for('login'))
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso', category='info')
    return redirect(url_for('index'))

app.run(debug=True)