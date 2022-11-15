import mysql.connector
import pandas as pd
from mysql.connector import Error


class Conexion:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'Tr4c30n'
        self.database = 'bdblog'
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print('Conexión exitosa!')
                self.cursor = self.connection.cursor()
        except Error as e:
            print('Error al conectarse con MySQL', e)

    def obtener_tabla(self):
        if self.connection.is_connected():
            query = """select a.Titulo, a.fechacreacion as 'Fecha_de_creacion', c.Categoria from bdblog.articulo a
inner join bdblog.categoria c on a.Categoria_id = c.id"""
            self.cursor.execute(query)
            row = self.cursor.fetchall()
            titulos_col = ["Titulo", "Fecha de Creacion", "Categoría"]
            df = pd.DataFrame(row, columns=titulos_col)
            print(df)
            return df
