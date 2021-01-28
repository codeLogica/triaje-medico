from Mod_Evaluar import Parametros

paramEvaluar = Parametros.Evaluar()

class Opciones():    
    def __init__(self):
        self.opcionDespierto= False
        self.opcionSomnoliento= False
        self.opcionIrritable= False
        self.opcionNoDuerme= False
        self.opcionCrisis= False

    def Despierto(self):
        self.opcionDespierto= True
        self.eleccionConciencia()
    def Somnoliento(self):
        self.opcionSomnoliento= True
        self.eleccionConciencia()
    def Irritable(self):
        self.opcionIrritable= True
        self.eleccionConciencia()
    def NoDuerme(self):
        self.opcionNoDuerme= True 
        self.eleccionConciencia()
    def Crisis(self):
        self.opcionCrisis= True
        self.eleccionConciencia()

    def eleccionConciencia(self):
        if (self.opcionDespierto):
            paramEvaluar.TEPA(True)
            paramEvaluar.SAT(+0)
            paramEvaluar.SAC(+0)
        elif (self.opcionSomnoliento):
            paramEvaluar.TEPA(True)
            paramEvaluar.SAT(+1)
            paramEvaluar.SAC(+0)
        elif (self.opcionIrritable):
            paramEvaluar.TEPA(False)
            paramEvaluar.SAT(+2)
            paramEvaluar.SAC(+0.3)
        elif (self.opcionNoDuerme):
            paramEvaluar.TEPA(False)
            paramEvaluar.SAT(+3)
            paramEvaluar.SAC(+1)
        elif (self.opcionCrisis):     
            paramEvaluar.TEPA(False)
            paramEvaluar.SAT(+3)
            paramEvaluar.SAC(+0.3)   
                
