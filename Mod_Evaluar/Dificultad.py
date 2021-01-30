import tkinter as tk
from tkinter import ttk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Presente(self):
        def dificultadElegida(*args):
            comboDificultadElegida= comboDificultad.get()

            if comboDificultadElegida== "Tiraje Intercostal":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(1)
                paramEvaluar.SAC(0.333)
            elif comboDificultadElegida=="Retracciones":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(2)
                paramEvaluar.SAC(0.666)
            elif comboDificultadElegida=="Aleteo Nasal":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(2)
                paramEvaluar.SAC(0.666)
            elif comboDificultadElegida=="Dis.Toraco Abdominal":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(3)
                paramEvaluar.SAC(0.666)

        comboDificultad= ttk.Combobox(self)
        comboDificultad['values']= ("Tiraje Intercostal", "Retracciones","Aleteo Nasal","Dis.Toraco Abdominal")
        comboDificultad.state(["readonly"])
        comboDificultad.bind("<<ComboboxSelected>>", dificultadElegida)
        comboDificultad.pack()
        
    def Ausente(self):
        paramEvaluar.TEPR(True)
        paramEvaluar.SAT(0)
        paramEvaluar.SAC(0.0)