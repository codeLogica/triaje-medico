import tkinter as tk
from tkinter import ttk
from Frames import *

#Esta seccion sirve para camibiar entre frames durante la ejecucion del programa. Funciona como manejador principal de la apariencia de todo el programa. 
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
#        tk.Tk.attributes(self, '-fullscreen', True)
#        tk.Tk.bind(self, "<F11>",'-fullscreen', False)
#        tk.Tk.bind(self, "<Escape>",'-fullscreen', False)
        self._frame = None
        self.switch_frame(PaginaGeneral)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()