import os
import pickle
import itertools
from datetime import datetime

class ExameLaboratorial:
    id_iter = itertools.count()

    def __init__(self, tipo, descricao):
        self.__id = next(self.id_iter)
        self._tipo = tipo
        self._descricao = descricao

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"Exame {self.__id} - Tipo: {self._tipo}, Descrição: {self._descricao}"

class Paciente:
    def __init__(self, cpf, nome, data_nascimento):
        self.__cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def get_cpf(self):
        return self.__cpf

    def __str__(self):
        return f"Paciente {self.__cpf} - Nome: {self._nome}, Data de Nascimento: {self._data_nascimento}"

class RegistroExameLaboratorial:
    id_iter = itertools.count()

    def __init__(self, exame, paciente, data_criacao):
        self.__id = next(self.id_iter)
        self.__exame = exame
        self.__paciente = paciente
        self.__data_criacao = data_criacao

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
