import tkinter as tk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Consolable(self):
        paramEvaluar.TEPC(True)
        paramEvaluar.SAT(1)
        paramEvaluar.SAC(0.0)
    def Inconsolable(self):
        paramEvaluar.TEPC(False)
        paramEvaluar.SAT(2)
        paramEvaluar.SAC(0.666)