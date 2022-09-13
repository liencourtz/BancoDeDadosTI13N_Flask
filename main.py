from flask import Flask, render_template, request
from model import model
import this

this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.modelo = model()

pessoa = Flask(__name__)

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data     = request.form['tNovaData']
        this.dados    = this.modelo.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo="Página Principal", resultado=this.dados)

@pessoa.route('/consultar.html', methods=['GET','POST'])
def consultarTudo():
    if request.method == 'POST':
        this.codigo   = request.form['tNovoCodigo']
        this.msg = this.modelo.consultar(this.codigo)
    return render_template('consultar.html', titulo="Consultar", dados=this.msg)

@pessoa.route('/atualizar.html', methods=['GET','POST'])

def atualizarDado():
    if request.method == 'POST':
        this.codigo = request.form['tNovoCodigo']
        this.campo = request.form['tCampo']
        this.dado = request.form['tDado']
        this.msg = this.modelo.atualizar(this.codigo, this.campo, this.dado)
    return render_template('atualizar.html', titulo="Atualizar", dados=this.msg)

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)

