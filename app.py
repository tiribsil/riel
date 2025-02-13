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
       if registrador.registrar(int(request.form['id_exame']), request.form['cpf']): return render_template('inserido.html')
       else: return render_template('cpf_invalido.html')


   return render_template('registrar_exame.html', exames=exames, pacientes=pacientes)




@app.route('/chamar_paciente')
def chamar_paciente():
   registro_removido = registrador.remover_fila_espera()


   if registro_removido:
       registrador.inserir_exame_em_coleta(registro_removido)
       mensagem = f"Paciente {registro_removido.get_paciente().get_cpf()} chamado para o exame {registro_removido.get_exame()}."
   else:
       mensagem = "Não há pacientes na fila de espera."


   return render_template('chamar_paciente.html', mensagem=mensagem, patient=registro_removido)




# @app.route('/dar_alta', methods=['GET', 'POST'])
# def dar_alta():
#     if request.method == 'POST':
#         cpf = request.form['cpf']
#         print(f"CPF recebido: {cpf}")
#
#         registro_removido = registrador.dar_alta(cpf=cpf)
#
#         if registro_removido:
#             mensagem = f"Exame {registro_removido.id_exame} do paciente {registro_removido.cpf_paciente} finalizado."
#         else:
#             mensagem = "Não há exames em coleta."
#
#         return render_template('dar_alta.html', mensagem=mensagem)
#
#     return render_template('dar_alta.html')


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
   return render_template('fila_de_espera.html', fila_espera=registrador.exibir_fila_de_espera())


@app.route('/exames_em_coleta')
def visualizar_exames_em_coleta():
   return render_template('visualizar_exames_em_coleta.html', em_coleta=registrador.exibir_exames_em_coleta())


@app.route('/exames_coletados')
def visualizar_exames_coletados():
   return render_template('exames_coletados.html', coletados=registrador.exibir_exames_coletados())


@app.route('/limpar')
def limpar():
   registrador.limpar()
   return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True)

