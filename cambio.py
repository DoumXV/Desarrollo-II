from tkinter import Frame, Label, Button, Tk


class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x200")
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def show(self):
        self.pack()
        self.crear_widgets()

    def cerrar_ventana(self):
        self.master.destroy()

    def hide(self):
        self.pack_forget()


class Ventana1(Ventana):
    def crear_widgets(self):
        label = Label(self, text="Esta es la Ventana 1")
        label.pack()

        boton_cambiar_ventana = Button(
            self, text="Cambiar a Ventana 2", command=self.cambiar_a_ventana2)
        boton_cambiar_ventana.pack()

    def cambiar_a_ventana2(self):
        self.master.ventana_actual.hide()
        self.master.ventana_actual = self.master.ventana2
        self.master.ventana_actual.show()


class Ventana2(Ventana):
    def crear_widgets(self):
        label = Label(self, text="Esta es la Ventana 2")
        label.pack()

        boton_cambiar_ventana = Button(
            self, text="Cambiar a Ventana 1", command=self.cambiar_a_ventana1)
        boton_cambiar_ventana.pack()

    def cambiar_a_ventana1(self):
        self.master.ventana_actual.hide()
        self.master.ventana_actual = self.master.ventana1
        self.master.ventana_actual.show()


def main():
    root = Tk()
    root.wm_title("CRUD Python con POO")

    ventana1 = Ventana1(root)
    ventana2 = Ventana2(root)

    root.ventana1 = ventana1
    root.ventana2 = ventana2

    root.ventana_actual = ventana1
    root.ventana_actual.show()

    root.mainloop()


if __name__ == "__main__":
    main()
