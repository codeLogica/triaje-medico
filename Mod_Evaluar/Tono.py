import tkinter as tk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Eutonico(self):
        paramEvaluar.TEPA(True)
    def Hipotonico(self):
        paramEvaluar.TEPA(False)