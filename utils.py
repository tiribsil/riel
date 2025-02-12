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

class Registrador:
    def registrar(self, registro):
        if not isinstance(registro, RegistroExameLaboratorial): return False


exames = [
    ExameLaboratorial("Hemograma", "Análise de células sanguíneas"),
    ExameLaboratorial("Colesterol Total", "Medição do colesterol no sangue"),
    ExameLaboratorial("Glicemia", "Medição da glicose no sangue"),
    ExameLaboratorial("Urina Tipo I", "Análise física e química da urina"),
    ExameLaboratorial("TSH", "Teste de função tireoidiana"),
    ExameLaboratorial("Creatinina", "Avaliação da função renal"),
    ExameLaboratorial("TGO/AST", "Enzima hepática"),
    ExameLaboratorial("TGP/ALT", "Enzima hepática"),
    ExameLaboratorial("PCR", "Proteína C Reativa - marcador de inflamação"),
    ExameLaboratorial("Vitamina D", "Níveis de vitamina D no sangue")
]

pacientes = [
    Paciente("123.456.789-00", "João Silva", "15/03/1985"),
    Paciente("234.567.890-11", "Maria Oliveira", "22/07/1990"),
    Paciente("345.678.901-22", "Carlos Souza", "10/11/1978"),
    Paciente("456.789.012-33", "Ana Costa", "05/05/2000"),
    Paciente("567.890.123-44", "Pedro Santos", "18/09/1982"),
    Paciente("678.901.234-55", "Fernanda Lima", "30/01/1995"),
    Paciente("789.012.345-66", "Ricardo Pereira", "12/12/1970"),
    Paciente("890.123.456-77", "Juliana Alves", "25/06/1988"),
    Paciente("901.234.567-88", "Marcos Rocha", "14/08/1992"),
    Paciente("012.345.678-99", "Patrícia Gomes", "03/04/1980"),
    Paciente("111.222.333-44", "Lucas Martins", "19/10/2005"),
    Paciente("222.333.444-55", "Camila Ribeiro", "07/02/1998"),
    Paciente("333.444.555-66", "Gustavo Ferreira", "21/11/1975"),
    Paciente("444.555.666-77", "Amanda Barbosa", "09/07/1987"),
    Paciente("555.666.777-88", "Roberto Carvalho", "28/03/1993"),
    Paciente("666.777.888-99", "Tatiane Nunes", "16/05/1984"),
    Paciente("777.888.999-00", "Bruno Mendes", "23/09/1979"),
    Paciente("888.999.000-11", "Vanessa Castro", "01/12/1991"),
    Paciente("999.000.111-22", "Diego Araújo", "08/08/1986"),
    Paciente("000.111.222-33", "Larissa Cardoso", "27/02/2002")
]
