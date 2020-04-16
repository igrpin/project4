import psycopg2


class Conexao:
    def __init__(self):
        self.conexao = psycopg2.connect(dbname='project4', user="postgres", password="postgres")
        print('Conexão estabelecida')
        self.cursor = self.conexao.cursor()


    def __del__(self):
        self.cursor.close()
        self.conexao.close()
        print('Conexão encerrada')