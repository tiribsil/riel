from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from utils import *

app = Flask(__name__)

registrador = Registrador()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar_exame', methods=['GET', 'POST'])
def registrar_exame():
    if request.method == 'POST':
        if registrador.registrar(int(request.form['id_exame']), request.form['cpf']):
            return render_template('inserido.html')
        else:
            return render_template('cpf_invalido.html')

    return render_template('registrar_exame.html', exames=exames, pacientes=pacientes)


@app.route('/chamar_paciente')
def chamar_paciente():
    registro_chamado = registrador.chamar_paciente()
    if registro_chamado:
        mensagem = f'Paciente {registro_chamado.get_paciente().get_cpf()} chamado.'
    else:
        mensagem = 'Fila de espera vazia!'

    return render_template('chamar_paciente.html', mensagem=mensagem)


@app.route('/dar_alta', methods=['GET', 'POST'])
def dar_alta():
    if request.method == 'POST':
        registrador.dar_alta(request.form['cpf'])

    return render_template('dar_alta.html')


@app.route('/quadro_geral')
def visualizar_todos():
    return render_template('quadro_geral.html',
                            quadro=registrador.exibir_quadro_geral())


@app.route('/fila_de_espera')
def visualizar_fila_espera():
    return render_template('fila_de_espera.html', fila_espera=registrador.exibir_fila_de_espera())

@app.route('/exames_em_coleta')
def visualizar_exames_em_coleta():
    return render_template('exames_em_coleta.html', em_coleta=registrador.exibir_exames_em_coleta())

@app.route('/exames_coletados')
def visualizar_exames_coletados():
    return render_template('exames_coletados.html', coletados=registrador.exibir_exames_coletados())

@app.route('/limpar')
def limpar():
    registrador.limpar()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)