import tkinter as tk
from tkinter import ttk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Si(self):
        def posicionElegida(*args):
            comboPosicionElegida= comboPosicion.get()
            
            if comboPosicionElegida== "Tripode":
                paramEvaluar.TEPR(False)
            elif comboPosicionElegida=="Olfateo":
                paramEvaluar.TEPR(False)
            elif comboPosicionElegida=="Cabeceo":
                paramEvaluar.TEPR(False)
                    
        comboPosicion= ttk.Combobox(self)
        comboPosicion['values']= ("Tripode","Olfateo","Caebeceo")
        comboPosicion.state(["readonly"])
        comboPosicion.bind("<<ComboboxSelected>>", posicionElegida)
        comboPosicion.pack()
        
    def No(self):
        paramEvaluar.TEPR(True)
        paramEvaluar.SAT(0)
        paramEvaluar.SAC(0.0)
