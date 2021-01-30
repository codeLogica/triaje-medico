import tkinter as tk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def NoTolera(self):
        paramEvaluar.SAC(0.333)
    def SiTolera(self):
        paramEvaluar.SAC(0.0)
