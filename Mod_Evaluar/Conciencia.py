import tkinter as tk
import app
from Mod_Evaluar import Parametros

#Se hace la llamda al modulo de parametros a evaluar. 
paramEvaluar = Parametros.Evaluar()

class Opciones():    
    def Despierto(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAT(+0)
        paramEvaluar.SAC(+0)
    def Somnoliento(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAT(+1)
        paramEvaluar.SAC(+0)
    def Irritable(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(+2)
        paramEvaluar.SAC(+0.3)
    def NoDuerme(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(+3)
        paramEvaluar.SAC(+1)
    def Crisis(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(+3)
        paramEvaluar.SAC(+0.3)

                
