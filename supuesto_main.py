from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import psycopg2


class DataBase:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="oketo2002.",
            database="Desarrollo II"

        )
        self.cursor = self.connection.cursor()
        print("Conexion Establecida")

    def seleccionar_usuario(self, val):
        sql = 'SELECT * FROM hospital WHERE id={}'.format(val)
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            if datos:
                tree.insert("", END, val, values=datos)  # Eliminar 'text=id'
        except Exception as ex:
            print(ex)

    def seleccionar_todos(self):
        sql = "SELECT * FROM hospital"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            for dato in datos:
                id = dato[0]
                tree.insert("", END, id, values=dato)  # Eliminar 'text=id'
        except Exception as ex:
            print(ex)

    def actualizar_usuario(self, val):
        id = tree.selection()[0]
        sql = 'UPDATE hospital SET nombre = %s, rut = %s, fono = %s WHERE id='+id
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
            print("Datos Actualizados Correctamente")
        except Exception as ex:
            print(ex)

    def guardar_usuario(self, val):
        sql = 'INSERT INTO hospital (nombre,rut,fono) VALUES (%s,%s,%s)'
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
            print("Datos Guardados Correctamente")
        except Exception as ex:
            print(ex)

    def eliminar_usuario(self, id):
        sql = 'DELETE FROM hospital WHERE id={}'.format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Usuario Eliminado Correcamente")
        except Exception as ex:
            print(ex)


# ------------Se conecta a la base de datos---------#
DB = DataBase()
modificar = False
# ------------FUNCIONES-------------#


def seleccionar(event):
    if tree.selection():
        id = tree.selection()[0]
        if int(id) > 0:
            Nombre.set(tree.item(id, "values")[1])
            Rut.set(tree.item(id, "values")[2])
            Fono.set(tree.item(id, "values")[3])


def modificarFalse():
    global modificar
    modificar = False
    tree.config(selectmode=NONE)
    btnGuardar.config(text="Guardar")
    btnModificar.config(text="Seleccionar")
    btnEliminar.config(state=DISABLED)


def modificarTrue():
    global modificar
    modificar = True
    tree.config(selectmode=BROWSE)
    btnGuardar.config(text="Nuevo")
    btnModificar.config(text="Modificar")
    btnEliminar.config(state=NORMAL)


def validar():
    return len(Nombre.get()) and len(Rut.get()) and len(Fono.get())


def validarid():
    return len(Id.get())


def limpiar():
    Id.set("")
    Nombre.set("")
    Rut.set("")
    Fono.set("")


def vaciar_tabla():
    datos = tree.get_children()
    for dato in datos:
        tree.delete(dato)


def llenar_tabla():
    vaciar_tabla()
    DB.seleccionar_todos()


def buscar():
    if modificar == False:
        if validarid():
            vaciar_tabla()
            val = (Id.get())
            DB.seleccionar_usuario(val)
        else:
            txtMensaje.config(
                text="El campo no debe estar vacio", fg="red")


def eliminar():
    if tree.selection():
        id = tree.selection()[0]
        DB.eliminar_usuario(id)
        tree.delete(id)
        txtMensaje.config(text="Se ha eliminado el registro correctamente")
        limpiar()
        llenar_tabla()
    else:
        txtMensaje.config(text="Seleccione un registro para eliminar")


def guardar():
    if modificar == False:
        if validar():
            val = (Nombre.get(), Rut.get(), Fono.get())
            DB.guardar_usuario(val)
            txtMensaje.config(text="Se ha guardado el registro correctamente")
            llenar_tabla()
            limpiar()
        else:
            txtMensaje.config(
                text="Los campos no deben estar vacios", fg="red")
    else:
        modificarFalse()


def actualizar():
    if modificar == True:
        if validar():
            val = (Nombre.get(), Rut.get(), Fono.get())
            DB.actualizar_usuario(val)
            txtMensaje.config(
                text="Se ha actualizado el registro correctamente")
            llenar_tabla()
            limpiar()
        else:
            txtMensaje.config(
                text="Los campos no deben estar vacios", fg="red")
    else:
        modificarTrue()


def mostrar():
    pass


# ----------------TKINTER------------#
ventana = Tk()
ventana.title(
    "Sistema de Gestión Administrativa - Hospital Regional Copiapó")
ventana.geometry("800x600")

Id = StringVar()
Nombre = StringVar()
Rut = StringVar()
Fono = StringVar()

# ----------------Tabla----------------#
tree = ttk.Treeview(height=10, columns=(
    "#0", "#1", "#2", "#3"), selectmode=NONE)
tree.place(x=100, y=180)
tree.column("#1", width=50)
tree.heading("#1", text="ID", anchor=W)
tree.column("#2", width=100)
tree.heading("#2", text="Nombre", anchor=W)
tree.column("#3", width=100)
tree.heading("#3", text="RUT", anchor=W)
tree.column("#4", width=100)
tree.heading("#4", text="Fono", anchor=W)
tree.bind("<<TreeviewSelect>>", seleccionar)
tree.config(show="headings")  # Ocultar la columna vacia

# -------------INPUTS------------#
txtMensaje = Label(ventana, text="",
                   fg="green")
txtMensaje.place(x=300, y=30)


e1 = Entry(ventana, textvariable=Id, width=5)
e1.place(x=300, y=125)

lnombre = Label(ventana, text="Nombre:")
lnombre.place(x=45, y=35)
etNombre = Entry(ventana, textvariable=Nombre, width=20)
etNombre.place(x=100, y=35)

lnombre = Label(ventana, text="Rut:")
lnombre.place(x=45, y=60)
etNombre = Entry(ventana, textvariable=Rut, width=20)
etNombre.place(x=100, y=60)

lnombre = Label(ventana, text="Fono:")
lnombre.place(x=45, y=85)
etNombre = Entry(ventana, textvariable=Fono, width=20)
etNombre.place(x=100, y=85)


# etNombre = Entry(ventana, textvariable=Id, width=30)
# etNombre.place(x=270, y=120)

# --------------BOTONES-----------#
btnGuardar = Button(ventana, text="Nuevo", command=guardar)
btnGuardar.place(x=50, y=120)

btnModificar = Button(ventana, text="Seleccionar", command=actualizar)
btnModificar.place(x=110, y=120)

btnEliminar = Button(ventana, text="Eliminar", command=eliminar)
btnEliminar.place(x=190, y=120)

btnBuscar = Button(ventana, text="Buscar", command=buscar)
btnBuscar.place(x=250, y=120)

boton_personal_medico = Button(
    ventana, text="Gestionar Personal Médico", command="")
boton_personal_medico.place(x=500, y=35)

boton_personal_administrativo = Button(
    ventana, text="Gestionar Personal Administrativo", command="")
boton_personal_administrativo.place(x=500, y=65)

# --------------BARRA---------#
"""Barramenu = Menu(ventana)
menu = Menu(Barramenu, tearoff=0)
menu.add_command(label="Limpiar Datos", command="")
menu.add_command(label="Salir", command="")
Barramenu.add_cascade(label="Config", menu=menu)
ventana.config(menu=Barramenu)
llenar_tabla()

ventana.mainloop()"""
