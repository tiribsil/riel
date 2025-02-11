class ExameLaboratorial:
    def __init__(self, id, tipo, descricao):
        self.__id = id
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

