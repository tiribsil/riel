import itertools

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