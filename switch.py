import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from src.bd import DataBase


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Ventana):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font="Verdana")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1 ",
                            command=lambda: controller.show_frame(Ventana))
        button1.pack()


class Ventana(Frame):
    hospital = DataBase()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatos()
        self.habilitarCajas("disabled")
        self.habilitarBtnIzq("normal")
        self.habilitarBtnDer("disabled")
        self.id = -1

    def llenarDatos(self):
        datos = self.hospital.seleccionar_todos()
        for dato in datos:
            self.tree.insert("", END, text=dato[0], values=(
                dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))

    def limpiarTree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def habilitarBtnIzq(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnDer(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def habilitarCajas(self, estado):
        self.txtEspecialidad.configure(state=estado)
        self.txtFecha.configure(state=estado)
        self.txtNombre.configure(state=estado)
        self.txtPrevision.configure(state=estado)
        self.txtProfesion.configure(state=estado)
        self.txtRut.configure(state=estado)
        self.txtSueldo.configure(state=estado)

    def limpiarCajas(self):
        self.txtEspecialidad.delete(0, END)
        self.txtFecha.delete(0, END)
        self.txtNombre.delete(0, END)
        self.txtPrevision.delete(0, END)
        self.txtProfesion.delete(0, END)
        self.txtRut.delete(0, END)
        self.txtSueldo.delete(0, END)

    def Nuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBtnIzq("disabled")
        self.habilitarBtnDer("normal")
        self.limpiarCajas()
        self.txtNombre.focus()

    def Modificar(self):
        selected = self.tree.focus()
        clave = self.tree.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Modificar", "Debes seleccionar un Elemento")
        else:
            self.id = clave
            self.habilitarCajas("normal")
            valores = self.tree.item(selected, 'values')
            self.limpiarCajas()
            self.txtNombre.insert(0, valores[0])
            self.txtRut.insert(0, valores[1])
            self.txtFecha.insert(0, valores[2])
            self.txtPrevision.insert(0, valores[3])
            self.txtProfesion.insert(0, valores[4])
            self.txtSueldo.insert(0, valores[5])
            self.txtEspecialidad.insert(0, valores[6])
            self.habilitarBtnIzq("disabled")
            self.habilitarBtnDer("normal")
            self.txtNombre.focus()

    def Eliminar(self):
        selected = self.tree.focus()
        clave = self.tree.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Eliminar", "Debes seleccionar un Elemento")
        else:
            r = messagebox.askquestion(
                "Eliminar", "Desea eliminar el registro seleccionado?")
            if r == messagebox.YES:
                n = self.hospital.eliminar_usuario(clave)
                if n == 1:
                    messagebox.showinfo(
                        "Eliminar", "Elemento eliminado correctamente")
                    self.limpiarTree()
                    self.llenarDatos()
                else:
                    messagebox.showinfo(
                        "Eliminar", "No fue posible eliminar el elemento")
            else:
                pass

    def Guardar(self):
        if self.id == -1:
            n = self.hospital.guardar_usuario(self.txtNombre.get(), self.txtRut.get(), self.txtFecha.get(
            ), self.txtPrevision.get(), self.txtProfesion.get(), self.txtSueldo.get(), self.txtEspecialidad.get())
            if n == 1:
                messagebox.showinfo(
                    "Guardar", "Elemento Registrado correctamente")
            else:
                messagebox.showinfo(
                    "Guardar", "No fue posible eliminar el elemento")
        else:
            n = self.hospital.actualizar_usuario(self.id, self.txtNombre.get(), self.txtRut.get(), self.txtFecha.get(
            ), self.txtPrevision.get(), self.txtProfesion.get(), self.txtSueldo.get(), self.txtEspecialidad.get())
            self.id = -1
            if n == 1:
                messagebox.showinfo(
                    "Modificar", "Elemento Modificado correctamente")
            else:
                messagebox.showinfo(
                    "Modificar", "No fue posible modificar el elemento")

        self.limpiarTree()
        self.llenarDatos()
        self.limpiarCajas()
        self.habilitarBtnDer("disabled")
        self.habilitarBtnIzq("normal")

    def Cancelar(self):
        r = messagebox.askquestion(
            "Cancelar", "Esta seguro que desea cancelar la operacion actual")
        if r == messagebox.YES:
            self.limpiarCajas()
            self.habilitarBtnDer("disabled")
            self.habilitarBtnIzq("normal")
            self.habilitarCajas("disabled")

    def mostrar_frame(self, frame):
        if self.frame_actual:
            self.frame_actual.pack_forget()  # Ocultar el frame actualmente visible

        frame.pack()  # Mostrar el nuevo frame
        self.frame_actual = frame  # Actualizar el frame actualmente visible

    def create_widgets(self):
        frame1 = Frame(self, bg="gray74")
        frame1.place(x=0, y=0, width=93, height=600)

        frame2 = Frame(self, bg="lavender")
        frame2.place(x=95, y=0, width=400, height=220)

        frame3 = Frame(self, bg="yellow")
        frame3.place(x=96, y=223, width=800, height=399)

        frame4 = Frame(self, bg="lavender")
        frame4.place(x=500, y=0, width=400, height=220)

        frame5 = Frame(self, bg="blue")  # Ejemplo de un nuevo frame
        frame5.place(x=700, y=0, width=400, height=220)

        frame6 = Frame(self, bg="red")  # Ejemplo de otro nuevo frame
        frame6.place(x=700, y=223, width=400, height=399)

        self.btnNuevo = Button(frame1, text="Nuevo",
                               command=self.Nuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnModificar = Button(frame1, text="Modificar",
                                   command=self.Modificar, bg="blue", fg="white")
        self.btnModificar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar = Button(frame1, text="Eliminar",
                                  command=self.Eliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)

        self.btnGuardar = Button(frame2, text="Guardar",
                                 command=self.Guardar, bg="green", fg="white")
        self.btnGuardar.place(x=70, y=180, width=80, height=30)

        self.btnCancelar = Button(frame2, text="Cancelar",
                                  command=self.Cancelar, bg="red", fg="white")
        self.btnCancelar.place(x=170, y=180, width=80, height=30)

        self.btnMostrarFrame5 = Button(
            frame1, text="Mostrar Frame 5", command="")
        self.btnMostrarFrame5.place(x=5, y=170, width=80, height=30)

        self.btnMostrarFrame6 = Button(
            frame1, text="Mostrar Frame 6", command=lambda: self.mostrar_frame(frame6))
        self.btnMostrarFrame6.place(x=5, y=210, width=80, height=30)

        # LABELS Y ENTRYS PARA PERSONAL MEDICO

        plbl1 = Label(frame4, text="Nombre: ", bg="lavender")
        plbl1.place(x=3, y=40)
        self.txtNombre = Entry(frame4)
        self.txtNombre.place(x=3, y=60, width=100, height=20)

        plbl2 = Label(frame4, text="Rut: ", bg="lavender")
        plbl2.place(x=3, y=80)
        self.txtRut = Entry(frame4)
        self.txtRut.place(x=3, y=100, width=100, height=20)

        plbl3 = Label(frame4, text="Fecha de ingreso: ", bg="lavender")
        plbl3.place(x=3, y=120)
        self.txtFecha = Entry(frame4)
        self.txtFecha.place(x=3, y=140, width=100, height=20)

        plbl4 = Label(frame4, text="Tipo de Prevision: ", bg="lavender")
        plbl4.place(x=120, y=80)
        self.txtPrevision = ttk.Combobox(
            frame4, values=["Fonasa", "Isapre", "Particular"])
        self.txtPrevision.place(x=120, y=100, width=100, height=20)

        plbl5 = Label(frame4, text="Sueldo Bruto: ", bg="lavender")
        plbl5.place(x=120, y=120)
        self.txtSueldo = Entry(frame4)
        self.txtSueldo.place(x=120, y=140, width=100, height=20)

        plbl6 = Label(frame4, text="Profesion: ", bg="lavender")
        plbl6.place(x=120, y=40)
        self.txtProfesion = ttk.Combobox(
            frame4, values=["Medico", "TENS"])
        self.txtProfesion.place(x=120, y=60, width=100, height=20)

        plbl7 = Label(frame4, text="Area/Especialidad: ", bg="lavender")
        plbl7.place(x=250, y=40)
        self.txtEspecialidad = Entry(frame4)
        self.txtEspecialidad.place(x=250, y=60, width=100, height=20)

        # LABELS Y ENTRYS PARA MEDICOS Y TENS

        lbl1 = Label(frame2, text="Nombre: ", bg="lavender")
        lbl1.place(x=3, y=40)
        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=3, y=60, width=100, height=20)

        lbl2 = Label(frame2, text="Rut: ", bg="lavender")
        lbl2.place(x=3, y=80)
        self.txtRut = Entry(frame2)
        self.txtRut.place(x=3, y=100, width=100, height=20)

        lbl3 = Label(frame2, text="Fecha de ingreso: ", bg="lavender")
        lbl3.place(x=3, y=120)
        self.txtFecha = Entry(frame2)
        self.txtFecha.place(x=3, y=140, width=100, height=20)

        lbl4 = Label(frame2, text="Tipo de Prevision: ", bg="lavender")
        lbl4.place(x=120, y=80)
        self.txtPrevision = ttk.Combobox(
            frame2, values=["Fonasa", "Isapre", "Particular"])
        self.txtPrevision.place(x=120, y=100, width=100, height=20)

        lbl5 = Label(frame2, text="Sueldo Bruto: ", bg="lavender")
        lbl5.place(x=120, y=120)
        self.txtSueldo = Entry(frame2)
        self.txtSueldo.place(x=120, y=140, width=100, height=20)

        lbl6 = Label(frame2, text="Profesion: ", bg="lavender")
        lbl6.place(x=120, y=40)
        self.txtProfesion = ttk.Combobox(
            frame2, values=["Medico", "TENS"])
        self.txtProfesion.place(x=120, y=60, width=100, height=20)

        lbl7 = Label(frame2, text="Area/Especialidad: ", bg="lavender")
        lbl7.place(x=250, y=40)
        self.txtEspecialidad = Entry(frame2)
        self.txtEspecialidad.place(x=250, y=60, width=100, height=20)

        # ----------------Tabla----------------#
        self.tree = ttk.Treeview(frame3, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.tree.column("#0", width=50)
        self.tree.column("col1", width=100, anchor=CENTER)
        self.tree.column("col2", width=100, anchor=CENTER)
        self.tree.column("col3", width=100, anchor=CENTER)
        self.tree.column("col4", width=100, anchor=CENTER)
        self.tree.column("col5", width=110, anchor=CENTER)
        self.tree.column("col6", width=110, anchor=CENTER)
        self.tree.column("col7", width=120, anchor=CENTER)

        self.tree.heading("#0", text="ID", anchor=W)
        self.tree.heading("col1", text="Nombre", anchor=W)
        self.tree.heading("col2", text="RUT", anchor=W)
        self.tree.heading("col3", text="Fecha Ingreso", anchor=W)
        self.tree.heading("col4", text="Tipo Prevision", anchor=W)
        self.tree.heading("col5", text="Profesion", anchor=W)
        self.tree.heading("col6", text="Sueldo Bruto", anchor=W)
        self.tree.heading("col7", text="Area / Especialidad", anchor=W)

        # self.tree.config(show="headings")  # Ocultar la columna vacia

        self.tree.pack(side=LEFT, fill=Y)
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.tree.config(yscrollcommand=sb.set)
        sb.config(command=self.tree.yview)
        self.tree['selectmode'] = 'browse'


app = SeaofBTCapp()
app.mainloop()
