from tkinter import ttk
from tkinter import *
from CipherOrDecipher import CipherOrDecipher

class Window:
    # Constructor por defecto
    def __init__(self, window):
        self.wind = window
        self.wind.title('Reto WH by Qwerty')

    # Método encargado de crear todo el cuerpo de la app
    def body(self):
        frame = LabelFrame(self.wind, text="Ingresa el mensaje que quieras cifrar o descifrar")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        # Input
        Label(frame, text = "Mensaje:").grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)
        Label(frame, text = "").grid(row = 2, column = 0)
        # Button
        ttk.Button(frame, text = 'Cifrar', command=self.btn_cipher).grid(row = 3, column = 0)
        ttk.Button(frame, text = 'Limpiar', command=self.btn_clear).grid(row = 3, column = 1)
        ttk.Button(frame, text = 'Descifrar', command=self.btn_decipher).grid(row = 3, column = 2)
        # Table
        frame2 = LabelFrame(self.wind, text="Resultado")
        frame2.grid(row = 5, column = 0, columnspan = 3, pady = 20)
        self.T = Text(frame2, height=15, width=30)
        self.T.pack()


    # Método encargado de crear la parte inferior de la app
    def footer(self):
        Label(self.wind, text = "\n").grid(row = 6, column = 0)
        

    # Método que manda el mensaje cifrado o descifrado al text área
    def set_message_totext(self, action):
        algorithm = CipherOrDecipher(self.name.get(), action)
        self.T.insert(END, algorithm.start_algorithm())

    # Métodos que los Buttons llamarán para realizar cierta acción
    def btn_cipher(self):
        self.set_message_totext('cipher')

    def btn_decipher(self):
        self.set_message_totext('decipher')

    def btn_clear(self):
        self.T.delete('1.0', END)
