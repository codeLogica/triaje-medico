# Se reciben los valores parasados como argumentos y realiza la suma.         
class Evaluar():       
    def __init__(self):
        self.valorInicialTEPA= True
        self.valorInicialTEPR= True
        self.valorInicialTEPC= True
        self.valorInicialSAT= 0
        self.valorInicialSAC= 0
        
        self.valorFinalSAT= 0
        self.valorFinalSAc= 0
        
        self.valorAnadidoTEPA= 0
        self.valorAnadidoTEPR= 0
        self.valorAnadidoTEPC= 0
        self.valorAnadidoSAT= 0
        self.valorAnadidoSAC= 0
        
    def TEPA(self, valorAnadidoTEPA):
        if  self.valorInicialTEPA != valorAnadidoTEPA:
            self.valorAnadidoTEPA = valorAnadidoTEPA
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Apariencia {self.valorAnadidoTEPA}")
        return self.valorAnadidoTEPA
    
    def TEPR(self, valorAnadidoTEPR):
        if  self.valorInicialTEPR != valorAnadidoTEPR:
            self.valorAnadidoTEPR = valorAnadidoTEPR
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Respiracion {self.valorAnadidoTEPR}")
        return self.valorAnadidoTEPR
    
    def TEPC(self, valorAnadidoTEPC):
        if  self.valorInicialTEPC == valorAnadidoTEPC:
            self.valorAnadidoTEPC = valorAnadidoTEPC
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Circulacion {self.valorAnadidoTEPC}")
        return self.valorAnadidoTEPC
    
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
            
    
##    self.codigoAzul = 0
##    self.codigoVerde = 0
##    self.codigoAmarillo = 0
##    self.codigoNaranja = 0
##    self.codigoRojo = 0
##    codigos= 0