import unittest

from utils import *

class TestFilaDeEspera(unittest.TestCase):
    def setUp(self):
        self.fila = FilaDeEspera()
        self.exames = [
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

        self.pacientes = [
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

        self.registros = [
            RegistroExameLaboratorial(self.exames[5], self.pacientes[1], '02/01/1903 19:30:00'),
            RegistroExameLaboratorial(self.exames[0], self.pacientes[12], '03/02/2023 08:15:00'),
            RegistroExameLaboratorial(self.exames[1], self.pacientes[9], '04/03/2023 09:20:00'),
            RegistroExameLaboratorial(self.exames[2], self.pacientes[4], '05/04/2023 10:25:00'),
            RegistroExameLaboratorial(self.exames[3], self.pacientes[15], '06/05/2023 11:30:00'),
            RegistroExameLaboratorial(self.exames[4], self.pacientes[6], '07/06/2023 12:35:00'),
            RegistroExameLaboratorial(self.exames[6], self.pacientes[2], '08/07/2023 13:40:00'),
            RegistroExameLaboratorial(self.exames[7], self.pacientes[0], '09/08/2023 14:45:00'),
            RegistroExameLaboratorial(self.exames[8], self.pacientes[8], '10/09/2023 15:50:00'),
            RegistroExameLaboratorial(self.exames[9], self.pacientes[10], '11/10/2023 16:55:00')
        ]

    def tearDown(self):
        if os.path.exists('backup_fila.bak'):
            os.remove('backup_fila.bak')

    def test_inserir_registro_fila_vazia(self):
        self.assertTrue(self.fila.inserir(self.registros[1]))
        self.assertEqual(str(self.fila), str(self.registros[1]))
        self.assertTrue(self.fila.inserir(self.registros[4]))
        self.assertEqual(str(self.fila), str(self.registros[1]) + '\n' + str(self.registros[4]))

    def test_remover_registro(self):
        self.fila.inserir(self.registros[5])
        self.fila.inserir(self.registros[7])
        self.assertEqual(self.fila.remover(), self.registros[5])
        self.assertEqual(len(self.fila), 1)

    def test_remover_de_fila_vazia(self):
        registro_removido = self.fila.remover()
        self.assertIsNone(registro_removido)

    def test_carregar_fila(self):
        self.fila.inserir(self.registros[5])
        nova_fila = FilaDeEspera()
        self.assertEqual(len(nova_fila), 1)
        self.assertEqual(str(nova_fila.remover()), str(self.registros[5]))


class TestExamesColetados(unittest.TestCase):
    def setUp(self):
        self.exames_coletados = ExamesColetados()

        self.exames = [
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

        self.pacientes = [
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

        self.registros = [
            RegistroExameLaboratorial(self.exames[5], self.pacientes[1], '02/01/1903 19:30:00'),
            RegistroExameLaboratorial(self.exames[0], self.pacientes[12], '03/02/2023 08:15:00'),
            RegistroExameLaboratorial(self.exames[1], self.pacientes[9], '04/03/2023 09:20:00'),
            RegistroExameLaboratorial(self.exames[2], self.pacientes[4], '05/04/2023 10:25:00'),
            RegistroExameLaboratorial(self.exames[3], self.pacientes[15], '06/05/2023 11:30:00'),
            RegistroExameLaboratorial(self.exames[4], self.pacientes[6], '07/06/2023 12:35:00'),
            RegistroExameLaboratorial(self.exames[6], self.pacientes[2], '08/07/2023 13:40:00'),
            RegistroExameLaboratorial(self.exames[7], self.pacientes[0], '09/08/2023 14:45:00'),
            RegistroExameLaboratorial(self.exames[8], self.pacientes[8], '10/09/2023 15:50:00'),
            RegistroExameLaboratorial(self.exames[9], self.pacientes[10], '11/10/2023 16:55:00')
        ]

    def tearDown(self):
        if os.path.exists('arquivo_historico.hist'):
            os.remove('arquivo_historico.hist')

    def test_inserir_registro(self):
        self.assertTrue(self.exames_coletados.inserir(self.registros[0]))
        self.assertTrue(self.exames_coletados.inserir(self.registros[1]))
        self.assertTrue(self.exames_coletados.inserir(self.registros[2]))
        self.assertEqual(str(self.exames_coletados), str(self.registros[0]) + str(self.registros[1]) + str(self.registros[2]))

    def test_inserir_registro_invalido(self):
        registro_invalido = "Isso definitivamente não é um registro"
        self.assertFalse(self.exames_coletados.inserir(registro_invalido))
        self.assertEqual(str(self.exames_coletados), "Nenhum exame registrado.")

    def test_limpar_historico(self):
        self.exames_coletados.inserir(self.registros[2])
        self.exames_coletados.inserir(self.registros[3])
        self.exames_coletados.limpar()
        self.assertEqual(str(self.exames_coletados), "Nenhum exame registrado.")

    def test_persistencia_dados(self):
        self.exames_coletados.inserir(self.registros[4])
        self.exames_coletados.inserir(self.registros[5])

        novos_exames = ExamesColetados()

        self.assertEqual(str(novos_exames), str(self.registros[4]) + str(self.registros[5]))

    def test_exibir_arquivo_vazio(self):
        if os.path.exists('arquivo_historico.hist'):
            os.remove('arquivo_historico.hist')

        novos_exames = ExamesColetados()
        self.assertEqual(str(novos_exames), "Nenhum exame registrado.")

if __name__ == '__main__':
    unittest.main()



