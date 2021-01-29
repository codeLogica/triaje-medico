import tkinter as tk
import tkinter as ttk
from tkinter import PhotoImage
from Mod_Evaluar import Conciencia
from Mod_Evaluar import ColoracionPiel
from Mod_Evaluar import HidraPiel
from Mod_Evaluar import HidraMucosa
from Mod_Evaluar import HidraOjos
from Mod_Evaluar import HidraPliegue
from Mod_Evaluar import HidraVomito
from Mod_Evaluar import HidraTolerancia
from Mod_Evaluar import Actividad

#Esta seccion sirve para camibiar entre frames durante la ejecucion del programa. 
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
        
#Esta es la pagina principal del programa, donde se muestra infomracion relevante. Se inicializa el frame y dentro encontramos los widgets necesarios. Se basa en una serie de imagenes con los parametros a analizar y dependiendo de la seleccion se evaluan en otro modulo. 
#Se sigue el siguiente esquema en todos los frames:
#Inizialicacion --> informacion --> imagenes --> llamada al modulo con el parametro a evaluar --> botones 
class PaginaGeneral(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tituloPrograma= tk.Label(self, text= "PROGRAMA DE EVALUACION PEDIATRICA")
        tituloPrograma.config(fg="blue", bg="light blue", font=("Verdana", 40))
        tituloPrograma.grid()
        introduccionPrograma1= tk.Label(self, text= "El siguiente programa es una DEMO para observar la funcionalidad de un triage computarizado. ").grid()
        introduccionPrograma2= tk.Label(self, text="Favor de informar cualquier error durante su uso.").grid()
        introduccionPrograma3= tk.Label(self, text="No nos hacemos responsables de los daños causados.").grid()
        self.imagen= tk.PhotoImage(file= ["bebe.gif"], format="gif -index 2")
        introduccionPrograma4= tk.Label(self, image= self.imagen).grid()

        botonSiguienteGeneral= tk.Button(self, text= "INICIO", command=lambda: master.switch_frame(PaginaConciencia))
        botonSiguienteGeneral.grid()
        
#Este es el primer frame con el primer parametro a evaluar, el de conciencia. Lo mas relevante es la funcionalidad del imagebutton: se crea una funcion lambda que manda a llamar dos funciones, ambas estan dentro de una tupla;
# 1.- La primera para asignar el valor segun el parametro a evlauar par dar un puntaje final  y asi dar un resultado
# 2.- La segunda aun dentro de la tupla, contenida en una lista, para dar paso al siguiente frame. 
class PaginaConciencia(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloGeneralConciencia= tk.Label(self, text= "Aspecto General")
        tituloGeneralConciencia.config(fg="blue", bg="light blue", font=("Arial", 30))
        tituloGeneralConciencia.grid()

        subtituloFrameConciencia= tk.Label(self, text= "Nivel de Conciencia")
        subtituloFrameConciencia.config(fg="blue", bg="light blue", font=("Arial", 20))
        subtituloFrameConciencia.grid()

        self.imagenDespierto= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaDespierto.png")
        self.imagenSomnoliento= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaSomnoliento.png")
        self.imagenIrritable= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaIrritable.png")
        self.imagenNoDuerme= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaNo.png")
        self.imagenCrisis= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaCrisis.png")
        
        conciencia = Conciencia.Opciones()

        botonDespierto= tk.Button(self, image= self.imagenDespierto, command= lambda:(conciencia.Despierto(), [master.switch_frame(PaginaColorPiel)])).grid()
        botonSomnoliento= tk.Button(self, image= self.imagenSomnoliento, command= lambda:(conciencia.Somnoliento(), [master.switch_frame(PaginaColorPiel)])).grid()
        botonIrritable= tk.Button(self, image= self.imagenIrritable, command= lambda:(conciencia.Irritable(), [master.switch_frame(PaginaColorPiel)])).grid()
        botonNoDuerme= tk.Button(self, image= self.imagenNoDuerme, command= lambda:(conciencia.NoDuerme(), [master.switch_frame(PaginaColorPiel)])).grid()
        botonCrisis= tk.Button(self, image= self.imagenCrisis, command= lambda:(conciencia.Crisis(), [master.switch_frame(PaginaColorPiel)])).grid()

#Este es el segundo frame con el segundo parametro a evaluar, el de coloracion de la piel. Sigue el mismo funcionamiento del frame anterior y la misma estructura general. 
class PaginaColorPiel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFramePiel= tk.Label(self, text= "Coloracion de la Piel")
        tituloFramePiel.grid()

        self.imagenPielRosada= tk.PhotoImage(file= "Imagenes/Piel/pielRosada.png")
        self.imagenPielPalida= tk.PhotoImage(file= "Imagenes/Piel/pielPalida.png")
        self.imagenPielCianotica= tk.PhotoImage(file= "Imagenes/Piel/pielCianotica.png")
        self.imagenPielRubicunda= tk.PhotoImage(file= "Imagenes/Piel/pielRubicunda.png")
        self.imagenPielMarmorea= tk.PhotoImage(file= "Imagenes/Piel/pielMarmorea.png")
        self.imagenPielPurpurica= tk.PhotoImage(file= "Imagenes/Piel/pielPurpurica.png")
        
        coloracionPiel = ColoracionPiel.Opciones()

        botonRosada= tk.Button(self, image= self.imagenPielRosada, command= lambda:(coloracionPiel.Rosada(), [master.switch_frame(PaginaHidraPiel)])).grid()
        botonPalida= tk.Button(self, image= self.imagenPielPalida,command= lambda:(coloracionPiel.Palida(), [master.switch_frame(PaginaHidraPiel)])).grid()
        botonCianotica= tk.Button(self, image= self.imagenPielCianotica,command= lambda:(coloracionPiel.Cianotica(), [master.switch_frame(PaginaHidraPiel)])).grid()
        botonRubicunda= tk.Button(self, image= self.imagenPielRubicunda,command= lambda:(coloracionPiel.Rubicunda(), [master.switch_frame(PaginaHidraPiel)])).grid()
        botonMarmorea= tk.Button(self, image= self.imagenPielMarmorea,command= lambda:(coloracionPiel.Marmorea(), [master.switch_frame(PaginaHidraPiel)])).grid()
        botonPurpurica= tk.Button(self, image= self.imagenPielPurpurica,command= lambda:(coloracionPiel.Purpurica(), [master.switch_frame(PaginaHidraPiel)])).grid()

#Este es el tercer frame con el tercer parametro a evaluar, el de la hidratacion de la piel. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraPiel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFramePiel= tk.Label(self, text= "Piel")
        tituloHidraFramePiel.grid()

        self.imagenHidraPielNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPielNormal.png")
        self.imagenHidraPielSeca= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPielSeca.png")
        
        hidraPiel = HidraPiel.Opciones()

        botonHidraPielNormal= tk.Button(self, image= self.imagenHidraPielNormal,command= lambda: (hidraPiel.Normal, [master.switch_frame(PaginaHidraMucosa)])).grid()
        botonHidraPielSeca= tk.Button(self, image= self.imagenHidraPielSeca, command= lambda: (hidraPiel.Seca, [master.switch_frame(PaginaHidraMucosa)])).grid()

#Este es el cuarto frame con el cuarto parametro a evluar, el de la hidratacion de las mucosas. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraMucosa(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameMucosas= tk.Label(self, text= "Mucosa")
        tituloHidraFrameMucosas.grid()

        self.imagenHidraMucosaNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraMucosaNormal.png")
        self.imagenHidraMucosaSeca= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraMucosaSeca.png")
        
        hidraMucosa = HidraMucosa.Opciones()

        botonHidraMucosaNormal= tk.Button(self, image= self.imagenHidraMucosaNormal, command= lambda: (hidraMucosa.Normal(), [master.switch_frame(PaginaHidraOjos)])).grid()
        botonHidraMucosaSeca= tk.Button(self, image= self.imagenHidraMucosaSeca, command= lambda: (hidraMucosa.Seca(), [master.switch_frame(PaginaHidraOjos)])).grid()

#Este es el quinto frame con el quinto parametro a evaluar, el estado de la hidratacion segun el estado clinico de los ojos. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraOjos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameOjos= tk.Label(self, text= "Ojos")
        tituloHidraFrameOjos.grid()

        self.imagenHidraOjosNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraOjosNormal.png")
        self.imagenHidraOjosHundidos= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraOjosHundidos.png")
        
        hidraOjos = HidraOjos.Opciones()

        botonHidraOjosNormal= tk.Button(self, image= self.imagenHidraOjosNormal, command= lambda: (hidraOjos.Normal(), [master.switch_frame(PaginaPliegue)])).grid()
        botonHidraOjosHundidos= tk.Button(self, image= self.imagenHidraOjosHundidos, command= lambda: (hidraOjos.Hundidos(), [master.switch_frame(PaginaPliegue)])).grid()

#Este es el sexto frame con el sexto parametro a evaluar, el estado de la hidratacion segun el signo del pliegue. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaPliegue(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFramePliegue= tk.Label(self, text= "Pliegue")
        tituloHidraFramePliegue.grid()

        self.imagenHidraPlieguePositivo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPlieguePositivo.png")
        self.imagenHidraPliegueNegativo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPliegueNegativo.png")
        
        hidraPliegue = HidraPliegue.Opciones()

        botonHidraPlieguePositivo= tk.Button(self, image= self.imagenHidraPlieguePositivo, command= lambda: (hidraPliegue.Positivo(), [master.switch_frame(PaginaHidraVomito)])).grid()
        botonHidraPliegueNegativo= tk.Button(self, image= self.imagenHidraPliegueNegativo, command= lambda: (hidraPliegue.Negativo(), [master.switch_frame(PaginaHidraVomito)])).grid()

#Este es el septimo frame con el septimo parametro a evaluar, el estado de hidratacion segun la presencia o ausencia de vomito. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraVomito(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameVomito= tk.Label(self, text= "Vomito")
        tituloHidraFrameVomito.grid()

        self.imagenHidraVomitoPresente= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraVomitoPresente.png")
        self.imagenHidraVomitoAusente= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraVomitoAusente.png")
        
        hidraVomito = HidraVomito.Opciones()

        botonHidraVomitoPresente= tk.Button(self, image= self.imagenHidraVomitoPresente, command= lambda: (hidraVomito.Presente(), [master.switch_frame(PaginaHidraTolerancia)])).grid()
        botonHidraVomitoAusente= tk.Button(self, image= self.imagenHidraVomitoAusente, command= lambda: (hidraVomito.Ausente(), [master.switch_frame(PaginaHidraTolerancia)])).grid()

#Este es el octavo frame con el octavo parametro a evaluar, la tolerancia a la via oral. Sigue el mismo funcionamiento del frame anterior y la misma estrctura general.
class PaginaHidraTolerancia(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameTolerancia= tk.Label(self, text= "¿Tolera Via Oral?")
        tituloHidraFrameTolerancia.grid()

        self.imagenHidraToleranciaSi= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraToleranciaSi.png")
        self.imagenHidraToleranciaNo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraToleranciaNo.png")
        
        tolerancia = HidraTolerancia.Opciones()

        botonHidraToleranciaSi= tk.Button(self, image= self.imagenHidraToleranciaSi, command= lambda: (tolerancia.SiTolera(), [master.switch_frame(PaginaActividad)])).grid()
        botonHidraToleranciaNo= tk.Button(self, image= self.imagenHidraToleranciaNo, command= lambda: (tolerancia.NoTolera(), [master.switch_frame(PaginaActividad)])).grid()

#Este es el noveno frame con el noveno parametro a evaluar, la actividad. Sigue el mismo funcionamiento del frame anrerior y la misma estrctura general. 
class PaginaActividad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameActividad= tk.Label(self, text= "Actividad")
        tituloFrameActividad.grid()

        self.imagenJuega= tk.PhotoImage(file= "Imagenes\Actividad\cactividadJuega.png")
        self.imagenConfundido= tk.PhotoImage(file= "Imagenes\Actividad\cactividadConfundido.png")
        self.imagenLetargico= tk.PhotoImage(file= "Imagenes\Actividad\cactividadLetargico.png")
        self.imagenInconsciente= tk.PhotoImage(file= "Imagenes\Actividad\cactividadInconsciente.png")
        
        actividad = Actividad.Opciones()

        botonJuega= tk.Button(self, image= self.imagenJuega, command= lambda: (actividad.Juega(), [master.switch_frame(PaginaTono)])).grid()
        botonConfundido= tk.Button(self, image= self.imagenConfundido, command= lambda: (actividad.Confundido(), [master.switch_frame(PaginaTono)])).grid()
        botonLetargico= tk.Button(self, image= self.imagenLetargico, command= lambda: (actividad.Letargico(), [master.switch_frame(PaginaTono)])).grid()
        botonInconsciente= tk.Button(self, image= self.imagenInconsciente, command= lambda: (actividad.Inconsciente(), [master.switch_frame(PaginaTono)])).grid()

class PaginaTono(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameTono= tk.Label(self, text= "Tono")
        tituloFrameTono.grid()

        self.imagenEutonico= tk.PhotoImage(file= "Imagenes\Tono\ctonoEutonico.png")
        self.imagenHipotonico= tk.PhotoImage(file= "Imagenes\Tono\ctonoHipotonico.png")

        botonEutonico= tk.Button(self, image= self.imagenEutonico,command= lambda:[master.switch_frame(PaginaVisual)]).grid()
        botonHipotonico= tk.Button(self, image= self.imagenHipotonico,command= lambda:[master.switch_frame(PaginaVisual)]).grid()

class PaginaVisual(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameVisual= tk.Label(self, text= "Contacto Visual")
        tituloFrameVisual.grid()

        self.imagenMantiene= tk.PhotoImage(file= "Imagenes\Visual\cvisualMantiene.png")
        self.imagenNoMantiene= tk.PhotoImage(file= "Imagenes\Visual\cvisualNoMantiene.png")
        self.imagenNoDirige= tk.PhotoImage(file= "Imagenes\Visual\cvisualNoDirige.png")

        botonMantiene= tk.Button(self, image= self.imagenMantiene,command= lambda:[master.switch_frame(PaginaLlanto)]).grid()
        botonNoMantiene= tk.Button(self, image= self.imagenNoMantiene,command= lambda:[master.switch_frame(PaginaLlanto)]).grid()
        botonNoDirige= tk.Button(self, image= self.imagenNoDirige,command= lambda:[master.switch_frame(PaginaLlanto)]).grid()

class PaginaLlanto(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameLlanto= tk.Label(self, text= "Lenguaje o Llanto")
        tituloFrameLlanto.grid()

        self.imagenLlantoFuerte= tk.PhotoImage(file= "Imagenes\Llanto\llantoFuerte.png")
        self.imagenLlantoDebil= tk.PhotoImage(file= "Imagenes\Llanto\llantoDebil.png")

        botonLlantoFuerte= tk.Button(self, image= self.imagenLlantoFuerte,command= lambda:[master.switch_frame(PaginaConsolabilidad)]).grid()
        botonLlantoDebil= tk.Button(self, image= self.imagenLlantoDebil,command= lambda:[master.switch_frame(PaginaConsolabilidad)]).grid()

class PaginaConsolabilidad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameConsolabilidad= tk.Label(self, text= "Consolabilidad")
        tituloFrameConsolabilidad.grid()

        self.imagenLlantoConsolable= tk.PhotoImage(file= "Imagenes\Llanto\llantoConsolable.png")
        self.imagenLlantoInconsolable= tk.PhotoImage(file= "Imagenes\Llanto\llantoInconsolable.png")

        botonConsolabilidad= tk.Button(self, image= self.imagenLlantoConsolable, command= lambda:[master.switch_frame(PaginaRuidos)]).grid()
        botonInconsolabilidad= tk.Button(self, image= self.imagenLlantoInconsolable, command= lambda:[master.switch_frame(PaginaRuidos)]).grid()

#Los frames correspondientes al apartado respiratorio tienen la cualidad de no reedigir directamente la sigueinte pagina. Si se selecciona positivamente aparecera un combobox para especificar la clase de patologica encontrada y de ahi se hara la reedirecion a la siguiente pagina. 
class PaginaRuidos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameRespiratorio1= tk.Label(self, text= "Respiratorio")
        tituloFrameRespiratorio1.grid()
        tituloFrameRuidos= tk.Label(self, text= "Ruidos Patologicos")
        tituloFrameRuidos.grid()
        self.opcionRespiracionRuidosSi= False
        self.opcionRespiracionRuidosNo= False

        self.imagenRespiracionRuidosSi= tk.PhotoImage(file= "Imagenes\Respiracion\cruidosSi.png")
        self.imagenRespiracionRuidosNo= tk.PhotoImage(file= "Imagenes\Respiracion\cruidosNo.png")

        botonRuidosSi= tk.Button(self, image= self.imagenRespiracionRuidosSi, command= lambda:[master.switch_frame(PaginaDificultad)]).grid()
        botonRuidosNo= tk.Button(self, image= self.imagenRespiracionRuidosNo, command= lambda:[ master.switch_frame(PaginaDificultad)]).grid()
        
        if (self.opcionRespiracionRuidosSi):
            def ruidoElegido(*args):
                comboRuidoElegido= comboRuidos.get()
                if comboRuidoElegido== "Gruñido":
                    pass
                elif comboRuidoElegido== "Estridor":
                    pass
                elif comboRuidoElegido== "Disfonia":
                    pass
                elif comboRuidoElegido== "Quejido":
                    pass
                elif comboRuidoElegido== "Silibancia":
                    pass
                    
            comboRuidos= ttk.Combobox(self)
            comboRuidos['values'] =("Gruñido", "Estridor", "Disfonia", "Quejido", "Silibancia") 
            comboRuidos.state(["readonly"])
            comboRuidos.bind("<<ComboboxSelected>>", ruidoElegido)
            comboRuidos.grid()
            
        elif (self.opcionRespiracionRuidosNo):
            trianguloEvaluacionPediatricaRespiracion= True

class PaginaDificultad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameDificultad= tk.Label(self, text= "Datos de Dificultad")
        tituloFrameDificultad.grid()
        self.opcionRespiracionDificultadSi= False
        self.opcionRespiracionDificultadNo= False

        self.imagenRespiracionDificultadSi= tk.PhotoImage(file= "Imagenes\Respiracion\dificultadSi.png")
        self.imagenRespiracionDificultadNo= tk.PhotoImage(file= "Imagenes\Respiracion\dificultadNo.png")

        botonDificultadSi= tk.Button(self, image= self.imagenRespiracionDificultadSi, command= lambda: [master.switch_frame(PaginaPosicion)]).grid()
        botonDificultadNo= tk.Button(self, image= self.imagenRespiracionDificultadNo, command= lambda:[master.switch_frame(PaginaPosicion)]).grid()
        
        if (self.opcionRespiracionDificultadSi):
            def dificultadElegida(*args):
                comboDificultadElegida= comboDificultad.get()
                if comboDificultadElegida== "Tiraje Intercostal":
                    pass
                elif comboDificultadElegida=="Retracciones":
                    pass
                elif comboDificultadElegida=="Aleteo Nasal":
                    pass
                elif comboDificultadElegida=="Dis.Toraco Abdominal":
                    pass

            comboDificultad= ttk.Combobox(self)
            comboDificultad['values']= ("Tiraje Intercostal", "Retracciones","Aleteo Nasal","Dis.Toraco Abdominal")
            comboDificultad.state(["readonly"])
            comboDificultad.bind("<<ComboboxSelected>>", dificultadElegida)
            comboDificultad.grid()

        elif (self.opcionRespiracionDificultadNo):
            trianguloEvaluacionPediatricaRespiracion= True


class PaginaPosicion(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFramePosicion= tk.Label(self, text= "Posicion Patologica")
        tituloFramePosicion.grid()

        self.imagenRespiracionPosicionSi= tk.PhotoImage(file= "Imagenes\Respiracion\posicionSi.png")
        self.imagenRespiracionPosicionNo= tk.PhotoImage(file= "Imagenes\Respiracion\posicionNo.png")

        botonPosicionSi= tk.Button(self, image= self.imagenRespiracionPosicionSi, command= lambda:[master.switch_frame(PaginaAntecedentes)]).grid()
        botonPosicionNo= tk.Button(self, image= self.imagenRespiracionPosicionNo, command= lambda:[master.switch_frame(PaginaAntecedentes)]).grid()
        
        
#A partir de estos frames los combobox ya no aparecen. 
class PaginaAntecedentes(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameAntecedentes= tk.Label(self, text= "Antecedentes")
        tituloFrameAntecedentes.grid()
        subtituloFrameAntecedentes= tk.Label(self, text="Enfermedades Cronico-Degenerativas o Uso de Esteroides")
        subtituloFrameAntecedentes.grid()

        self.imagenAntecedentesSi= tk.PhotoImage(file= "Imagenes\Antecedentes\cantecedentesSi.png")
        self.imagenAntecedentesNo= tk.PhotoImage(file= "Imagenes\Antecedentes\cantecedentesNo.png")

        botonAntecedentesSi= tk.Button(self, image= self.imagenAntecedentesSi, command= lambda:[master.switch_frame(PaginaAbuso)]).grid()
        botonAntecedentesNo= tk.Button(self, image= self.imagenAntecedentesNo, command= lambda:[master.switch_frame(PaginaAbuso)]).grid()

class PaginaAbuso(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameAbuso= tk.Label(self, text= "Datos de Abuso")
        tituloFrameAbuso.grid()

        self.imagenAbusoSi= tk.PhotoImage(file= "Imagenes\Antecedentes\cabusoSi.png")
        self.imagenAbusoNo= tk.PhotoImage(file= "Imagenes\Antecedentes\cabusoNo.png")

        botonAbusoSi= tk.Button(self, image= self.imagenAbusoSi, command= lambda:[master.switch_frame(PaginaResultado)]).grid()
        botonAbusoNo= tk.Button(self, image= self.imagenAbusoNo, command= lambda:[master.switch_frame(PaginaResultado)]).grid()

#En esta pagina se dara a conocer el resultado segun la evaluacion de los parametros descritos anteriormente. Tiene que aparecer el frame del color correspondiente a la gravedad de la urgencia medica. 
class PaginaResultado(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()