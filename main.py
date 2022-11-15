from Database.Conexion import Conexion


conec: Conexion = Conexion()
conec.conectar()
dataframe = conec.obtener_tabla()
dataframe.to_csv("data", index=False)
