import tkinter as tk
from tkinter import ttk
#Se importa el modulo a los que se asignara los valores, pasandolos como argumentos.
from Mod_Eva import Parametros

#Se hace la llamda al modulo de parametros a evaluar. 
paramEvaluar = Parametros.Evaluar()

#Cada metodo de las clases esta asignado a un boton en el GUI, estos pasan al modulo Parametros un valor como argumento. Algunos metodos pasan los mismos valores, estos es porque en la practica puede que la presentacion de los sintomas sea distinta pero igual de beninga o maligna, dependiendo. 
class ConcienciaOpcion():    
    def Despierto(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAT(0)
        paramEvaluar.SAC(0.0)
    def Somnoliento(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAT(1)
        paramEvaluar.SAC(0.0)
    def Irritable(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(2)
        paramEvaluar.SAC(0.333)
    def NoDuerme(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(3)
        paramEvaluar.SAC(0.333)
    def Crisis(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(3)
        paramEvaluar.SAC(0.333)

class ColorPielOpcion():
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
        
class HidratacionPielOpcion():
    def Normal(self):
        paramEvaluar.SAC(0)
    def Seca(self):
        paramEvaluar.SAC(0.333)       
        
class HidratacionMucosasOpcion():
    def Normal(self):
        paramEvaluar.SAC(0)
    def Seca(self):
        paramEvaluar.SAC(0.333)      
        
class HidratacionOjosOpcion():
    def Normal(self):
        paramEvaluar.SAC(0)
    def Hundidos(self):
        paramEvaluar.SAC(0.333)        
        
class HidratacionVomitoOpcion():
    def Presente(self):
        paramEvaluar.SAC(0.333)
    def Ausente(self):
        paramEvaluar.SAC(0.0)
        
class HidratacionToleranciaOpcion():
    def NoTolera(self):
        paramEvaluar.SAC(0.333)
    def SiTolera(self):
        paramEvaluar.SAC(0.0)

class HidratacionPliegueOpcion():
    def Positivo(self):
        paramEvaluar.SAC(0.333)
    def Negativo(self):
        paramEvaluar.SAC(0.0)

class ActividadOpcion():
    def Juega(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAT(0)
        paramEvaluar.SAC(0.0)
    def Confundido(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(3)
        paramEvaluar.SAC(0.333)
    def Letargico(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(3)
        paramEvaluar.SAC(0.666)
    def Inconsciente(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAT(3)
        paramEvaluar.SAC(0.666)
        
class TonoOpcion():
    def Eutonico(self):
        paramEvaluar.TEPA(True)
    def Hipotonico(self):
        paramEvaluar.TEPA(False)
        
class VisualOpcion():
    def Mantiene(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAC(0.0)
    def NoMantiene(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAC(0.333)
    def NoDirige(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAC(0.666)
        
class LlantoOpcion():
    def Fuerte(self):
        paramEvaluar.TEPA(True)
        paramEvaluar.SAC(0.0)
    def Debil(self):
        paramEvaluar.TEPA(False)
        paramEvaluar.SAC(0.333)

class ConsolableOpcion():
    def Consolable(self):
        paramEvaluar.TEPC(True)
        paramEvaluar.SAT(1)
        paramEvaluar.SAC(0.0)
    def Inconsolable(self):
        paramEvaluar.TEPC(False)
        paramEvaluar.SAT(2)
        paramEvaluar.SAC(0.666)
        
class RuidoRespiratorioOpcion():
    def Presentes(self):
        def ruidoElegido(*args):
            comboRuidoElegido= comboRuidos.get()
            if comboRuidoElegido== "Gruñido":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(3)
                paramEvaluar.SAC(0.333)
                return True
            elif comboRuidoElegido== "Estridor":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(3)
                paramEvaluar.SAC(0.333)
                return True
            elif comboRuidoElegido== "Disfonia":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(3)
                paramEvaluar.SAC(0.333)
                return True
            elif comboRuidoElegido== "Quejido":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(3)
                paramEvaluar.SAC(0.333)
                return True
            elif comboRuidoElegido== "Silibancia":
                paramEvaluar.TEPR(False)
                paramEvaluar.SAT(3)
                paramEvaluar.SAC(0.333)
                return True

        comboRuidos= ttk.Combobox(self)
        comboRuidos['values'] =("Gruñido", "Estridor", "Disfonia", "Quejido", "Silibancia") 
        comboRuidos.state(["readonly"])
        comboRuidos.bind("<<ComboboxSelected>>", ruidoElegido)
        comboRuidos.pack()
                    
    def Ausentes(self):
        paramEvaluar.TEPR(True)
        paramEvaluar.SAT(0)
        paramEvaluar.SAC(0.0)   
        
class DificultadRespiratoriaOpcion():
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

class PosicionPatologicaOpcion():
    def Si(self):
        def posicionElegida(*args):
            comboPosicionElegida= comboPosicion.get()
            
            if comboPosicionElegida== "Tripode":
                paramEvaluar.TEPR(False)
            elif comboPosicionElegida=="Olfateo":
                paramEvaluar.TEPR(False)
            elif comboPosicionElegida=="Cabeceo":
                paramEvaluar.TEPR(False)
                    
        comboPosicion= ttk.Combobox(self)
        comboPosicion['values']= ("Tripode","Olfateo","Caebeceo")
        comboPosicion.state(["readonly"])
        comboPosicion.bind("<<ComboboxSelected>>", posicionElegida)
        comboPosicion.pack()
        
    def No(self):
        paramEvaluar.TEPR(True)
        paramEvaluar.SAT(0)
        paramEvaluar.SAC(0.0)
        
class AntecedentesOpcion():
    def Presentes(self):
        paramEvaluar.SAC(0.333)
    def Negados(self):
        paramEvaluar.SAC(0.0)
   
class AbusoOpcion():
    def Presente(self):
        paramEvaluar.SAC(0.333)
    def Ausente(self):
        paramEvaluar.SAC(0.0)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
        
        
        