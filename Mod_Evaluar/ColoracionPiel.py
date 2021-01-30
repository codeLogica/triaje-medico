import tkinter as tk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Rosada(self):
        paramEvaluar.TEPC(True)
        paramEvaluar.SAT(0)
        paramEvaluar.SAC(0.0)
    def Palida(self):
        paramEvaluar.TEPC(False)
        paramEvaluar.SAT(1)
        paramEvaluar.SAC(0.333)
    def Cianotica(self):
        paramEvaluar.TEPC(False)
        paramEvaluar.SAT(2)
        paramEvaluar.SAC(0.333)
    def Rubicunda(self):
        paramEvaluar.TEPC(False)
        paramEvaluar.SAT(2)
        paramEvaluar.SAC(0.333)
    def Marmorea(self):
        paramEvaluar.TEPC(False)
        paramEvaluar.SAT(3)
        paramEvaluar.SAC(0.333)
    def Purpurica(self):
        paramEvaluar.TEPC(False)
        paramEvaluar.SAT(3)
        paramEvaluar.SAC(0.333)
        