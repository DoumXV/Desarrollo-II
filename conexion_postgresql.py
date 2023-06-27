import psycopg2


class DataBase:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="admin",
            database="Desarrollo II"

        )
        self.cursor = self.connection.cursor()
        print("Conexion Establecida")

    def seleccionar_usuario(self, id):
        sql = "SELECT idx, Nombre, Rut, Fono FROM public.agenda WHERE idx={}".format(
            id)
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            print(f" ID: {datos[0]}")
            print(f" Nombre: {datos[1]}")
            print(f" Rut: {datos[2]}")
            print(f" Fono: {datos[3]}")

        except Exception as ex:
            print(ex)

    def seleccionar_todos(self):
        sql = "SELECT * FROM agenda"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            for dato in datos:
                '''print(f" ID: {dato[0]}")
                print(f" Nombre: {dato[1]}")
                print(f" Rut: {dato[2]}")
                print(f" Fono: {dato[3]}")
                print(f"-------------\n")'''
                id = dato[0]
        except Exception as ex:
            print(ex)

    def actualizar_usuario(self, id, nombre):
        sql = 'UPDATE agenda SET Nombre = {} WHERE idx = {}'.format(
            nombre, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Datos Actualizados Correctamente")
        except Exception as ex:
            print(ex)

    def guardar_usuario(self, id, nombre, rut, fono):
        sql = 'INSERT INTO agenda VALUES ({},{},{},{})'.format(
            id, nombre, rut, fono)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Datos Guardados Correctamente")
        except Exception as ex:
            print(ex)

    def eliminar_usuario(self, id):
        sql = 'DELETE FROM agenda WHERE idx={}'.format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Usuario Eliminado Correcamente")
        except Exception as ex:
            print(ex)


# DB = DataBase()
# DB.seleccionar_usuario(5)
# DB.seleccionar_todos()
# DB.actualizar_usuario(4, "'jorgito'")
# DB.guardar_usuario(5,"'Pepe'",121518899,23232323)
# DB.eliminar_usuario(5)
