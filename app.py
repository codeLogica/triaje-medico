import tkinter as tk
from tkinter import PhotoImage

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(PaginaGeneral)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class PaginaGeneral(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tituloPrograma= tk.Label(self, text= "PROGRAMA DE EVALUACION PEDIATRICA")
        tituloPrograma.config(fg="blue", bg="light blue", font=("Verdana", 40))
        tituloPrograma.pack()
        introduccionPrograma1= tk.Label(self, text= "El siguiente programa es una DEMO para observar la funcionalidad de un triage computarizado. ").pack()
        introduccionPrograma2= tk.Label(self, text="Favor de informar cualquier error durante su uso.").pack()
        introduccionPrograma3= tk.Label(self, text="No nos hacemos responsables de los daños causados.").pack()
        self.imagen= tk.PhotoImage(file= ["bebe.gif"], format="gif -index 2")
        introduccionPrograma4= tk.Label(self, image= self.imagen).pack()

        botonSiguienteGeneral= tk.Button(self, text= "INICIO", command=lambda: master.switch_frame(PaginaConciencia))
        botonSiguienteGeneral.pack()

class PaginaConciencia(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloGeneralConciencia= tk.Label(self, text= "Aspecto General")
        tituloGeneralConciencia.config(fg="blue", bg="light blue", font=("Arial", 30))
        tituloGeneralConciencia.grid(row=0, column=3)

        subtituloFrameConciencia= tk.Label(self, text= "Nivel de Conciencia")
        subtituloFrameConciencia.config(fg="blue", bg="light blue", font=("Arial", 20))
        subtituloFrameConciencia.grid(row=1, column=3)

        self.imagenDespierto= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaDespierto.png")
        self.imagenSomnoliento= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaSomnoliento.png")
        self.imagenIrritable= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaIrritable.png")
        self.imagenNoDuerme= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaNo.png")
        self.imagenCrisis= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaCrisis.png")

        llamadaConciencia= Conciencia.Opciones()
        botonDespierto= tk.Button(self, image= self.imagenDespierto, command= lambda:[llamadaConciencia.Despierto, master.switch_frame(PaginaColorPiel)]).grid(row=3, column=2)
        botonSomnoliento= tk.Button(self, image= self.imagenSomnoliento, command= lambda:[llamadaConciencia.Somnoliento, master.switch_frame(PaginaColorPiel)]).grid(row=3, column=3)
        botonIrritable= tk.Button(self, image= self.imagenIrritable, command= lambda:[llamadaConciencia.Irritable, master.switch_frame(PaginaColorPiel)]).grid(row=3, column=5)
        botonNoDuerme= tk.Button(self, image= self.imagenNoDuerme, command= lambda:[llamadaConciencia.NoDuerme, master.switch_frame(PaginaColorPiel)]).grid(row=4, column=2)
        botonCrisis= tk.Button(self, image= self.imagenCrisis, command= lambda:[llamadaConciencia.Crisis, master.switch_frame(PaginaColorPiel)]).grid(row=4, column=5)

class PaginaColorPiel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFramePiel= tk.Label(self, text= "Coloracion de la Piel")
        tituloFramePiel.grid(row=0, column=3)

        self.imagenPielRosada= tk.PhotoImage(file= "Imagenes/Piel/pielRosada.png")
        self.imagenPielPalida= tk.PhotoImage(file= "Imagenes/Piel/pielPalida.png")
        self.imagenPielCianotica= tk.PhotoImage(file= "Imagenes/Piel/pielCianotica.png")
        self.imagenPielRubicunda= tk.PhotoImage(file= "Imagenes/Piel/pielRubicunda.png")
        self.imagenPielMarmorea= tk.PhotoImage(file= "Imagenes/Piel/pielMarmorea.png")
        self.imagenPielPurpurica= tk.PhotoImage(file= "Imagenes/Piel/pielPurpurica.png")

        llamadaColoracionPiel= ColoracionPiel.OpcionesColoracionPiel()
        botonRosada= tk.Button(self, image= self.imagenPielRosada, command= lambda:[llamadaColoracionPiel.Rosada, master.switch_frame(PaginaHidraPiel)]).grid(row=1, column=2)
        botonPalida= tk.Button(self, image= self.imagenPielPalida,command= lambda:[llamadaColoracionPiel.Palida, master.switch_frame(PaginaHidraPiel)]).grid(row=1, column=3)
        botonCianotica= tk.Button(self, image= self.imagenPielCianotica,command= lambda:[llamadaColoracionPiel.Cianotica, master.switch_frame(PaginaHidraPiel)]).grid(row=1, column=4)
        botonRubicunda= tk.Button(self, image= self.imagenPielRubicunda,command= lambda:[llamadaColoracionPiel.Rubicunda, master.switch_frame(PaginaHidraPiel)]).grid(row=2, column=2)
        botonMarmorea= tk.Button(self, image= self.imagenPielMarmorea,command= lambda:[llamadaColoracionPiel.Marmorea, master.switch_frame(PaginaHidraPiel)]).grid(row=2, column=3)
        botonPurpurica= tk.Button(self, image= self.imagenPielPurpurica,command= lambda:[llamadaColoracionPiel.Purpurica, master.switch_frame(PaginaHidraPiel)]).grid(row=2, column=4)

class PaginaHidraPiel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFramePiel= tk.Label(self, text= "Piel")
        tituloHidraFramePiel.grid()

        self.imagenHidraPielNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPielNormal.png")
        self.imagenHidraPielSeca= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPielSeca.png")

        llamadaHidraPiel= HidraPiel.OpcionesHidraPiel()
        botonHidraPielNormal= tk.Button(self, image= self.imagenHidraPielNormal,command= lambda:[llamadaHidraPiel.PielNormal, master.switch_frame(PaginaHidraMucosa)]).grid()
        botonHidraPielSeca= tk.Button(self, image= self.imagenHidraPielSeca, command= lambda:[llamadaHidraPiel.PielSeca, master.switch_frame(PaginaHidraMucosa)]).grid()

class PaginaHidraMucosa(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameMucosas= tk.Label(self, text= "Mucosa")
        tituloHidraFrameMucosas.grid()

        self.imagenHidraMucosaNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraMucosaNormal.png")
        self.imagenHidraMucosaSeca= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraMucosaSeca.png")

        llamadaHidraMucosa= HidraMucosa.Opciones()
        botonHidraMucosaNormal= tk.Button(self, image= self.imagenHidraMucosaNormal, command= lambda:[llamadaHidraMucosa.MucosaNormal, master.switch_frame(PaginaHidraOjos)]).grid()
        botonHidraMucosaSeca= tk.Button(self, image= self.imagenHidraMucosaSeca, command= lambda:[llamadaHidraMucosa.MucosaSeca, master.switch_frame(PaginaHidraOjos)]).grid()

class PaginaHidraOjos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameOjos= tk.Label(self, text= "Ojos")
        tituloHidraFrameOjos.grid()

        self.imagenHidraOjosNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraOjosNormal.png")
        self.imagenHidraOjosHundidos= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraOjosHundidos.png")

        llamadaHidraOjos= HidraOjos.Opciones()
        botonHidraOjosNormal= tk.Button(self, image= self.imagenHidraOjosNormal, command= lambda:[llamadaHidraOjos.OjosNormal, master.switch_frame(PaginaPliegue)]).grid()
        botonHidraOjosHundidos= tk.Button(self, image= self.imagenHidraOjosHundidos, command= lambda:[llamadaHidraOjos.OjosHundidos, master.switch_frame(PaginaPliegue)]).grid()

class PaginaPliegue(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFramePliegue= tk.Label(self, text= "Pliegue")
        tituloHidraFramePliegue.grid()

        self.imagenHidraPlieguePositivo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPlieguePositivo.png")
        self.imagenHidraPliegueNegativo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPliegueNegativo.png")

        llamadaHidraPliegue= Pliegue.OpcionesPliegue()
        botonHidraPlieguePositivo= tk.Button(self, image= self.imagenHidraPlieguePositivo, command= lambda:[llamadaHidraPliegue.PlieguePositivo, master.switch_frame(PaginaHidraVomito)]).grid()
        botonHidraPliegueNegativo= tk.Button(self, image= self.imagenHidraPliegueNegativo, command= lambda:[llamadaHidraPliegue.PliegueNegativo, master.switch_frame(PaginaHidraVomito)]).grid()

class PaginaHidraVomito(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameVomito= tk.Label(self, text= "Vomito")
        tituloHidraFrameVomito.grid()

        self.imagenHidraVomitoPresente= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraVomitoPresente.png")
        self.imagenHidraVomitoAusente= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraVomitoAusente.png")

        llamadaHidraVomito= Vomito.OpcionesVomito()
        botonHidraVomitoPresente= tk.Button(self, image= self.imagenHidraVomitoPresente, command= lambda:[llamadaHidraVomito.VomitoPresente, master.switch_frame(PaginaHidraTolerancia)]).grid()
        botonHidraVomitoAusente= tk.Button(self, image= self.imagenHidraVomitoAusente, command= lambda:[llamadaHidraVomito.VomitoAusente, master.switch_frame(PaginaHidraTolerancia)]).grid()

class PaginaHidraTolerancia(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameTolerancia= tk.Label(self, text= "¿Tolera Via Oral?")
        tituloHidraFrameTolerancia.grid()

        self.imagenHidraToleranciaSi= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraToleranciaSi.png")
        self.imagenHidraToleranciaNo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraToleranciaNo.png")

        llamadaTolerancia= Tolerancia.OpcionesTolerancia()
        botonHidraToleranciaSi= tk.Button(self, image= self.imagenHidraToleranciaSi, command= lambda:[llamadaTolerancia.SiTolera, master.switch_frame(PaginaActividad)]).grid()
        botonHidraToleranciaNo= tk.Button(self, image= self.imagenHidraToleranciaNo, command= lambda:[llamadaTolerancia.NoTolera, master.switch_frame(PaginaActividad)]).grid()

class PaginaActividad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameActividad= tk.Label(self, text= "Actividad")
        tituloFrameActividad.grid(row=1, column=2)

        self.imagenJuega= tk.PhotoImage(file= "Imagenes\Actividad\cactividadJuega.png")
        self.imagenConfundido= tk.PhotoImage(file= "Imagenes\Actividad\cactividadConfundido.png")
        self.imagenLetargico= tk.PhotoImage(file= "Imagenes\Actividad\cactividadLetargico.png")
        self.imagenInconsciente= tk.PhotoImage(file= "Imagenes\Actividad\cactividadInconsciente.png")

        llamadaActividad= Actividad.OpcionesActividad()
        botonJuega= tk.Button(self, image= self.imagenJuega, command= lambda:[llamadaActividad.Juega, master.switch_frame(PaginaTono)]).grid(row=2, column=1)
        botonConfundido= tk.Button(self, image= self.imagenConfundido, command= lambda:[llamadaActividad.Confundido, master.switch_frame(PaginaTono)]).grid(row=2, column=2)
        botonLetargico= tk.Button(self, image= self.imagenLetargico, command= lambda:[llamadaActividad.Letargico, master.switch_frame(PaginaTono)]).grid(row=2, column=3)
        botonInconsciente= tk.Button(self, image= self.imagenInconsciente, command= lambda:[llamadaActividad.Inconsciente, master.switch_frame(PaginaTono)]).grid(row=2, column=4)

class PaginaTono(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameTono= tk.Label(self, text= "Tono")
        tituloFrameTono.pack()

        self.imagenEutonico= tk.PhotoImage(file= "Imagenes\Tono\ctonoEutonico.png")
        self.imagenHipotonico= tk.PhotoImage(file= "Imagenes\Tono\ctonoHipotonico.png")

        llamadaTono= Tono.OpcionesTono()
        botonEutonico= tk.Button(self, image= self.imagenEutonico,command= lambda:[llamadaTono.Eutonico, master.switch_frame(PaginaVisual)]).pack()
        botonHipotonico= tk.Button(self, image= self.imagenHipotonico,command= lambda:[llamadaTono.Hipotonico, master.switch_frame(PaginaVisual)]).pack()

class PaginaVisual(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameVisual= tk.Label(self, text= "Contacto Visual")
        tituloFrameVisual.pack()

        self.imagenMantiene= tk.PhotoImage(file= "Imagenes\Visual\cvisualMantiene.png")
        self.imagenNoMantiene= tk.PhotoImage(file= "Imagenes\Visual\cvisualNoMantiene.png")
        self.imagenNoDirige= tk.PhotoImage(file= "Imagenes\Visual\cvisualNoDirige.png")

        llamadaVisual= Visual.OpcionesVisual()
        botonMantiene= tk.Button(self, image= self.imagenMantiene,command= lambda:[llamadaVisual.Mantiene, master.switch_frame(PaginaLlanto)]).pack()
        botonNoMantiene= tk.Button(self, image= self.imagenNoMantiene,command= lambda:[llamadaVisual.NoMantiene, master.switch_frame(PaginaLlanto)]).pack()
        botonNoDirige= tk.Button(self, image= self.imagenNoDirige,command= lambda:[llamadaVisual.NoDirige, master.switch_frame(PaginaLlanto)]).pack()

class PaginaLlanto(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameLlanto= tk.Label(self, text= "Lenguaje o Llanto")
        tituloFrameLlanto.pack()

        self.imagenLlantoFuerte= tk.PhotoImage(file= "Imagenes\Llanto\llantoFuerte.png")
        self.imagenLlantoDebil= tk.PhotoImage(file= "Imagenes\Llanto\llantoDebil.png")

        llamadaLlanto= Llanto.OpcionesLlanto()
        botonLlantoFuerte= tk.Button(self, image= self.imagenLlantoFuerte,command= lambda:[llamadaLlanto.LlantoFuerte, master.switch_frame(PaginaConsolabilidad)]).pack()
        botonLlantoDebil= tk.Button(self, image= self.imagenLlantoDebil,command= lambda:[llamadaLlanto.LlantoDebil, master.switch_frame(PaginaConsolabilidad)]).pack()

class PaginaConsolabilidad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameConsolabilidad= tk.Label(self, text= "Consolabilidad")
        tituloFrameConsolabilidad.pack()

        self.imagenLlantoConsolable= tk.PhotoImage(file= "Imagenes\Llanto\llantoConsolable.png")
        self.imagenLlantoInconsolable= tk.PhotoImage(file= "Imagenes\Llanto\llantoInconsolable.png")

        llamadaConsolabilidad= Consolabilidad.OpcionesConsolabilidad()
        botonConsolabilidad= tk.Button(self, image= self.imagenLlantoConsolable, command= lambda:[llamadaConsolabilidad.Consolable, master.switch_frame(PaginaRuidos)]).pack()
        botonInconsolabilidad= tk.Button(self, image= self.imagenLlantoInconsolable, command= lambda:[llamadaConsolabilidad.Inconsolable, master.switch_frame(PaginaRuidos)]).pack()

class PaginaRuidos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameRespiratorio1= tk.Label(self, text= "Respiratorio")
        tituloFrameRespiratorio1.pack()
        tituloFrameRuidos= tk.Label(self, text= "Ruidos Patologicos")
        tituloFrameRuidos.pack()

        self.imagenRespiracionRuidosSi= tk.PhotoImage(file= "Imagenes\Respiracion\cruidosSi.png")
        self.imagenRespiracionRuidosNo= tk.PhotoImage(file= "Imagenes\Respiracion\cruidosNo.png")

        llamadaRuidos= Ruidos.OpcionesRuidos()
        botonRuidosSi= tk.Button(self, image= self.imagenRespiracionRuidosSi, command= lambda:[llamadaRuidos.RuidosSi, master.switch_frame(PaginaDificultad)]).pack()
        botonRuidosNo= tk.Button(self, image= self.imagenRespiracionRuidosNo, command= lambda:[llamadaRuidos.RuidosNo, master.switch_frame(PaginaDificultad)]).pack()

class PaginaDificultad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameDificultad= tk.Label(self, text= "Datos de Dificultad")
        tituloFrameDificultad.pack()

        self.imagenRespiracionDificultadSi= tk.PhotoImage(file= "Imagenes\Respiracion\dificultadSi.png")
        self.imagenRespiracionDificultadNo= tk.PhotoImage(file= "Imagenes\Respiracion\dificultadNo.png")

        llamadaDificultad= Dificultad.OpcionesDificultad()
        botonDificultadSi= tk.Button(self, image= self.imagenRespiracionDificultadSi, command= lambda:[llamadaDificultad.DificultadSi, master.switch_frame(PaginaPosicion)]).pack()
        botonDificultadNo= tk.Button(self, image= self.imagenRespiracionDificultadNo, command= lambda:[llamadaDificultad.DificultadNo, master.switch_frame(PaginaPosicion)]).pack()

class PaginaPosicion(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFramePosicion= tk.Label(self, text= "Posicion Patologica")
        tituloFramePosicion.pack()

        self.imagenRespiracionPosicionSi= tk.PhotoImage(file= "Imagenes\Respiracion\posicionSi.png")
        self.imagenRespiracionPosicionNo= tk.PhotoImage(file= "Imagenes\Respiracion\posicionNo.png")

        llamadaPosicion= Posicion.OpcionesPosicion()
        botonPosicionSi= tk.Button(self, image= self.imagenRespiracionPosicionSi, command= lambda:[llamadaPosicion.PosicionSi, master.switch_frame(PaginaAntecedentes)]).pack()
        botonPosicionNo= tk.Button(self, image= self.imagenRespiracionPosicionNo, command= lambda:[llamadaPosicion.PosicionNo, master.switch_frame(PaginaAntecedentes)]).pack()

class PaginaAntecedentes(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameAntecedentes= tk.Label(self, text= "Antecedentes")
        tituloFrameAntecedentes.pack()
        subtituloFrameAntecedentes= tk.Label(self, text="Enfermedades Cronico-Degenerativas o Uso de Esteroides")
        subtituloFrameAntecedentes.pack()

        self.imagenAntecedentesSi= tk.PhotoImage(file= "Imagenes\Antecedentes\cantecedentesSi.png")
        self.imagenAntecedentesNo= tk.PhotoImage(file= "Imagenes\Antecedentes\cantecedentesNo.png")

        llamadaAntecedentes= Antecedentes.OpcionesAntecedentes()
        botonAntecedentesSi= tk.Button(self, image= self.imagenAntecedentesSi, command= lambda:[llamadaAntecedentes.AntecedentesSi, master.switch_frame(PaginaAbuso)]).pack()
        botonAntecedentesNo= tk.Button(self, image= self.imagenAntecedentesNo, command= lambda:[llamadaAntecedentes.AntecedentesNo, master.switch_frame(PaginaAbuso)]).pack()

class PaginaAbuso(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameAbuso= tk.Label(self, text= "Datos de Abuso")
        tituloFrameAbuso.pack()

        self.imagenAbusoSi= tk.PhotoImage(file= "Imagenes\Antecedentes\cabusoSi.png")
        self.imagenAbusoNo= tk.PhotoImage(file= "Imagenes\Antecedentes\cabusoNo.png")

        llamadaAbuso= Abuso.OpcionesAbuso()
        botonAbusoSi= tk.Button(self, image= self.imagenAbusoSi, command= lambda:[llamadaAbuso.AbusoSi, master.switch_frame(PaginaResultado)]).pack()
        botonAbusoNo= tk.Button(self, image= self.imagenAbusoNo, command= lambda:[llamadaAbuso.AbusoNo, master.switch_frame(PaginaResultado)]).pack()

class PaginaResultado(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()