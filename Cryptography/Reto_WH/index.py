from tkinter import *
from tkinter import ttk
from window_view import Window

class Index():

    def main():
        # Creando nuestra ventana con su diseño
        window = Tk()
        app = Window(window)
        app.body()
        app.footer()
        window.mainloop()

    if __name__ == '__main__':
        main()
