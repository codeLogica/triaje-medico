import tkinter as tk
from tkinter import ttk
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Opciones():
    def Presentes(self):
        paramEvaluar.SAC(0.333)
    def Negados(self):
        paramEvaluar.SAC(0.0)