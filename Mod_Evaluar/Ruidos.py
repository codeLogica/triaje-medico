import tkinter as tk
from tkinter import ttk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Presentes(self):
        def ruidoElegido(*args):
            comboRuidoElegido= comboRuidos.get()
            if comboRuidoElegido== "Gruñido":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(+3)
                paramEvaluar.SAC(+0.333)
                return True
            elif comboRuidoElegido== "Estridor":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(+3)
                paramEvaluar.SAC(+0.333)
                return True
            elif comboRuidoElegido== "Disfonia":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(+3)
                paramEvaluar.SAC(+0.333)
                return True
            elif comboRuidoElegido== "Quejido":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(+3)
                paramEvaluar.SAC(+0.333)
                return True
            elif comboRuidoElegido== "Silibancia":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(+3)
                paramEvaluar.SAC(+0.333)
                return True

        comboRuidos= ttk.Combobox(self)
        comboRuidos['values'] =("Gruñido", "Estridor", "Disfonia", "Quejido", "Silibancia") 
        comboRuidos.state(["readonly"])
        comboRuidos.bind("<<ComboboxSelected>>", ruidoElegido)
        comboRuidos.pack()
                    
    def Ausentes(self):
        paramEvaluar.TEPR(True)
        paramEvaluar.SAT(+0)
        paramEvaluar.SAC(+0)