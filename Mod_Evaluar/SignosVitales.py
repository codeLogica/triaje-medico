import tkinter as tk
from tkinter import ttk
from typing import Text
import app
from Mod_Evaluar import Parametros

#Se hace la llamada a el modulo de los parametros a evaluar
paramEvaluar = Parametros.Evaluar()

class Validar():
    def Dato(datoIngresado):
        return Text.isdecimal()
        
 