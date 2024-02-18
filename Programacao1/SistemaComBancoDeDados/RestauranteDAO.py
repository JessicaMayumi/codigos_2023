
import mysql.connector
from Restaurante import Restaurante
from ConnectionFactory import ConnectionFactory


class RestauranteDAO:
    conexao = ConnectionFactory().getConexao()

    def buscaRestaurante(self, id):
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM RESTAURANTE WHERE ID_RESTAURANTE = %s' 
            cursor.execute(sql, (id,))
            dados = cursor.fetchone()
            if dados:
                return Restaurante(nome=dados[1], endereco=dados[2], telefone=dados[3],cep=dados[4],nota=dados[5], id=dados[0],)
            else:
                return None
        except Exception as err:
            print (f"Erro ao buscar restaurante: {err}")

    def buscaRestauranteNome(self, nome):
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM RESTAURANTE WHERE NOME LIKE %s' 
            cursor.execute(sql, (nome,))
            dados = cursor.fetchone()
            if dados:
                return Restaurante(nome=dados[1], endereco=dados[2], telefone=dados[3],cep=dados[4],nota=dados[5], id=dados[0],)
            else:
                return None
        except Exception as err:
            print (f"Erro ao buscar restaurante: {err}")

    def buscaRestaurantes(self):
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM RESTAURANTE'
            cursor.execute(sql)
            dados = cursor.fetchall()
            restaurantes = []
            for i in dados:
                restaurante = Restaurante(nome=i[1], endereco=i[2], telefone=i[3], cep=i[4], nota=i[5], id=i[0],)
                restaurantes.append(restaurante)
            return restaurantes
        except Exception as err:
            print(f"Erro ao buscar restaurante: {err}")

    def insereRestaurante(self, restaurante):
        try:
            cursor = self.conexao.cursor()
            sql = 'INSERT INTO RESTAURANTE (NOME, ENDERECO, TELEFONE, CEP, NOTA) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(sql, (restaurante.nome, restaurante.endereco, restaurante.telefone, restaurante.cep, restaurante.nota,))
            self.conexao.commit()
            return True
        except Exception as err:
            print(f"Erro ao inserir restaurante: {err}")

    def alteraRestaurante(self, restaurante):
        try:
            cursor = self.conexao.cursor()
            sql = 'UPDATE RESTAURANTE SET NOME = %s, ENDERECO = %s, TELEFONE = %s, CEP = %s, NOTA = %s WHERE ID_RESTAURANTE = %s'
            cursor.execute(sql,  (restaurante.nome, restaurante.endereco, restaurante.telefone, restaurante.cep, restaurante.nota, restaurante.id,))
            self.conexao.commit()
            return True
        except Exception as err:
            print(f"Erro ao alterar restaurante: {err}")

    def apagarRestaurante(self, restaurante):
        try:
            cursor = self.conexao.cursor()
            sql = 'DELETE FROM RESTAURANTE WHERE ID_RESTAURANTE = %s'
            cursor.execute(sql, (restaurante.id,))
            self.conexao.commit()
            return True
        except Exception as err:
            print(f"Erro ao apagar restaurante: {err}")