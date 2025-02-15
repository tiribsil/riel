CREATE TABLE pacientes (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE exames (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL
);

INSERT INTO pacientes (cpf, nome, data_nascimento) VALUES
('123.456.789-00', 'João Silva', '1985-03-15'),
('234.567.890-11', 'Maria Oliveira', '1990-07-22'),
('345.678.901-22', 'Carlos Souza', '1978-11-10'),
('456.789.012-33', 'Ana Costa', '2000-05-05'),
('567.890.123-44', 'Pedro Santos', '1982-09-18'),
('678.901.234-55', 'Fernanda Lima', '1995-01-30'),
('789.012.345-66', 'Ricardo Pereira', '1970-12-12'),
('890.123.456-77', 'Juliana Alves', '1988-06-25'),
('901.234.567-88', 'Marcos Rocha', '1992-08-14'),
('012.345.678-99', 'Patrícia Gomes', '1980-04-03'),
('111.222.333-44', 'Lucas Martins', '2005-10-19'),
('222.333.444-55', 'Camila Ribeiro', '1998-02-07'),
('333.444.555-66', 'Gustavo Ferreira', '1975-11-21'),
('444.555.666-77', 'Amanda Barbosa', '1987-07-09'),
('555.666.777-88', 'Roberto Carvalho', '1993-03-28'),
('666.777.888-99', 'Tatiane Nunes', '1984-05-16'),
('777.888.999-00', 'Bruno Mendes', '1979-09-23'),
('888.999.000-11', 'Vanessa Castro', '1991-12-01'),
('999.000.111-22', 'Diego Araújo', '1986-08-08'),
('000.111.222-33', 'Larissa Cardoso', '2002-02-27');

INSERT INTO exames (tipo, descricao) VALUES
('Hemograma', 'Análise de células sanguíneas'),
('Colesterol Total', 'Medição do colesterol no sangue'),
('Glicemia', 'Medição da glicose no sangue'),
('Urina Tipo I', 'Análise física e química da urina'),
('TSH', 'Teste de função tireoidiana'),
('Creatinina', 'Avaliação da função renal'),
('TGO/AST', 'Enzima hepática'),
('TGP/ALT', 'Enzima hepática'),
('PCR', 'Proteína C Reativa - marcador de inflamação'),
('Vitamina D', 'Níveis de vitamina D no sangue');