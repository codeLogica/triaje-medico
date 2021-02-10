#En esta modulo se reciben los resultados de analizar los valores clinicos. Se analiza los nuevos valores y se arroja un resultado de codigo de color segun la gravedad...  
#Tenemos un inicializador con los parametros a checar, junto con las variables del Triangulo de Evaluacion Pediatrica. Un metodo que verifica que se tengan todos los datos completos y finalmente uno que arroje un resultado final. 

class CodigoColor():    
    def __init__(self):
        self.codigoRojo= 0
        self.codigoNaranja= 0
        self.codigoAmarillo= 0
        self.codigoVerde= 0
        self.codigoAzul= 0
        
        self.valorFinalTEPA= None
        self.valorFinalTEPC= None
        self.valorFinalTEPR= None
    
    def TrianguloEvaluacionPediatricaApariencia(self, TEPA):
        self.valorFinalTEPA= TEPA
        self.ValidarValoresTriangulo()
        return self.valorFinalTEPA
    def TrianguloEvaluacionPediatricaCirculacion(self, TEPC):
        self.valorFinalTEPC= TEPC
        self.ValidarValoresTriangulo()
        return self.valorFinalTEPC
    def TrianguloEvaluacionPediatricaRespiracion(self, TEPR):
        self.valorFinalTEPR= TEPR
        self.ValidarValoresTriangulo()
        return self.valorFinalTEPR
    
    def ValidarValoresTriangulo(self):
        if self.valorFinalTEPA != None and self.valorFinalTEPC != None and self.valorFinalTEPR != None:
            self.TrianguloEvaluacionPediatrica()
        else:
            pass

    def TrianguloEvaluacionPediatrica(self):
        if self.valorFinalTEPA== True and self.valorFinalTEPC== True and self.valorFinalTEPR== True:
            self.codigoAzul=+ 1
            return self.codigoAzul
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== True and self.valorFinalTEPR== True:
            self.codigoRojo=+ 1
            return self.codigoRojo
        elif self.valorFinalTEPA== True and self.valorFinalTEPC== True and self.valorFinalTEPR== False:
            self.codigoNaranja=+ 1
            return self.codigoNaranja
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== True and self.valorFinalTEPR== False:
            self.codigoRojo=+ 1
            return self.codigoRojo
        elif self.valorFinalTEPA== True and self.valorFinalTEPC== False and self.valorFinalTEPR== True:
            self.codigoNaranja=+ 1
            return self.codigoNaranja
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== False and self.valorFinalTEPR== True:
            self.codigoRojo=+ 1
            return self.codigoRojo
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== False and self.valorFinalTEPR== False:
            self.codigoRojo=+ 1
            return self.codigoRojo
    
    def SistemaAlertaTemprana(self, valorFinalSAT):
        self.valorFinalSAT= valorFinalSAT
                
        if self.valorFinalSAT==0:
            self.codigoAzul=+ 1
        elif self.valorFinalSAT==1:
            self.codigoVerde=+ 1
        elif self.valorFinalSAT==2:
            self.codigoAmarillo=+ 1
        elif self.valorFinalSAT==3:
            self.codigoNaranja=+ 1
        elif self.valorFinalSAT>3:
            self.codigoRojo=+ 1

    def SaveChild(self, valorFinalSAC):
        self.valorFinalSAC= valorFinalSAC
                
        if self.valorFinalSAC>0 and self.valorFinalSAC<1:
            self.codigoAzul=+1
        elif self.valorFinalSAC>1 and self.valorFinalSAC<2:
            self.codigoVerde=+1
        elif self.valorFinalSAC>2 and self.valorFinalSAC<3:
            self.codigoAmarillo=+1
        elif self.valorFinalSAC>3 and self.valorFinalSAC<4:
            self.codigoNaranja=+1
        elif self.valorFinalSAC >4:
            self.codigoRojo=+1  