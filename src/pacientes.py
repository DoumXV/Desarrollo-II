from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bd import *


class Ventana2(Frame):
    hospital = Paciente()

    def __init__(self, master=None):
        super().__init__(master, width=1200, height=600)
        self.master = master
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
            print(dato[9])
            self.tree.insert("", END, text=dato[0], values=(
                dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))

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
        self.txtDerivacion.configure(state=estado)
        self.txtMotivo.configure(state=estado)
        self.txtRut.configure(state=estado)
        self.txtBox.configure(state=estado)
        self.txtMedico.configure(state=estado)
        self.txtPrevision.configure(state=estado)

    def limpiarCajas(self):
        self.txtEspecialidad.delete(0, END)
        self.txtFecha.delete(0, END)
        self.txtNombre.delete(0, END)
        self.txtPrevision.delete(0, END)
        self.txtBox.delete(0, END)
        self.txtRut.delete(0, END)
        self.txtMedico.delete(0, END)
        self.txtMotivo.delete(0, END)
        self.txtDerivacion.delete(0, END)

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
            self.txtMotivo.insert(0, valores[4])
            self.txtDerivacion.insert(0, valores[5])
            self.txtMedico.insert(0, valores[6])
            self.txtEspecialidad.insert(0, valores[7])
            self.txtBox.insert(0, valores[8])
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
            ), self.txtPrevision.get(), self.txtMotivo.get(), self.txtDerivacion.get(), self.txtMedico.get(), self.txtEspecialidad.get(), self.txtBox.get())
            if n == 1:
                messagebox.showinfo(
                    "Guardar", "Elemento Registrado correctamente")
            else:
                messagebox.showinfo(
                    "Guardar", "No fue posible eliminar el elemento")
        else:
            n = self.hospital.guardar_usuario(self.txtNombre.get(), self.txtRut.get(), self.txtFecha.get(
            ), self.txtPrevision.get(), self.txtMotivo.get(), self.txtDerivacion.get(), self.txtMedico.get(), self.txtEspecialidad.get(), self.txtBox.get())
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

    def create_widgets(self):
        frame1 = Frame(self, bg="gray99")
        frame1.place(x=0, y=0, width=93, height=220)

        frame2 = Frame(self, bg="gray99")
        frame2.place(x=95, y=0, width=980, height=220)

        frame3 = Frame(self, bg="gray99")
        frame3.place(x=5, y=223, width=980, height=399)

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
        self.btnGuardar.place(x=400, y=80, width=80, height=30)

        self.btnCancelar = Button(frame2, text="Cancelar",
                                  command=self.Cancelar, bg="red", fg="white")
        self.btnCancelar.place(x=400, y=120, width=80, height=30)

        self.btnVolver = Button(frame1, text="Volver",
                                command=self.master.mostrar_interfaz, bg="black", fg="white")
        self.btnVolver.place(x=5, y=5, width=80, height=30)

        # LABELS Y ENTRYS PARA MEDICOS Y TENS

        lbl1 = Label(frame2, text="Nombre: ", bg="gray99")
        lbl1.place(x=3, y=40)
        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=3, y=60, width=100, height=20)

        lbl2 = Label(frame2, text="Rut: ", bg="gray99")
        lbl2.place(x=3, y=80)
        self.txtRut = Entry(frame2)
        self.txtRut.place(x=3, y=100, width=100, height=20)

        lbl3 = Label(frame2, text="Fecha de ingreso: ", bg="gray99")
        lbl3.place(x=3, y=120)
        self.txtFecha = Entry(frame2)
        self.txtFecha.place(x=3, y=140, width=100, height=20)

        lbl4 = Label(frame2, text="Tipo de Prevision: ", bg="gray99")
        lbl4.place(x=120, y=80)
        self.txtPrevision = ttk.Combobox(
            frame2, values=["Fonasa", "Isapre", "Particular"])
        self.txtPrevision.place(x=120, y=100, width=100, height=20)

        lbl5 = Label(frame2, text="Motivo del Ingreso : ", bg="gray99")
        lbl5.place(x=120, y=120)
        self.txtMotivo = Entry(frame2)
        self.txtMotivo.place(x=120, y=140, width=100, height=20)

        lbl6 = Label(frame2, text="Derivacion: ", bg="gray99")
        lbl6.place(x=120, y=40)
        self.txtDerivacion = ttk.Combobox(
            frame2, values=["Consulta Medica", "Urgencia"])
        self.txtDerivacion.place(x=120, y=60, width=100, height=20)

        lbl7 = Label(frame2, text="Medico: ", bg="gray99")
        lbl7.place(x=250, y=40)
        self.txtMedico = Entry(frame2)
        self.txtMedico.place(x=250, y=60, width=100, height=20)

        lbl8 = Label(frame2, text="Especialidad: ", bg="gray99")
        lbl8.place(x=250, y=80)
        self.txtEspecialidad = Entry(frame2)
        self.txtEspecialidad.place(x=250, y=100, width=100, height=20)

        lbl9 = Label(frame2, text="Box: ", bg="gray99")
        lbl9.place(x=250, y=120)
        self.txtBox = Entry(frame2)
        self.txtBox.place(x=250, y=140, width=100, height=20)

        # ----------------Tabla----------------#
        self.tree = ttk.Treeview(frame3, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.tree.column("#0", width=50)
        self.tree.column("col1", width=100, anchor=CENTER)
        self.tree.column("col2", width=100, anchor=CENTER)
        self.tree.column("col3", width=100, anchor=CENTER)
        self.tree.column("col4", width=100, anchor=CENTER)
        self.tree.column("col5", width=110, anchor=CENTER)
        self.tree.column("col6", width=110, anchor=CENTER)
        self.tree.column("col7", width=110, anchor=CENTER)
        self.tree.column("col8", width=110, anchor=CENTER)
        self.tree.column("col9", width=100, anchor=CENTER)

        self.tree.heading("#0", text="ID", anchor=W)
        self.tree.heading("col1", text="Nombre", anchor=W)
        self.tree.heading("col2", text="RUT", anchor=W)
        self.tree.heading("col3", text="Fecha Ingreso", anchor=W)
        self.tree.heading("col4", text="Tipo Prevision", anchor=W)
        self.tree.heading("col5", text="Motivo", anchor=W)
        self.tree.heading("col6", text="Derivacion", anchor=W)
        self.tree.heading("col7", text="Medico", anchor=W)
        self.tree.heading("col8", text="Especialidad", anchor=W)
        self.tree.heading("col9", text="Box", anchor=W)

        # self.tree.config(show="headings")  # Ocultar la columna vacia

        self.tree.pack(side=LEFT, fill=Y)
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.tree.config(yscrollcommand=sb.set)
        sb.config(command=self.tree.yview)
        self.tree['selectmode'] = 'browse'
