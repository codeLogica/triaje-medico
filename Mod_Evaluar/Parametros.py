# Se reciben los valores parasados como argumentos y realiza la suma. 

class Evaluar():
    def __init__(self):
        self.valorInicial= 0
        self.valorTotal= 0
        
    def TEPA(self, valorAñadido):
        self.valorAñadido = valorAñadido
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Apariencia {self.valorAñadido}")
        return self.valorAñadido
    def TEPR(self, valorAñadido):
        self.valorAñadido = valorAñadido
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Respiracion {self.valorAñadido}")
        return self.valorAñadido
    def TEPC(self, valorAñadido):
        self.valorAñadido = valorAñadido
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Circulacion {self.valorAñadido}")
        return self.valorAñadido
    
    def SAT(self, valorAñadido):
        self.valorAñadido = valorAñadido
    
        if self.valorInicial == 0:
            self.valorTotal= self.valorInicial + self.valorAñadido
            self.valorInicial=+ 1
            print(f"Soy el valor del Sistema Alerta Temprana {self.valorTotal}")
            return self.valorTotal
        else:
            self.valorTotal = self.valorTotal + self.valorAñadido
            print(f"Soy el valor del Sistema Alerta Temprana {self.valorTotal}")
            return self.valorTotal
            
    def SAC(self, valorAñadido):
        self.valorAñadido = valorAñadido
    
        if self.valorInicial == 0:
            self.valorTotal= self.valorInicial + self.valorAñadido
            self.valorInicial=+ 1
            print(f"Soy el valor de Save a Child {self.valorTotal}")
            return self.valorTotal
        else:
            self.valorTotal = self.valorTotal + self.valorAñadido
            print(f"Soy el valor de Save a Child {self.valorTotal}")
            return self.valorTotal
            
    
##    self.codigoAzul = 0
##    self.codigoVerde = 0
##    self.codigoAmarillo = 0
##    self.codigoNaranja = 0
##    self.codigoRojo = 0
##    codigos= 0