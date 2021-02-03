from Mod_Eva import Resultado

resultado = Resultado.CodigoColor()
# Se reciben los valores parasados como argumentos y realiza la suma que dara como resultado un codigo de color. 
class Evaluar():       
    def __init__(self):
        self.valorInicialTEPA= True
        self.valorInicialTEPR= True
        self.valorInicialTEPC= True
        self.valorInicialSAT= 0
        self.valorInicialSAC= 0
        
        self.valorFinalTEPA= None
        self.valorFinalTEPR= None
        self.valorFinalTEPC= None
        self.valorFinalSAT= 0
        self.valorFinalSAC= 0
        
        self.valorAnadidoTEPA= 0
        self.valorAnadidoTEPR= 0
        self.valorAnadidoTEPC= 0
        self.valorAnadidoSAT= 0
        self.valorAnadidoSAC= 0
        
        resultado.TrianguloEvaluacionPediatrica(self.valorFinalTEPA, 
                                                self.valorFinalTEPC, 
                                                self.valorFinalTEPR)
        
        resultado.SistemaAlertaTemprana(self.valorFinalSAT)
        
        resultado.SaveChild(self.valorFinalSAC)

        
    def TEPA(self, valorAnadidoTEPA):
        if  self.valorInicialTEPA != valorAnadidoTEPA:
            self.valorFinalTEPA = valorAnadidoTEPA
        else:
            self.valorFinalTEPA= self.valorInicialTEPA
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Apariencia {self.valorFinalTEPA}")
        return self.valorFinalTEPA
    
    def TEPR(self, valorAnadidoTEPR):
        if  self.valorInicialTEPR != valorAnadidoTEPR:
            self.valorFinalTEPR = valorAnadidoTEPR
        else:
            self.valorFinalTEPR= self.valorInicialTEPR
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Respiracion {self.valorFinalTEPR}")
        return self.valorFinalTEPR
    
    def TEPC(self, valorAnadidoTEPC):
        if  self.valorInicialTEPC == valorAnadidoTEPC:
            self.valorFinalTEPC = valorAnadidoTEPC
        else:
            self.valorFinalTEPC= self.valorInicialTEPC
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Circulacion {self.valorFinalTEPC}")
        return self.valorFinalTEPC
    
    def SAT(self, valorAnadidoSAT):
        self.valorAnadidoSAT = valorAnadidoSAT
        if self.valorInicialSAT == 0:
            self.valorFinalSAT= self.valorInicialSAT + self.valorAnadidoSAT
            self.valorInicialSAT=+ 1
            print(f"Soy el valor del Sistema Alerta Temprana {self.valorFinalSAT}")
            return self.valorFinalSAT
        else:
            self.valorFinalSAT += self.valorAnadidoSAT
            print(f"Soy el valor del Sistema Alerta Temprana {self.valorFinalSAT}")
            return self.valorFinalSAT
            
    def SAC(self, valorAnadidoSAC):
        self.valorAnadidoSAC = valorAnadidoSAC
    
        if self.valorInicialSAC == 0:
            self.valorFinalSAC= self.valorInicialSAC + self.valorAnadidoSAC
            self.valorInicialSAC=+ 1
            print(f"Soy el valor de Save a Child {self.valorFinalSAC}")
            return self.valorFinalSAC
        else:
            self.valorFinalSAC += self.valorAnadidoSAC
            print(f"Soy el valor de Save a Child {self.valorFinalSAC}")
            return self.valorFinalSAC
            
    
