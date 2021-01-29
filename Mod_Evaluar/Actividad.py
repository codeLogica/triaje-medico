import tkinter as tk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Juega(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAT(+0)
        paramEvaluar.SAC(+0)
    def Confundido(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(+3)
        paramEvaluar.SAC(+0.333)
    def Letargico(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(+3)
        paramEvaluar.SAC(+0.666)
    def Inconsciente(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(+3)
        paramEvaluar.SAC(+0.666)