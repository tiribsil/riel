import os
import pickle
import itertools
from datetime import datetime

from tenacity import retry_if_exception_message


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

    def get_exame(self):
        return self.__exame

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
        try: paciente = next(p for p in pacientes if p.get_cpf() == cpf_paciente)
        except StopIteration: return False
        exame = next(e for e in exames if e.get_id() == id_exame)

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

