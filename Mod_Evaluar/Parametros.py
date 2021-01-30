class Evaluar():
    def TEPA(self, valorAñadido):
        self.valorAñadido = valorAñadido
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Apariencia {self.valorAñadido}")
    def TEPR(self, valorAñadido):
        self.valorAñadido = valorAñadido
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Respiracion {self.valorAñadido}")
    def TEPC(self, valorAñadido):
        self.valorAñadido = valorAñadido
        print(f"Soy el valor del Triangulo Evaluacion Pediatrica Circulacion {self.valorAñadido}")
    def SAT(self, valorAñadido):
        self.valorInicial= 0
        self.valorTotal= 0
    
        if self.valorInicial == 0:
            self.valorTotal= self.valorInicial + self.valorAñadido
            self.valorInicial = self.valorInicial + 1
        else:
            self.valorTotal = self.valorTotal + self.valorAñadido
            
        print(f"Soy el valor del Sistema Alerta Temprana {self.valorTotal}")
        
    def SAC(self, valorAñadido):
        self.valorInicial= 0.0
        self.valorTotal= 0
    
        if self.valorInicial == 0:
            self.valorTotal= self.valorInicial + self.valorAñadido
            self.valorInicial = self.valorInicial + 1
        else:
            self.valorTotal = self.valorTotal + self.valorAñadido
            
        print(f"Soy el valor de Save a Child {self.valorTotal}")
    
##    self.codigoAzul = 0
##    self.codigoVerde = 0
##    self.codigoAmarillo = 0
##    self.codigoNaranja = 0
##    self.codigoRojo = 0
##    codigos= 0