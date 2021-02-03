class CodigoColor():    
    def __init__(self):
        self.codigoRojo= 0
        self.codigoNaranja= 0
        self.codigoAmarillo= 0
        self.codigoVerde= 0
        self.codigoAzul= 0
    
    def TrianguloEvaluacionPediatrica(self, TEPA, TEPC, TEPR):
        self.valorFinalTEPA= TEPA
        self.valorFinalTEPC= TEPC
        self.valorFinalTEPR= TEPR
        
        if self.valorFinalTEPA== True and self.valorFinalTEPC== True and self.valorFinalTEPR== True:
            self.codigoAzul=+ 1
            print(self.codigoAzul)
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== True and self.valorFinalTEPR== True:
            self.codigoRojo=+ 1
            print(self.codigoRojo)
        elif self.valorFinalTEPA== True and self.valorFinalTEPC== True and self.valorFinalTEPR== False:
            self.codigoNaranja=+ 1
            print(self.codigoNaranja)
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== True and self.valorFinalTEPR== False:
            self.codigoRojo=+ 1
            print(self.codigoRojo)
        elif self.valorFinalTEPA== True and self.valorFinalTEPC== False and self.valorFinalTEPR== True:
            self.codigoNaranja=+ 1
            print(self.codigoNaranja)
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== False and self.valorFinalTEPR== True:
            self.codigoRojo=+ 1
            print(self.codigoRojo)
        elif self.valorFinalTEPA== False and self.valorFinalTEPC== False and self.valorFinalTEPR== False:
            self.codigoRojo=+ 1
            print(self.codigoRojo)
    
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
        
        if self.valorFinalSAC==0 and self.valorFinalSAC<1:
            self.codigoAzul=+1
        elif self.valorFinalSAC==1 and self.valorFinalSAC<2:
            self.codigoVerde=+1
        elif self.valorFinalSAC==2 and self.valorFinalSAC<3:
            self.codigoAmarillo=+1
        elif self.valorFinalSAC==3 and self.valorFinalSAC<4:
            self.codigoNaranja=+1
        elif self.valorFinalSAC >=4:
            self.codigoRojo=+1  
    
        