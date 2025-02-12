from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from utils import *

app = Flask(__name__)

fila_de_espera = FilaDeEspera()
#exames_em_coleta = ExamesEmColeta()
#exames_coletados = ExamesColetados()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar_exame', methods=['GET', 'POST'])
def registrar_exame():
    if request.method == 'POST':
        id_exame = request.form['id_exame']
        cpf_paciente = request.form['cpf_paciente']

        registro = RegistroExameLaboratorial(id_exame, cpf_paciente, datetime.now())

        fila_de_espera.inserir(registro)

        return redirect(url_for('index'))
    return render_template('registrar_exame.html')


@app.route('/chamar_paciente')
# def chamar_paciente():
#     registro_removido = fila_de_espera.remover()
#
#     if registro_removido:
#         exames_em_coleta.inserir(registro_removido)
#         mensagem = f"Paciente {registro_removido.cpf_paciente} chamado para o exame {registro_removido.id_exame}."
#     else:
#         mensagem = "Não há pacientes na fila de espera."
#
#     return render_template('chamar_paciente.html', mensagem=mensagem)


@app.route('/dar_alta')
# def dar_alta():
    # registro_removido = exames_em_coleta.remover()
    #
    # if registro_removido:
    #     exames_coletados.inserir(registro_removido)
    #     mensagem = f"Exame {registro_removido.id_exame} do paciente {registro_removido.cpf_paciente} finalizado."
    # else:
    #     mensagem = "Não há exames em coleta."
    #
    # return render_template('dar_alta.html', mensagem=mensagem)


@app.route('/quadro_geral')
# def visualizar_todos():
    # registros_fila_espera = fila_de_espera.obter_todos()
    # registros_em_coleta = exames_em_coleta.obter_todos()
    # registros_coletados = exames_coletados.obter_todos()
    #
    # return render_template('visualizar_todos.html',
    #                        fila_espera=registros_fila_espera,
    #                        em_coleta=registros_em_coleta,
    #                        coletados=registros_coletados)


@app.route('/fila_de_espera')
def visualizar_fila_espera():
    registros_fila_espera = str(fila_de_espera)
    return render_template('fila_de_espera.html', fila_espera=registros_fila_espera)


@app.route('/exames_em_coleta')
# def visualizar_exames_em_coleta():
#     registros_em_coleta = exames_em_coleta.obter_todos()
#     return render_template('visualizar_exames_em_coleta.html', em_coleta=registros_em_coleta)


@app.route('/exames_coletados')
def visualizar_exames_coletados():
    registros_coletados = 'str(exames_coletados)'
    return render_template('exames_coletados.html', coletados=registros_coletados)


if __name__ == '__main__':
    app.run(debug=True)