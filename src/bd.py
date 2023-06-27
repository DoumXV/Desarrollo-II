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


class Medico(DataBase):
    def __str__(self):
        datos = self.seleccionar_todos()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def seleccionar_usuario(self, id):
        sql = "SELECT * FROM medico WHERE id = {}".format(id)
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        return datos

    def seleccionar_todos(self):
        sql = "SELECT * FROM medico"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def actualizar_usuario(self, id, nombre, rut, fecha, prevision, profesion, sueldo, especialidad):
        sql = '''UPDATE medico SET nombre = '{}', rut = '{}', fecha = '{}', prevision='{}',profesion ='{}',sueldo ={},especialidad='{}' WHERE id='{}' '''.format(
            nombre, rut, fecha, prevision, profesion, sueldo, especialidad, id)
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Actualizados Correctamente")
        except Exception as ex:
            print(ex)
        return n

    def guardar_usuario(self, nombre, rut, fecha, prevision, profesion, sueldo, especialidad):
        sql = '''INSERT INTO medico (nombre,rut,fecha,prevision,profesion,sueldo,especialidad) VALUES ('{}','{}','{}','{}','{}',{},'{}')'''.format(
            nombre, rut, fecha, prevision, profesion, sueldo, especialidad)
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
        except Exception as ex:
            print(ex)
        return n

    def eliminar_usuario(self, id):
        sql = 'DELETE FROM medico WHERE id={}'.format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Usuario Eliminado Correcamente")
            n = self.cursor.rowcount
        except Exception as ex:
            print(ex)
        return n


class Personal(DataBase):

    def __str__(self):
        datos = self.seleccionar_todos()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def seleccionar_usuario(self, id):
        sql = "SELECT * FROM personal WHERE id = {}".format(id)
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        return datos

    def seleccionar_todos(self):
        sql = "SELECT * FROM personal"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def actualizar_usuario(self, id, nombre, rut, fecha, prevision, sueldo, unidad, cargo):
        sql = '''UPDATE personal SET nombre = '{}', rut = '{}', fecha = '{}', prevision='{}',sueldo ={},unidad ='{}',cargo='{}' WHERE id='{}' '''.format(
            nombre, rut, fecha, prevision, sueldo, unidad, cargo, id)
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Actualizados Correctamente")
        except Exception as ex:
            print(ex)
        return n

    def guardar_usuario(self, nombre, rut, fecha, prevision, sueldo, unidad, cargo):
        sql = '''INSERT INTO personal (nombre,rut,fecha,prevision,sueldo,unidad,cargo) VALUES ('{}','{}','{}','{}',{},'{}','{}')'''.format(
            nombre, rut, fecha, prevision, sueldo, unidad, cargo)
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
        except Exception as ex:
            print(ex)
        return n

    def eliminar_usuario(self, id):
        sql = 'DELETE FROM personal WHERE id={}'.format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Usuario Eliminado Correcamente")
            n = self.cursor.rowcount
        except Exception as ex:
            print(ex)
        return n


class Paciente(DataBase):
    def __str__(self):
        datos = self.seleccionar_todos()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def seleccionar_usuario(self, id):
        sql = "SELECT * FROM paciente WHERE id = {}".format(id)
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        return datos

    def seleccionar_todos(self):
        sql = "SELECT * FROM paciente"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def actualizar_usuario(self, id, nombre, rut, fecha, prevision, motivo, derivacion, medico, especialidadmedico, boxurgencia):
        sql = '''UPDATE paciente SET nombre = '{}', rut = '{}', fecha = '{}', prevision='{}',motivo ='{}',derivacion ='{}',medico='{}', especialidadmedico='{}',boxurgencia={} WHERE id='{}' '''.format(
            nombre, rut, fecha, prevision, motivo, derivacion, medico, especialidadmedico, boxurgencia, id)
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Actualizados Correctamente")
        except Exception as ex:
            print(ex)
        return n

    def guardar_usuario(self, nombre, rut, fecha, prevision, motivo, derivacion, medico, especialidadmedico, boxurgencia):
        sql = '''INSERT INTO paciente (nombre, rut, fecha, prevision, motivo, derivacion, medico, especialidadmedico, boxurgencia) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}',{})'''.format(
            nombre, rut, fecha, prevision, motivo, derivacion, medico, especialidadmedico, boxurgencia)
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
        except Exception as ex:
            print(ex)
        return n

    def eliminar_usuario(self, id):
        sql = 'DELETE FROM paciente WHERE id={}'.format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Usuario Eliminado Correcamente")
            n = self.cursor.rowcount
        except Exception as ex:
            print(ex)
        return n
