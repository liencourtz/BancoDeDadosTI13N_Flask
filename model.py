import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
        
    def inserir(self, nome, telefone, endereco, dataDeNascimento):
        try:
            sql = "Insert into person(codigo, nome, telefone, endereco, dataDeNascimento) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def consultar(self, codigo):
        try:
            sql = "select * from person where codigo ='{}'".format(codigo)
            self.con.execute(sql)
            msg = ""
            
            for(codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg = msg + "\nCódigo: {}, Nome: {}, Telefone: {}, Endereço: {}, Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg
        except Exception as erro:
            return erro
        
    def atualizar(self, cod, campo, novoDado):
        try:
            sql = "update person set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def excluir(self, cod):
        try:
            sql = "delete from person where codigo = '{}'".format(cod)
            self.con.execute(cod)
            self.db_connection.commit()
            return "{} linha excluida!".format(cod) 
        except Exception as erro:
            return erro
        
    def tratarData(self, texto):
        separado = texto.split("/")
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)