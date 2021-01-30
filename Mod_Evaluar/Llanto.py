import tkinter as tk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Fuerte(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAC(0.0)
    def Debil(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAC(0.333)