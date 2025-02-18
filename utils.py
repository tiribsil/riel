import os
import pickle
import itertools
from datetime import datetime
import mysql.connector

# colocar os dados para conectar ao BD aqui :)
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kashira",
    database="laboratorio"
)
db_cursor = db_connection.cursor()

class ExameLaboratorial:
    id_iter = itertools.count()

    def __init__(self, tipo, descricao):
        self.__id = next(self.id_iter)
        self._tipo = tipo
        self._descricao = descricao

    def get_id(self):
        return self.__id

    def get_tipo(self):
        return self._tipo

    def __str__(self):
        return f"Exame {self.__id} - Tipo: {self._tipo}, Descrição: {self._descricao}"

class Paciente:
    def __init__(self, cpf, nome, data_nascimento):
        self.__cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self._nome

    def __str__(self):
        return f"Paciente {self.__cpf} - Nome: {self._nome}, Data de Nascimento: {self._data_nascimento}"

class RegistroExameLaboratorial:
    if not os.path.exists('ultimo_id_registro.txt'):
        with open('ultimo_id_registro.txt', 'w') as f:
            f.write('0')
    with open('ultimo_id_registro.txt', 'r') as f:
        id_iter = itertools.count(start=int(f.read().strip()))

    def __init__(self, exame, paciente, data_criacao):
        self.__id = next(self.id_iter)
        with open('ultimo_id_registro.txt', 'w') as f:
            f.write(str(self.__id + 1))
        self.__exame = exame
        self.__paciente = paciente
        self.__data_criacao = data_criacao

    def get_paciente(self):
        return self.__paciente

    def __str__(self):
        return (f"Registro de Exame Laboratorial {self.__id}:\n"
                f"  - {self.__exame}\n"
                f"  - {self.__paciente}\n"
                f"  - Data de Criação: {self.__data_criacao}")

class FilaDeEspera:
    def __init__(self):
        self.__fila = []
        if not os.path.exists('backup_fila.bak'): self.__salvar()
        with open('backup_fila.bak', 'rb') as arquivo_backup:
            self.__fila = pickle.load(arquivo_backup)

    def inserir(self, registro):
        if not isinstance(registro, RegistroExameLaboratorial): return False
        self.__fila.append(registro)
        self.__salvar()
        return True

    def remover(self):
        if not self.__fila: return None
        registro_removido = self.__fila.pop(0)
        self.__salvar()
        return registro_removido

    def limpar(self):
        while self.__fila: self.remover()

    def __salvar(self):
        with open('backup_fila.bak', 'wb') as arquivo_backup:
            pickle.dump(self.__fila, arquivo_backup)

    def __str__(self):
        if not self.__fila:
            return "Fila de espera vazia."
        return "\n".join(str(registro) for registro in self.__fila)

    def __len__(self):
        return len(self.__fila)

class ExamesEmColeta:
    def __init__(self):
        self.__lista = []
        if not os.path.exists('backup_lista.bak'): self.__salvar()
        with open('backup_lista.bak', 'rb') as arquivo_backup:
            self.__lista = pickle.load(arquivo_backup)

    def __salvar(self):
        with open('backup_lista.bak', 'wb') as arquivo_backup:
            pickle.dump(self.__lista, arquivo_backup)

    def inserir(self, registro):
        if not isinstance(registro, RegistroExameLaboratorial): return False
        self.__lista.append(registro)
        self.__salvar()
        return True

    def remover(self, cpf):
        if not self.__lista: return None

        indice = -1
        for i, registro in enumerate(self.__lista):
            paciente = registro.get_paciente()
            if paciente.get_cpf() == cpf:
                indice = i
                break

        if indice == -1: return False
        registro_removido = self.__lista.pop(indice)
        self.__salvar()
        return registro_removido

    def limpar(self):
        while self.__lista: self.__lista.pop(0)
        self.__salvar()

    def __str__(self):
        if not self.__lista:
            return "Nenhum exame em coleta."
        return "\n".join(str(registro) for registro in self.__lista)

    def __len__(self):
        return len(self.__lista)

class ExamesColetados:
    def __init__(self):
        self.__arquivo_historico = 'arquivo_historico.hist'

    def inserir(self, registro):
        if not isinstance(registro, RegistroExameLaboratorial): return False
        with open(self.__arquivo_historico, 'a') as arquivo:
            arquivo.write(str(registro))
            arquivo.close()
        return True

    def limpar(self):
        with open(self.__arquivo_historico, 'w'):
            pass

    def __str__(self):
        if not os.path.exists(self.__arquivo_historico):
            return "Nenhum exame registrado."

        with open(self.__arquivo_historico, 'r+') as arquivo:
            conteudo = arquivo.read()
            if len(conteudo) == 0:
                arquivo.close()
                return "Nenhum exame registrado."
            else:
                arquivo.close()
                return conteudo


class Registrador:
    def __init__(self):
        self.__fila = FilaDeEspera()
        self.__em_coleta = ExamesEmColeta()
        self.__coletados = ExamesColetados()

    def limpar(self):
        self.__fila.limpar()
        self.__em_coleta.limpar()
        self.__coletados.limpar()

    def registrar(self, id_exame, cpf_paciente):
        db_cursor.execute("SELECT * FROM pacientes WHERE cpf = %s", (cpf_paciente,))
        paciente_data = db_cursor.fetchone()
        if not paciente_data:
            return False
        paciente = Paciente(*paciente_data)

        db_cursor.execute("SELECT * FROM exames WHERE id = %s", (id_exame,))
        exame_data = db_cursor.fetchone()
        if not exame_data:
            return False
        exame = ExameLaboratorial(*exame_data[1:])
        exame._ExameLaboratorial__id = exame_data[0]

        registro = RegistroExameLaboratorial(exame, paciente, datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.__fila.inserir(registro)
        return True

    def chamar_paciente(self):
        registro_chamado = self.__fila.remover()
        if self.__em_coleta.inserir(registro_chamado): return registro_chamado
        else: return False

    def dar_alta(self, cpf):
        registro_alta = self.__em_coleta.remover(cpf)
        if self.__coletados.inserir(registro_alta): return registro_alta
        else: return False

    def exibir_fila_de_espera(self):
        return str(self.__fila)

    def exibir_exames_coletados(self):
        return str(self.__coletados)

    def exibir_exames_em_coleta(self):
        return str(self.__em_coleta)

    def exibir_quadro_geral(self):
        return 'Fila de Espera\n' + str(self.__fila) + '\n\nExames em Coleta\n' + str(self.__em_coleta) + '\n\nExames Coletados\n' + str(self.__coletados)

