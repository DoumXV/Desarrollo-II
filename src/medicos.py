from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bd import *
from pacientes import *


class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Hospital Copiapo")
        self.geometry("993x600")

        self.frame_actual = None

        self.mostrar_interfaz()
        self.create_menu()

    def create_menu(self):
        # Crea una instancia del menú
        menubar = Menu(self)

        # Crea el primer menú desplegable
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Pacientes", command=self.mostrar_ventana2)
        file_menu.add_command(label="Empleados", command=self.mostrar_ventana1)
        file_menu.add_separator()
        # file_menu.add_command(
        #    label="Limpiar Tabla", command=Ventana.limpiarTree(self) and Ventana.limpiarTreeP(self))
        file_menu.add_command(label="Salir", command=self.confirm_exit)

        # Agrega el primer menú desplegable a la barra de menú
        menubar.add_cascade(label="Archivo", menu=file_menu)

        # Configura la barra de menú en la ventana principal
        self.config(menu=menubar)

    def mostrar_interfaz(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Interfaz(self)

    def mostrar_ventana1(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana(self)

    def mostrar_ventana2(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana2(self)

    def confirm_exit(self):
        # Muestra un cuadro de diálogo de confirmación antes de salir
        if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
            self.destroy()


class Interfaz(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=993, height=600)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        frame1 = Frame(self, bg="lavender")
        frame1.place(x=0, y=0, width=993, height=600)

        self.btnEmpleados = Button(frame1, text="Gestionar Empleados",
                                   command=self.master.mostrar_ventana1, bg="blue", fg="white")
        self.btnEmpleados.place(x=400, y=170, width=200, height=30)

        self.btnPacientes = Button(frame1, text="Gestionar Pacientes",
                                   command=self.master.mostrar_ventana2, bg="blue", fg="white")
        self.btnPacientes.place(x=400, y=220, width=200, height=30)

        self.btnConsultas = Button(frame1, text="Consultas",
                                   command="", bg="blue", fg="white")
        self.btnConsultas.place(x=400, y=270, width=200, height=30)


class Ventana(Frame):
    medicos = Medico()
    personaal = Personal()

    def __init__(self, master=None):
        super().__init__(master, width=993, height=600)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatosP()
        self.llenarDatos()
        self.habilitarCajasMedico("disabled")
        self.habilitarCajasPersonal("disabled")
        self.habilitarBtnIzqMedico("normal")
        self.habilitarBtnDerMedico("disabled")
        self.id = -1

    def validar(self):
        if not self.txtNombre.get() or not self.txtRut.get() or not self.txtFecha.get() or not self.txtPrevision.get() or not self.txtProfesion.get() or not self.txtSueldo.get() or not self.txtEspecialidad.get():
            return False
        return True

    def validarP(self):
        if not self.pxtNombre.get() or not self.pxtRut.get() or not self.pxtFecha.get() or not self.pxtPrevision.get() or not self.pxtSueldo.get() or not self.pxtUnidad.get() or not self.pxtCargo.get():
            return False
        return True

    def validarid(self):
        if not self.txtID.get():
            return False
        return True

    def validaridP(self):
        if not self.pxtID.get():
            return False
        return True

    def habilitarTreeMedico(self):
        self.treeP.pack_forget()
        self.tree.pack(side=LEFT, fill=Y)

    def habilitarTreePersonal(self):
        self.treeP.pack(side=LEFT, fill=Y)
        self.tree.pack_forget()

    def llenarDatos(self):
        # PACIENTES BOX
        datos = self.medicos.seleccionar_todos()
        print(datos)
        for dato in datos:
            self.tree.insert("", END, text=dato[0], values=(
                dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))

    def llenarDatosP(self):
        datos = self.personaal.seleccionar_todos()
        print(datos)
        for dato in datos:
            self.treeP.insert("", END, text=dato[0], values=(
                dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))

    def limpiarTree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def limpiarTreeP(self):
        for item in self.treeP.get_children():
            self.treeP.delete(item)

    def habilitarBtnIzqMedico(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnIzqPersonal(self, estado):
        self.btnNuevoP.configure(state=estado)
        self.btnModificarP.configure(state=estado)
        self.btnEliminarP.configure(state=estado)

    def habilitarBtnDerMedico(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def habilitarBtnDerPersonal(self, estado):
        self.btnGuardarP.configure(state=estado)
        self.btnCancelarP.configure(state=estado)

    def habilitarCajasMedico(self, estado):
        self.txtEspecialidad.configure(state=estado)
        self.txtFecha.configure(state=estado)
        self.txtNombre.configure(state=estado)
        self.txtPrevision.configure(state=estado)
        self.txtProfesion.configure(state=estado)
        self.txtRut.configure(state=estado)
        self.txtSueldo.configure(state=estado)

    def habilitarCajasPersonal(self, estado):
        self.pxtCargo.configure(state=estado)
        self.pxtFecha.configure(state=estado)
        self.pxtNombre.configure(state=estado)
        self.pxtPrevision.configure(state=estado)
        self.pxtRut.configure(state=estado)
        self.pxtSueldo.configure(state=estado)
        self.pxtUnidad.configure(state=estado)

    def limpiarCajasMedico(self):
        self.txtEspecialidad.delete(0, END)
        self.txtFecha.delete(0, END)
        self.txtNombre.delete(0, END)
        self.txtPrevision.delete(0, END)
        self.txtProfesion.delete(0, END)
        self.txtRut.delete(0, END)
        self.txtSueldo.delete(0, END)

    def limpiarCajasPersonal(self):
        self.pxtNombre.delete(0, END)
        self.pxtRut.delete(0, END)
        self.pxtFecha.delete(0, END)
        self.pxtPrevision.delete(0, END)
        self.pxtSueldo.delete(0, END)
        self.pxtUnidad.delete(0, END)
        self.pxtCargo.delete(0, END)

    def Nuevo(self):
        self.limpiarTree()
        self.llenarDatos()
        self.habilitarTreeMedico()
        self.habilitarCajasMedico("normal")
        self.habilitarBtnIzqMedico("disabled")
        self.habilitarBtnDerMedico("normal")
        self.limpiarCajasMedico()
        self.txtNombre.focus()

    def NuevoP(self):
        self.limpiarTreeP()
        self.llenarDatosP()
        self.habilitarTreePersonal()
        self.habilitarCajasPersonal("normal")
        self.habilitarBtnIzqPersonal("disabled")
        self.habilitarBtnDerPersonal("normal")
        self.limpiarCajasPersonal()
        self.pxtNombre.focus()

    def Modificar(self):
        selected = self.tree.focus()
        clave = self.tree.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Modificar", "Debes seleccionar un Elemento")
        else:
            self.id = clave
            self.habilitarCajasMedico("normal")
            valores = self.tree.item(selected, 'values')
            self.limpiarCajasMedico()
            self.txtNombre.insert(0, valores[0])
            self.txtRut.insert(0, valores[1])
            self.txtFecha.insert(0, valores[2])
            self.txtPrevision.insert(0, valores[3])
            self.txtProfesion.insert(0, valores[4])
            self.txtSueldo.insert(0, valores[5])
            self.txtEspecialidad.insert(0, valores[6])
            self.habilitarBtnIzqMedico("disabled")
            self.habilitarBtnDerMedico("normal")
            self.txtNombre.focus()

    def ModificarP(self):
        selected = self.treeP.focus()
        clave = self.treeP.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Modificar", "Debes seleccionar un Elemento")
        else:
            self.id = clave
            self.habilitarCajasPersonal("normal")
            valores = self.treeP.item(selected, 'values')
            print(valores)
            self.habilitarCajasPersonal("normal")
            self.limpiarCajasPersonal()
            self.pxtNombre.insert(0, valores[0])
            self.pxtRut.insert(0, valores[1])
            self.pxtFecha.insert(0, valores[2])
            self.pxtPrevision.insert(0, valores[3])
            self.pxtSueldo.insert(0, valores[4])
            self.pxtUnidad.insert(0, valores[5])
            self.pxtCargo.insert(0, valores[6])
            self.habilitarBtnIzqPersonal("disabled")
            self.habilitarBtnDerPersonal("normal")
            self.pxtNombre.focus()

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
                n = self.medicos.eliminar_usuario(clave)
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

    def EliminarP(self):
        selected = self.treeP.focus()
        clave = self.treeP.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Eliminar", "Debes seleccionar un Elemento")
        else:
            r = messagebox.askquestion(
                "Eliminar", "Desea eliminar el registro seleccionado?")
            if r == messagebox.YES:
                n = self.personaal.eliminar_usuario(clave)
                if n == 1:
                    messagebox.showinfo(
                        "Eliminar", "Elemento eliminado correctamente")
                    self.limpiarTreeP()
                    self.llenarDatosP()
                    self.habilitarTreePersonal()
                else:
                    messagebox.showinfo(
                        "Eliminar", "No fue posible eliminar el elemento")
            else:
                pass

    def Buscar(self):
        if self.validarid():
            dato = self.medicos.seleccionar_usuario(self.txtID.get())
            print(dato)
            if dato!=None:
                self.habilitarTreeMedico()
                self.limpiarTree()
                self.tree.insert("", END, text=dato[0], values=(
                    dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))
            else:
                messagebox.showwarning("Buscar", "Este ID no existe")

        else:
            messagebox.showwarning("Buscar", "Debes ingresar un ID")

    def BuscarP(self):
        if self.validaridP():
            dato = self.personaal.seleccionar_usuario(self.pxtID.get())
            print(dato)
            if dato !=None:
                self.habilitarTreePersonal()
                self.limpiarTreeP()
                self.treeP.insert("", END, text=dato[0], values=(
                    dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))
            else:
                messagebox.showwarning("Buscar", "Este ID no existe")

        else:
            messagebox.showwarning("Buscar", "Debes ingresar un ID")

    def Guardar(self):
        if self.validar():
            if self.id == -1:
                n = self.medicos.guardar_usuario(self.txtNombre.get(), self.txtRut.get(), self.txtFecha.get(
                ), self.txtPrevision.get(), self.txtProfesion.get(), self.txtSueldo.get(), self.txtEspecialidad.get())
                if n == 1:
                    messagebox.showinfo(
                        "Guardar", "Elemento Registrado correctamente")
                else:
                    messagebox.showinfo(
                        "Guardar", "No fue posible eliminar el elemento")
            else:
                n = self.medicos.actualizar_usuario(self.id, self.txtNombre.get(), self.txtRut.get(), self.txtFecha.get(
                ), self.txtPrevision.get(), self.txtProfesion.get(), self.txtSueldo.get(), self.txtEspecialidad.get())
                self.id = -1
                if n == 1:
                    messagebox.showinfo(
                        "Modificar", "Elemento Modificado correctamente")
                    self.limpiarCajasMedico()
                    self.habilitarCajasMedico("disabled")
                else:
                    messagebox.showinfo(
                        "Modificar", "No fue posible modificar el elemento")

            self.limpiarTree()
            self.llenarDatos()
            self.limpiarCajasMedico()
            self.habilitarBtnDerMedico("disabled")
            self.habilitarBtnIzqMedico("normal")
        else:
            messagebox.showwarning(
                "Guardar", "Debes completar todos los campos")

    def GuardarP(self):
        if self.validarP():
            if self.id == -1:
                n = self.personaal.guardar_usuario(self.pxtNombre.get(), self.pxtRut.get(), self.pxtFecha.get(
                ), self.pxtPrevision.get(), self.pxtSueldo.get(), self.pxtUnidad.get(), self.pxtCargo.get())
                if n == 1:
                    messagebox.showinfo(
                        "Guardar", "Elemento Registrado correctamente")
                else:
                    messagebox.showinfo(
                        "Guardar", "No fue posible eliminar el elemento")
            else:
                n = self.personaal.actualizar_usuario(self.id, self.pxtNombre.get(), self.pxtRut.get(), self.pxtFecha.get(
                ), self.pxtPrevision.get(), self.pxtSueldo.get(), self.pxtUnidad.get(), self.pxtCargo.get())
                self.id = -1
                if n == 1:
                    messagebox.showinfo(
                        "Modificar", "Elemento Modificado correctamente")
                    self.limpiarCajasPersonal()
                    self.habilitarCajasPersonal("disabled")
                else:
                    messagebox.showinfo(
                        "Modificar", "No fue posible modificar el elemento")

            self.limpiarTreeP()
            self.llenarDatosP()
            self.limpiarCajasPersonal()
            self.habilitarBtnDerPersonal("disabled")
            self.habilitarBtnIzqPersonal("normal")
        else:
            messagebox.showwarning(
                "Guardar", "Debes completar todos los campos")

    def Cancelar(self):
        r = messagebox.askquestion(
            "Cancelar", "Esta seguro que desea cancelar la operacion actual")
        if r == messagebox.YES:
            self.limpiarCajasMedico()
            self.habilitarBtnDerMedico("disabled")
            self.habilitarBtnIzqMedico("normal")
            self.habilitarCajasMedico("disabled")

    def CancelarP(self):
        r = messagebox.askquestion(
            "Cancelar", "Esta seguro que desea cancelar la operacion actual")
        if r == messagebox.YES:
            self.limpiarCajasPersonal()
            self.habilitarBtnDerPersonal("disabled")
            self.habilitarBtnIzqPersonal("normal")
            self.habilitarCajasPersonal("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="powder blue")
        frame1.place(x=0, y=0, width=93, height=600)

        frame2 = Frame(self, bg="powder blue")
        frame2.place(x=95, y=0, width=400, height=220)

        frame3 = Frame(self, bg="powder blue")
        frame3.place(x=96, y=223, width=804, height=399)

        frame4 = Frame(self, bg="powder blue")
        frame4.place(x=500, y=0, width=400, height=220)

        frame5 = Frame(self, bg="powder blue")
        frame5.place(x=902, y=0, width=93, height=600)

        # BOTONOES MEDICOS
        self.btnNuevo = Button(frame1, text="Nuevo",
                               command=self.Nuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnModificar = Button(frame1, text="Modificar",
                                   command=self.Modificar, bg="blue", fg="white")
        self.btnModificar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar = Button(frame1, text="Eliminar",
                                  command=self.Eliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)

        self.btnBuscar = Button(frame1, text="Buscar",
                                command=self.Buscar, bg="blue", fg="white")
        self.btnBuscar.place(x=5, y=250, width=80, height=30)

        self.btnGuardar = Button(frame2, text="Guardar",
                                 command=self.Guardar, bg="chartreuse3", fg="white")
        self.btnGuardar.place(x=70, y=180, width=80, height=30)

        self.btnCancelar = Button(frame2, text="Cancelar",
                                  command=self.Cancelar, bg="tomato", fg="white")
        self.btnCancelar.place(x=170, y=180, width=80, height=30)

        # BOTONES PERSONAL
        self.btnNuevoP = Button(frame5, text="Nuevo",
                                command=self.NuevoP, bg="blue", fg="white")
        self.btnNuevoP.place(x=5, y=50, width=80, height=30)

        self.btnModificarP = Button(frame5, text="Modificar",
                                    command=self.ModificarP, bg="blue", fg="white")
        self.btnModificarP.place(x=5, y=90, width=80, height=30)

        self.btnEliminarP = Button(frame5, text="Eliminar",
                                   command=self.EliminarP, bg="blue", fg="white")
        self.btnEliminarP.place(x=5, y=130, width=80, height=30)

        self.btnBuscarP = Button(frame5, text="Buscar",
                                 command=self.BuscarP, bg="blue", fg="white")
        self.btnBuscarP.place(x=5, y=250, width=80, height=30)

        self.btnGuardarP = Button(frame4, text="Guardar",
                                  command=self.GuardarP, bg="chartreuse3", fg="white")
        self.btnGuardarP.place(x=70, y=180, width=80, height=30)

        self.btnCancelarP = Button(frame4, text="Cancelar",
                                   command=self.CancelarP, bg="tomato", fg="white")
        self.btnCancelarP.place(x=170, y=180, width=80, height=30)

        self.btnVolver = Button(frame1, text="Volver",
                                command=self.master.mostrar_interfaz, bg="black", fg="white")
        self.btnVolver.place(x=5, y=5, width=80, height=30)

        # LABELS Y ENTRYS PARA PERSONAL MEDICO
        plbl0 = Label(frame4, text="Personal de Salud ",
                      bg="powder blue", font="Verdana")
        plbl0.place(x=120, y=10)

        lblid = Label(frame1, text="ID: ", bg="powder blue")
        lblid.place(x=3, y=220)
        self.txtID = Entry(frame1)
        self.txtID.place(x=30, y=220, width=50, height=20)

        plblid = Label(frame5, text="ID: ", bg="powder blue")
        plblid.place(x=3, y=220)
        self.pxtID = Entry(frame5)
        self.pxtID.place(x=30, y=220, width=50, height=20)

        plbl1 = Label(frame4, text="Nombre: ", bg="powder blue")
        plbl1.place(x=3, y=40)
        self.pxtNombre = Entry(frame4)
        self.pxtNombre.place(x=3, y=60, width=100, height=20)

        plbl2 = Label(frame4, text="Rut: ", bg="powder blue")
        plbl2.place(x=3, y=80)
        self.pxtRut = Entry(frame4)
        self.pxtRut.place(x=3, y=100, width=100, height=20)

        plbl3 = Label(frame4, text="Fecha de ingreso: ", bg="powder blue")
        plbl3.place(x=3, y=120)
        self.pxtFecha = Entry(frame4)
        self.pxtFecha.place(x=3, y=140, width=100, height=20)

        plbl4 = Label(frame4, text="Tipo de Prevision: ", bg="powder blue")
        plbl4.place(x=120, y=80)
        self.pxtPrevision = ttk.Combobox(
            frame4, values=["Fonasa", "Isapre", "Particular"])
        self.pxtPrevision.place(x=120, y=100, width=100, height=20)

        plbl5 = Label(frame4, text="Sueldo Bruto: ", bg="powder blue")
        plbl5.place(x=120, y=120)
        self.pxtSueldo = Entry(frame4)
        self.pxtSueldo.place(x=120, y=140, width=100, height=20)

        plbl6 = Label(frame4, text="Unidad Administrativa:", bg="powder blue")
        plbl6.place(x=120, y=40)
        self.pxtUnidad = ttk.Combobox(
            frame4, values=["Servicios Generales", "Personal", "Jefatura"])
        self.pxtUnidad.place(x=120, y=60, width=100, height=20)

        plbl7 = Label(frame4, text="Cargo: ", bg="powder blue")
        plbl7.place(x=250, y=40)
        self.pxtCargo = ttk.Combobox(
            frame4, values=["Jefe", "Empleado"])
        self.pxtCargo.place(x=250, y=60, width=100, height=20)

        # LABELS Y ENTRYS PARA MEDICOS Y TENS

        lbl0 = Label(frame2, text="Medicos/TENS ",
                     bg="powder blue", font="Verdana")
        lbl0.place(x=120, y=10)

        lbl1 = Label(frame2, text="Nombre: ", bg="powder blue")
        lbl1.place(x=3, y=40)
        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=3, y=60, width=100, height=20)

        lbl2 = Label(frame2, text="Rut: ", bg="powder blue")
        lbl2.place(x=3, y=80)
        self.txtRut = Entry(frame2)
        self.txtRut.place(x=3, y=100, width=100, height=20)

        lbl3 = Label(frame2, text="Fecha de ingreso: ", bg="powder blue")
        lbl3.place(x=3, y=120)
        self.txtFecha = Entry(frame2)
        self.txtFecha.place(x=3, y=140, width=100, height=20)

        lbl4 = Label(frame2, text="Tipo de Prevision: ", bg="powder blue")
        lbl4.place(x=120, y=80)
        self.txtPrevision = ttk.Combobox(
            frame2, values=["Fonasa", "Isapre", "Particular"])
        self.txtPrevision.place(x=120, y=100, width=100, height=20)

        lbl5 = Label(frame2, text="Sueldo Bruto: ", bg="powder blue")
        lbl5.place(x=120, y=120)
        self.txtSueldo = Entry(frame2)
        self.txtSueldo.place(x=120, y=140, width=100, height=20)

        lbl6 = Label(frame2, text="Profesion: ", bg="powder blue")
        lbl6.place(x=120, y=40)
        self.txtProfesion = ttk.Combobox(
            frame2, values=["Medico", "TENS"])
        self.txtProfesion.place(x=120, y=60, width=100, height=20)

        lbl7 = Label(frame2, text="Area/Especialidad: ", bg="powder blue")
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
        self.tree.column("col7", width=128, anchor=CENTER)

        self.tree.heading("#0", text="ID", anchor=W)
        self.tree.heading("col1", text="Nombre", anchor=W)
        self.tree.heading("col2", text="RUT", anchor=W)
        self.tree.heading("col3", text="Fecha Ingreso", anchor=W)
        self.tree.heading("col4", text="Tipo Prevision", anchor=W)
        self.tree.heading("col5", text="Profesion", anchor=W)
        self.tree.heading("col6", text="Sueldo Bruto", anchor=W)
        self.tree.heading("col7", text="Area / Especialidad", anchor=W)

        # ----------------Tabla----------------#
        self.treeP = ttk.Treeview(frame3, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.treeP.column("#0", width=50)
        self.treeP.column("col1", width=100, anchor=CENTER)
        self.treeP.column("col2", width=100, anchor=CENTER)
        self.treeP.column("col3", width=100, anchor=CENTER)
        self.treeP.column("col4", width=100, anchor=CENTER)
        self.treeP.column("col5", width=110, anchor=CENTER)
        self.treeP.column("col6", width=110, anchor=CENTER)
        self.treeP.column("col7", width=128, anchor=CENTER)

        self.treeP.heading("#0", text="ID", anchor=W)
        self.treeP.heading("col1", text="Nombre", anchor=W)
        self.treeP.heading("col2", text="RUT", anchor=W)
        self.treeP.heading("col3", text="Fecha Ingreso", anchor=W)
        self.treeP.heading("col4", text="Tipo Prevision", anchor=W)
        self.treeP.heading("col5", text="Sueldo", anchor=W)
        self.treeP.heading("col6", text="Unidad ", anchor=W)
        self.treeP.heading("col7", text="Cargo", anchor=W)

        # self.tree.config(show="headings")  # Ocultar la columna vacia
