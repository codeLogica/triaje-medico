import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox as msb
from datetime import datetime
from Mod_Eva import Modulo
from Mod_Eva import Resultado
from Mod_Eva import Parametros

#Esta es la pagina principal del programa, donde se muestra informacion relevante. Se inicializa el frame y dentro encontramos los widgets necesarios. Se basa en una serie de imagenes con los parametros a analizar y dependiendo de la seleccion se evaluan en otro modulo. 
#Se sigue el siguiente esquema en todos los frames:
#Inizialicacion --> informacion --> imagenes --> llamada al modulo con el parametro a evaluar --> botones 
class PaginaGeneral(tk.Frame):
    def __init__(self, master):
        tk.Canvas.__init__(self, master)
        tituloPrograma= tk.Label(self, 
                                 text= "PROGRAMA DE EVALUACION PEDIATRICA")
        tituloPrograma.config(fg="blue", 
                              bg="light blue", 
                              font=("Verdana", 30))
        tituloPrograma.grid()
        introduccionPrograma1= tk.Label(self, 
                                        text= "El siguiente programa es una DEMO para observar la funcionalidad de un triage computarizado. ")
        introduccionPrograma1.grid()
        introduccionPrograma2= tk.Label(self, 
                                        text="Favor de informar cualquier error durante su uso.")
        introduccionPrograma2.grid()
        introduccionPrograma3= tk.Label(self, 
                                        text="No nos hacemos responsables de los daños causados.")
        introduccionPrograma3.grid()
        
        self.imagen= tk.PhotoImage(file= ["bebe.gif"], format="gif -index 2")
        introduccionPrograma4= tk.Label(self, 
                                        image= self.imagen)
        introduccionPrograma4.grid(row= 3, column=0, columnspan= 2)

        botonSiguienteGeneral= tk.Button(self, 
                                         text= "INICIO", 
                                         command=lambda: master.switch_frame(PaginaDatos))
        botonSiguienteGeneral.grid(row= 6, column=0)
        
#Aqui se tomaran los datos generales del paciente para identificarlo. Nombre, apellidos, fecha nacimiento y sexo. 
class PaginaDatos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tituloDatos= tk.Label(self, text= "Datos del Paciente")
        tituloDatos.grid(row=0, column=0, columnspan=3)
        
        #Funcion para corroborar que se ingresen caracteres alfabeticos en el nombre y que sean en mayusculas. 
        def validar_mayuscula(nomApAm_mayuscula):            
            if (nomApAm_mayuscula) == None:
                return False
            checks = [] 
            for i, char in enumerate(nomApAm_mayuscula):
                if i in ():
                    checks.append(char == " ", ".") #Por si tiene 2 nombres.
                else:
                    checks.append(char.isupper())
            return all(checks)

        #Funcion para corrobar el ingreso de la fecha de nacimiento con datos numericos y con 8 digitos a lo maximo (2 dia/2 mes/4 año) y 2 caracteres barra diagonal para separarlos.
        def edad_por_nacimiento(f_nacimiento):
            if len(f_nacimiento) > 10:
                return False
            checks = [] 
            for i, char in enumerate(f_nacimiento):
                if i in (2,2) or i in (2, 2) or i in (2, 5):
                    checks.append(char == "/")
                    f_nacimiento_comprobacion= str(f_nacimiento)
                else:
                    checks.append(char.isdecimal())

            #Se comprueba que se tengan los 10 caracteres (8 digitos y 2 barras diagonales)
                if len(f_nacimiento) == 10:
                    diaActual= datetime.now()
                    diaNacimiento= datetime.strptime(f_nacimiento, "%d/%m/%Y")
                    calculoEdad= (diaActual - diaNacimiento)
                    
                    diferenciaAños= calculoEdad.days / 365
                    diferenciaMeses= calculoEdad.days / 30
                    diferenciaDias= calculoEdad.days
                    
                    if diferenciaDias < 28:
                        print("Recien Nacido")
                    elif diferenciaMeses < 12:
                        print("Lactante Menor")
                    elif diferenciaMeses < 24:
                        print("Lactante Mayor")
                    elif diferenciaAños >2 and diferenciaAños <6:
                        print("Pre Escolar")
                    elif diferenciaAños >6 and diferenciaAños <10:
                        print("Escolar")
                    elif diferenciaAños > 11 and diferenciaAños <19:
                        print("Adolescente")
                    print(calculoEdad)
                    return calculoEdad
            
            return all(checks)
   
        def corroborar_datos(self):
            self.nomEnt= self.nombreEntry.get()
            self.apPatEnt= self.apellPaterno.get()
            self.apMatEnt= self.apellMaterno.get()
            self.fechNacEnt= self.fechaNacimiento.get()
            
            pasar_datos(self, self.nomEnt, self.apPatEnt, self.apMatEnt)

            self.verificarDatosPaciente= msb.askyesno(title="Verificacion de Datos", 
                         message=(f"¿Datos introducidos correctamente?\n\n Nombre: {self.nomEnt}\n Apellido Paterno: {self.apPatEnt}\n Apellido Materno: {self.apMatEnt}\n Fecha de Nacimiento: {self.fechNacEnt}"))
            
            if self.verificarDatosPaciente:
                master.switch_frame(PaginaConciencia) 


        self.opcionNombre= tk.StringVar()
        tk.Label(self, text= "Nombre").grid(row=1, column=0, sticky="e")
        self.nombreEntry= tk.Entry(self,
                              textvariable=self.opcionNombre, 
                              validate="key",
                              validatecommand=(self.register(validar_mayuscula), "%P"))
        self.nombreEntry.grid(row=1, column=2)

        self.opcionApPat= tk.StringVar()
        tk.Label(self, text= "Apellido Paterno").grid(row=2, column=0, sticky="e")
        self.apellPaterno= tk.Entry(self,
                               textvariable=self.opcionApPat,
                               validate="key",
                               validatecommand=(self.register(validar_mayuscula), "%P"))
        self.apellPaterno.grid(row=2, column=2)

        self.opcionApMat= tk.StringVar()
        tk.Label(self, text= "Apellido Materno").grid(row=3, column=0, sticky="e")
        self.apellMaterno= tk.Entry(self,
                               textvariable=self.opcionApMat, 
                               validate="key",
                               validatecommand=(self.register(validar_mayuscula), "%P"))
        self.apellMaterno.grid(row=3, column=2)
        
        self.opcionNacimiento= tk.StringVar()
        tk.Label(self, text= "Fecha de Nacimiento").grid(row=4, column=0, sticky="e")
        self.fechaNacimiento= tk.Entry(self,
                                  textvariable=self.opcionNacimiento,
                                  validate="key",
                                  validatecommand=(self.register(edad_por_nacimiento), "%P"))
        self.fechaNacimiento.grid(row=4, column=2)
        
        self.opcionSexo= tk.IntVar()
        tk.Label(self, text= "Sexo").grid(row=5, column=0, sticky="e")
        self.radioButtonHombre= tk.Radiobutton(self,
                                          text= "Hombre",
                                          variable=self.opcionSexo,
                                          value= 1)
        self.radioButtonHombre.grid(row=5, column=2, sticky="w")
        
        self.radioButtonMujer= tk.Radiobutton(self,
                                          text= "Mujer",
                                          variable=self.opcionSexo,
                                          value= 2)
        self.radioButtonMujer.grid(row=6, column=2, sticky="w")

        botonGuardarDatos= tk.Button(self, 
                                     text="Guardar",
                                    command=lambda: corroborar_datos(self))
        botonGuardarDatos.grid(row=7, column=0, columnspan=3)

        def pasar_datos(self, n, ap, am):
            self.nombre= n
            self.apellP= ap
            self.apellM= am
            
            return [self.nombre, self.apellP, self.apellM]
        
#Este es el primer frame con el primer parametro a evaluar, el de conciencia. Lo mas relevante es la funcionalidad del imagebutton: se crea una funcion lambda que manda a llamar dos funciones, ambas estan dentro de una tupla;
# 1.- La primera para asignar el valor segun el parametro a evlauar par dar un puntaje final  y asi dar un resultado
# 2.- La segunda aun dentro de la tupla, contenida en una lista, para dar paso al siguiente frame. 
class PaginaConciencia(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        
        tituloGeneralConciencia= tk.Label(self, 
                                          text= "Aspecto General")
        tituloGeneralConciencia.config(fg="blue", 
                                       bg="light blue", 
                                       font=("Arial", 30))
        tituloGeneralConciencia.grid(row=0, column=0, columnspan=3)

        subtituloFrameConciencia= tk.Label(self, 
                                           text= "Nivel de Conciencia")
        subtituloFrameConciencia.config(fg="blue", 
                                        bg="light blue", 
                                        font=("Arial", 20))
        subtituloFrameConciencia.grid(row=1, column=0, columnspan=3)
        
        d = PaginaDatos(self)

        tk.Label(self, text=(f"Paciente: {d.opcionNombre.get(), d.opcionApPat.get(), d.opcionApMat.get()}")).grid(row=2, column=0, columnspan=3)
        
        
        self.imagenDespierto= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaDespierto.png")
        self.imagenSomnoliento= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaSomnoliento.png")
        self.imagenIrritable= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaIrritable.png")
        self.imagenNoDuerme= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaNo.png")
        self.imagenCrisis= tk.PhotoImage(file= "Imagenes/Conciencia/concienciaCrisis.png")
        
        conciencia = Modulo.ConcienciaOpcion()
        
        botonDespierto= tk.Button(self, 
                                  image= self.imagenDespierto, 
                                  command= lambda:(conciencia.Despierto(), [master.switch_frame(PaginaColorPiel)]))
        botonDespierto.grid(row=3, column=0)
        
        botonSomnoliento= tk.Button(self, 
                                    image= self.imagenSomnoliento, 
                                    command= lambda:(conciencia.Somnoliento(), [master.switch_frame(PaginaColorPiel)]))
        botonSomnoliento.grid(row=3, column=2)
        botonIrritable= tk.Button(self, 
                                  image= self.imagenIrritable, 
                                  command= lambda:(conciencia.Irritable(), [master.switch_frame(PaginaColorPiel)]))
        botonIrritable.grid(row=4, column=0)
        botonNoDuerme= tk.Button(self, 
                                 image= self.imagenNoDuerme, 
                                 command= lambda:(conciencia.NoDuerme(), [master.switch_frame(PaginaColorPiel)]))
        botonNoDuerme.grid(row=4, column=1)
        botonCrisis= tk.Button(self, 
                               image= self.imagenCrisis, 
                               command= lambda:(conciencia.Crisis(), [master.switch_frame(PaginaColorPiel)]))
        botonCrisis.grid(row=4, column=2)

#Este es el segundo frame con el segundo parametro a evaluar, el de coloracion de la piel. Sigue el mismo funcionamiento del frame anterior y la misma estructura general. 
class PaginaColorPiel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFramePiel= tk.Label(self, 
                                  text= "Coloracion de la Piel")
        tituloFramePiel.config(fg="blue", 
                               bg="light blue", 
                               font=("Arial", 20))
        tituloFramePiel.grid(row=0, column=0, columnspan=3)

        self.imagenPielRosada= tk.PhotoImage(file= "Imagenes/Piel/pielRosada.png")
        self.imagenPielPalida= tk.PhotoImage(file= "Imagenes/Piel/pielPalida.png")
        self.imagenPielCianotica= tk.PhotoImage(file= "Imagenes/Piel/pielCianotica.png")
        self.imagenPielRubicunda= tk.PhotoImage(file= "Imagenes/Piel/pielRubicunda.png")
        self.imagenPielMarmorea= tk.PhotoImage(file= "Imagenes/Piel/pielMarmorea.png")
        self.imagenPielPurpurica= tk.PhotoImage(file= "Imagenes/Piel/pielPurpurica.png")
        
        coloracionPiel = Modulo.ColorPielOpcion()

        botonRosada= tk.Button(self, 
                               image= self.imagenPielRosada, 
                               command= lambda:(coloracionPiel.Rosada(), [master.switch_frame(PaginaHidraPiel)]))
        botonRosada.grid(row=1, column=0)
        botonPalida= tk.Button(self, 
                               image= self.imagenPielPalida,
                               command= lambda:(coloracionPiel.Palida(), [master.switch_frame(PaginaHidraPiel)]))
        botonPalida.grid(row=1, column=1)
        botonCianotica= tk.Button(self, 
                                  image= self.imagenPielCianotica,
                                  command= lambda:(coloracionPiel.Cianotica(), [master.switch_frame(PaginaHidraPiel)]))
        botonCianotica.grid(row=1, column=2)
        botonRubicunda= tk.Button(self, 
                                  image= self.imagenPielRubicunda,
                                  command= lambda:(coloracionPiel.Rubicunda(), [master.switch_frame(PaginaHidraPiel)]))
        botonRubicunda.grid(row=2, column=0)
        botonMarmorea= tk.Button(self, 
                                 image= self.imagenPielMarmorea,
                                 command= lambda:(coloracionPiel.Marmorea(), [master.switch_frame(PaginaHidraPiel)]))
        botonMarmorea.grid(row=2, column=1)
        botonPurpurica= tk.Button(self, 
                                  image= self.imagenPielPurpurica,
                                  command= lambda:(coloracionPiel.Purpurica(), [master.switch_frame(PaginaHidraPiel)]))
        botonPurpurica.grid(row=2, column=2)

#Este es el tercer frame con el tercer parametro a evaluar, el de la hidratacion de la piel. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraPiel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFramePiel= tk.Label(self, 
                                       text= "Piel")
        tituloHidraFramePiel.config(fg="blue", 
                                    bg="light blue", 
                                    font=("Arial", 20))
        tituloHidraFramePiel.grid(row=0, column=0, columnspan=3)

        self.imagenHidraPielNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPielNormal.png")
        self.imagenHidraPielSeca= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPielSeca.png")
        
        hidraPiel = Modulo.HidratacionPielOpcion()

        botonHidraPielNormal= tk.Button(self, 
                                        image= self.imagenHidraPielNormal,
                                        command= lambda: (hidraPiel.Normal, [master.switch_frame(PaginaHidraMucosa)]))
        botonHidraPielNormal.grid(row=1, column=0)
        botonHidraPielSeca= tk.Button(self, 
                                      image= self.imagenHidraPielSeca, 
                                      command= lambda: (hidraPiel.Seca, [master.switch_frame(PaginaHidraMucosa)]))
        botonHidraPielSeca.grid(row=1, column=1)

#Este es el cuarto frame con el cuarto parametro a evluar, el de la hidratacion de las mucosas. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraMucosa(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameMucosas= tk.Label(self, 
                                          text= "Mucosa")
        tituloHidraFrameMucosas.config(fg="blue",
                                       bg="light blue", 
                                       font=("Arial", 20))
        tituloHidraFrameMucosas.grid(row=0, column=0, columnspan=3)

        self.imagenHidraMucosaNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraMucosaNormal.png")
        self.imagenHidraMucosaSeca= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraMucosaSeca.png")
        
        hidraMucosa = Modulo.HidratacionMucosasOpcion()

        botonHidraMucosaNormal= tk.Button(self, 
                                          image= self.imagenHidraMucosaNormal, 
                                          command= lambda: (hidraMucosa.Normal(), [master.switch_frame(PaginaHidraOjos)]))
        botonHidraMucosaNormal.grid(row=1, column=0)
        
        botonHidraMucosaSeca= tk.Button(self, 
                                        image= self.imagenHidraMucosaSeca, 
                                        command= lambda: (hidraMucosa.Seca(), [master.switch_frame(PaginaHidraOjos)]))
        botonHidraMucosaSeca.grid(row=1, column=1)

#Este es el quinto frame con el quinto parametro a evaluar, el estado de la hidratacion segun el estado clinico de los ojos. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraOjos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameOjos= tk.Label(self, 
                                       text= "Ojos")
        tituloHidraFrameOjos.config(fg="blue", 
                                    bg="light blue", 
                                    font=("Arial", 20))
        tituloHidraFrameOjos.grid(row=0, column=0, columnspan=3)

        self.imagenHidraOjosNormal= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraOjosNormal.png")
        self.imagenHidraOjosHundidos= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraOjosHundidos.png")
        
        hidraOjos = Modulo.HidratacionOjosOpcion()

        botonHidraOjosNormal= tk.Button(self, 
                                        image= self.imagenHidraOjosNormal, 
                                        command= lambda: (hidraOjos.Normal(), [master.switch_frame(PaginaPliegue)]))
        botonHidraOjosNormal.grid(row=1, column=0)
        
        botonHidraOjosHundidos= tk.Button(self, 
                                          image= self.imagenHidraOjosHundidos, 
                                          command= lambda: (hidraOjos.Hundidos(), [master.switch_frame(PaginaPliegue)]))
        botonHidraOjosHundidos.grid(row=1, column=1)

#Este es el sexto frame con el sexto parametro a evaluar, el estado de la hidratacion segun el signo del pliegue. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaPliegue(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFramePliegue= tk.Label(self, 
                                          text= "Pliegue")
        tituloHidraFramePliegue.config(fg="blue", 
                                       bg="light blue", 
                                       font=("Arial", 20))
        tituloHidraFramePliegue.grid(row=0, column=0, columnspan=3)

        self.imagenHidraPlieguePositivo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPlieguePositivo.png")
        self.imagenHidraPliegueNegativo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraPliegueNegativo.png")
        
        hidraPliegue = Modulo.HidratacionPliegueOpcion()

        botonHidraPlieguePositivo= tk.Button(self, 
                                             image= self.imagenHidraPlieguePositivo, 
                                             command= lambda: (hidraPliegue.Positivo(), [master.switch_frame(PaginaHidraVomito)]))
        botonHidraPlieguePositivo.grid(row=1, column=0)
        
        botonHidraPliegueNegativo= tk.Button(self, 
                                             image= self.imagenHidraPliegueNegativo, 
                                             command= lambda: (hidraPliegue.Negativo(), [master.switch_frame(PaginaHidraVomito)]))
        botonHidraPliegueNegativo.grid(row=1, column=1)

#Este es el septimo frame con el septimo parametro a evaluar, el estado de hidratacion segun la presencia o ausencia de vomito. Sigue el mismo funcionamiento del frame anterior y la misma estructura general.
class PaginaHidraVomito(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameVomito= tk.Label(self, 
                                         text= "Vomito")
        tituloHidraFrameVomito.config(fg="blue", 
                                      bg="light blue", 
                                      font=("Arial", 20))
        tituloHidraFrameVomito.grid(row=0, column=0, columnspan=3)

        self.imagenHidraVomitoPresente= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraVomitoPresente.png")
        self.imagenHidraVomitoAusente= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraVomitoAusente.png")
        
        hidraVomito = Modulo.HidratacionVomitoOpcion()

        botonHidraVomitoPresente= tk.Button(self, 
                                            image= self.imagenHidraVomitoPresente, 
                                            command= lambda: (hidraVomito.Presente(), [master.switch_frame(PaginaHidraTolerancia)]))
        botonHidraVomitoPresente.grid(row=1, column=0)
        
        botonHidraVomitoAusente= tk.Button(self, 
                                           image= self.imagenHidraVomitoAusente, 
                                           command= lambda: (hidraVomito.Ausente(), [master.switch_frame(PaginaHidraTolerancia)]))
        botonHidraVomitoAusente.grid(row=1, column=1)

#Este es el octavo frame con el octavo parametro a evaluar, la tolerancia a la via oral. Sigue el mismo funcionamiento del frame anterior y la misma estrctura general.
class PaginaHidraTolerancia(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloHidraFrameTolerancia= tk.Label(self, 
                                             text= "¿Tolera Via Oral?")
        tituloHidraFrameTolerancia.config(fg="blue", 
                                          bg="light blue", 
                                          font=("Arial", 20))
        tituloHidraFrameTolerancia.grid(row=0, column=0, columnspan=3)

        self.imagenHidraToleranciaSi= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraToleranciaSi.png")
        self.imagenHidraToleranciaNo= tk.PhotoImage(file= "Imagenes\Hidratacion\hidraToleranciaNo.png")
        
        tolerancia = Modulo.HidratacionToleranciaOpcion()

        botonHidraToleranciaSi= tk.Button(self, 
                                          image= self.imagenHidraToleranciaSi, 
                                          command= lambda: (tolerancia.SiTolera(), [master.switch_frame(PaginaActividad)]))
        botonHidraToleranciaSi.grid(row=1, column=0)
        
        botonHidraToleranciaNo= tk.Button(self, 
                                          image= self.imagenHidraToleranciaNo, 
                                          command= lambda: (tolerancia.NoTolera(), [master.switch_frame(PaginaActividad)]))
        botonHidraToleranciaNo.grid(row=1, column=1)

#Este es el noveno frame con el noveno parametro a evaluar, la actividad. Sigue el mismo funcionamiento del frame anrerior y la misma estrctura general. 
class PaginaActividad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameActividad= tk.Label(self, 
                                       text= "Actividad")
        tituloFrameActividad.config(fg="blue", 
                                    bg="light blue", 
                                    font=("Arial", 20))
        tituloFrameActividad.grid(row=0, column=0, columnspan=3)

        self.imagenJuega= tk.PhotoImage(file= "Imagenes\Actividad\cactividadJuega.png")
        self.imagenConfundido= tk.PhotoImage(file= "Imagenes\Actividad\cactividadConfundido.png")
        self.imagenLetargico= tk.PhotoImage(file= "Imagenes\Actividad\cactividadLetargico.png")
        self.imagenInconsciente= tk.PhotoImage(file= "Imagenes\Actividad\cactividadInconsciente.png")
        
        actividad = Modulo.ActividadOpcion()

        botonJuega= tk.Button(self, 
                              image= self.imagenJuega, 
                              command= lambda: (actividad.Juega(), [master.switch_frame(PaginaTono)]))
        botonJuega.grid(row=1, column=0)
        
        botonConfundido= tk.Button(self, 
                                   image= self.imagenConfundido, 
                                   command= lambda: (actividad.Confundido(), [master.switch_frame(PaginaTono)]))
        botonConfundido.grid(row=1, column=1)
        
        botonLetargico= tk.Button(self, 
                                  image= self.imagenLetargico, 
                                  command= lambda: (actividad.Letargico(), [master.switch_frame(PaginaTono)]))
        botonLetargico.grid(row=2, column=0)
        
        botonInconsciente= tk.Button(self, 
                                     image= self.imagenInconsciente, 
                                     command= lambda: (actividad.Inconsciente(), [master.switch_frame(PaginaTono)]))
        botonInconsciente.grid(row=2, column=1)

#Este es el decimo frame con el decimo parametro a evaluar, el tono muscular. Sigue el mismo funcionamiento del frame anterior y la misma estrctura general. 
class PaginaTono(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameTono= tk.Label(self, 
                                  text= "Tono")
        tituloFrameTono.config(fg="blue", 
                               bg="light blue", 
                               font=("Arial", 20))
        tituloFrameTono.grid(row=0, column=0, columnspan=3)

        self.imagenEutonico= tk.PhotoImage(file= "Imagenes\Tono\ctonoEutonico.png")
        self.imagenHipotonico= tk.PhotoImage(file= "Imagenes\Tono\ctonoHipotonico.png")
        
        tono = Modulo.TonoOpcion()

        botonEutonico= tk.Button(self, 
                                 image= self.imagenEutonico,
                                 command= lambda: (tono.Eutonico(), [master.switch_frame(PaginaVisual)]))
        botonEutonico.grid(row=1, column=0)
        botonHipotonico= tk.Button(self, 
                                   image= self.imagenHipotonico,
                                   command= lambda: (tono.Hipotonico(),[master.switch_frame(PaginaVisual)]))
        botonHipotonico.grid(row=1, column=1)

#Este es el onceavo frame con el onceavo parametro a evaluar, el contacto visual. Sigue el mismo funcionamiento del frame anterior y la misma estructura general. 
class PaginaVisual(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameVisual= tk.Label(self, 
                                    text= "Contacto Visual")
        tituloFrameVisual.config(fg="blue", 
                                 bg="light blue", 
                                 font=("Arial", 20))
        tituloFrameVisual.grid(row=0, column=0, columnspan=3)

        self.imagenMantiene= tk.PhotoImage(file= "Imagenes\Visual\cvisualMantiene.png")
        self.imagenNoMantiene= tk.PhotoImage(file= "Imagenes\Visual\cvisualNoMantiene.png")
        self.imagenNoDirige= tk.PhotoImage(file= "Imagenes\Visual\cvisualNoDirige.png")
        
        mirada = Modulo.VisualOpcion()

        botonMantiene= tk.Button(self, 
                                 image= self.imagenMantiene,
                                 command= lambda: (mirada.Mantiene(), [master.switch_frame(PaginaLlanto)]))
        botonMantiene.grid(row=1, column=0)
        botonNoMantiene= tk.Button(self, 
                                   image= self.imagenNoMantiene,
                                   command= lambda: (mirada.NoMantiene(), [master.switch_frame(PaginaLlanto)]))
        botonNoMantiene.grid(row=1, column=1)
        botonNoDirige= tk.Button(self, 
                                 image= self.imagenNoDirige,
                                 command= lambda: (mirada.NoDirige(), [master.switch_frame(PaginaLlanto)]))
        botonNoDirige.grid(row=1, column=2)

#Este es el doceavo frame con el doceavo parametro a evaluar, la clinica del llanto. Sigue el mismo funcionamiento del frame anterior y la misma estructua general.
class PaginaLlanto(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameLlanto= tk.Label(self, 
                                    text= "Lenguaje o Llanto")
        tituloFrameLlanto.config(fg="blue", 
                                 bg="light blue", 
                                 font=("Arial", 20))
        tituloFrameLlanto.grid(row=0, column=0, columnspan=3)

        self.imagenLlantoFuerte= tk.PhotoImage(file= "Imagenes\Llanto\llantoFuerte.png")
        self.imagenLlantoDebil= tk.PhotoImage(file= "Imagenes\Llanto\llantoDebil.png")
        
        llanto = Modulo.LlantoOpcion()

        botonLlantoFuerte= tk.Button(self, 
                                     image= self.imagenLlantoFuerte,
                                     command= lambda: (llanto.Fuerte(), [master.switch_frame(PaginaConsolabilidad)]))
        botonLlantoFuerte.grid(row=1, column=0)
        botonLlantoDebil= tk.Button(self, 
                                    image= self.imagenLlantoDebil,
                                    command= lambda: (llanto.Debil(), [master.switch_frame(PaginaConsolabilidad)]))
        botonLlantoDebil.grid(row=1, column=1)

#Este es el treceavo frame con el traceavo parametro a evaluar, la capacidad de ser consolado. Sigue el mismo funcionamiento del frame anterior y la misma estructura general. 
class PaginaConsolabilidad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameConsolabilidad= tk.Label(self, 
                                            text= "Consolabilidad")
        tituloFrameConsolabilidad.config(fg="blue", 
                                         bg="light blue", 
                                         font=("Arial", 20))
        tituloFrameConsolabilidad.grid(row=0, column=0, columnspan=3)

        self.imagenLlantoConsolable= tk.PhotoImage(file= "Imagenes\Llanto\llantoConsolable.png")
        self.imagenLlantoInconsolable= tk.PhotoImage(file= "Imagenes\Llanto\llantoInconsolable.png")
        
        es = Modulo.ConsolableOpcion()

        botonConsolabilidad= tk.Button(self, 
                                       image= self.imagenLlantoConsolable, 
                                       command= lambda: (es.Consolable(), [master.switch_frame(PaginaRuidos)]))
        botonConsolabilidad.grid(row=1, column=0)
        botonInconsolabilidad= tk.Button(self, 
                                         image= self.imagenLlantoInconsolable, 
                                         command= lambda: (es.Inconsolable(), [master.switch_frame(PaginaRuidos)]))
        botonInconsolabilidad.grid(row=1, column=1)

#Se hace una instancia de clase del modulo parametros para pasarle los valores a analizar, solo en la seccion Respiratoria que incluyen la siguientes 3 clases.
paramEvaluar = Parametros.Evaluar()

#Los frames correspondientes al apartado respiratorio tienen la cualidad de no reedigir directamente la sigueinte pagina. Si se selecciona positivamente aparecera un combobox para especificar la clase de patologica encontrada y de ahi se hara la reedirecion a la siguiente pagina. 
class PaginaRuidos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameRespiratorio1= tk.Label(self, 
                                           text= "Respiratorio")
        tituloFrameRespiratorio1.config(fg="blue", bg="light blue", font=("Arial", 30))
        tituloFrameRespiratorio1.grid(row=0, column=0, columnspan=3)
        
        tituloFrameRuidos= tk.Label(self, 
                                    text= "Ruidos Patologicos")
        tituloFrameRuidos.config(fg="blue", bg="light blue", font=("Arial", 20))
        tituloFrameRuidos.grid(row=1, column=0, columnspan=3)

        self.imagenRespiracionRuidosSi= tk.PhotoImage(file= "Imagenes\Respiracion\cruidosSi.png")
        self.imagenRespiracionRuidosNo= tk.PhotoImage(file= "Imagenes\Respiracion\cruidosNo.png")
        
        #ruidos = Modulo.RuidoRespiratorioOpcion()
        
        def RuidosPresentes(self):
            def ruidoElegido(*args):
                comboRuidoElegido= comboRuidos.get()
                
                if comboRuidoElegido== "Gruñido":
                    paramEvaluar.TEPR(False)
                    paramEvaluar.SAT(3)
                    paramEvaluar.SAC(0.333)
                elif comboRuidoElegido== "Estridor":
                    paramEvaluar.TEPR(False)
                    paramEvaluar.SAT(3)
                    paramEvaluar.SAC(0.333)
                elif comboRuidoElegido== "Disfonia":
                    paramEvaluar.TEPR(False)
                    paramEvaluar.SAT(3)
                    paramEvaluar.SAC(0.333)
                elif comboRuidoElegido== "Quejido":
                    paramEvaluar.TEPR(False)
                    paramEvaluar.SAT(3)
                    paramEvaluar.SAC(0.333)
                elif comboRuidoElegido== "Silibancia":
                    paramEvaluar.TEPR(False)
                    paramEvaluar.SAT(3)
                    paramEvaluar.SAC(0.333)
                
                master.switch_frame(PaginaDificultad)
            
            comboRuidos= ttk.Combobox(self)
            comboRuidos['values']=("Gruñido", 
                                   "Estridor", 
                                   "Disfonia", 
                                   "Quejido", 
                                   "Silibancia") 
            comboRuidos.state(["readonly"])
            comboRuidos.bind("<<ComboboxSelected>>", ruidoElegido)
            comboRuidos.grid(row=3, column=0, columnspan=3)
                    
        def RuidosAusentes(self):
            paramEvaluar.TEPR(True)
            paramEvaluar.SAT(0)
            paramEvaluar.SAC(0.0)
            
            master.switch_frame(PaginaDificultad)

        botonRuidosPresentes= tk.Button(self, 
                                        image= self.imagenRespiracionRuidosSi, 
                                        command= lambda: RuidosPresentes(self))
        botonRuidosPresentes.grid(row=2, column=0)
        botonRuidosAusentes= tk.Button(self, 
                                       image= self.imagenRespiracionRuidosNo, 
                                       command= lambda: RuidosAusentes(self))
        botonRuidosAusentes.grid(row=2, column=1)
        
class PaginaDificultad(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameDificultad= tk.Label(self, 
                                        text= "Datos de Dificultad")
        tituloFrameDificultad.config(fg="blue", bg="light blue", font=("Arial", 20))
        tituloFrameDificultad.grid(row=0, column=0, columnspan=3)
        
        def DificultadPresente(self):
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
            
                master.switch_frame(PaginaPosicion)

            comboDificultad= ttk.Combobox(self)
            comboDificultad['values']= ("Tiraje Intercostal", 
                                        "Retracciones",
                                        "Aleteo Nasal",
                                        "Dis.Toraco Abdominal")
            comboDificultad.state(["readonly"])
            comboDificultad.bind("<<ComboboxSelected>>", dificultadElegida)
            comboDificultad.grid(row=2, column=0, columnspan=3)
        
        def DificultadAusente(self):
            paramEvaluar.TEPR(True)
            paramEvaluar.SAT(0)
            paramEvaluar.SAC(0.0) 
        
            master.switch_frame(PaginaPosicion)

        self.imagenRespiracionDificultadSi= tk.PhotoImage(file= "Imagenes\Respiracion\dificultadSi.png")
        self.imagenRespiracionDificultadNo= tk.PhotoImage(file= "Imagenes\Respiracion\dificultadNo.png")
        
        #dificultadResp = Modulo.DificultadRespiratoriaOpcion()

        botonDificultadPresente= tk.Button(self, 
                                           image= self.imagenRespiracionDificultadSi, 
                                           command= lambda: DificultadPresente(self))
        botonDificultadPresente.grid(row=1, column=0)
        botonDificultadAusente= tk.Button(self, 
                                          image= self.imagenRespiracionDificultadNo, 
                                          command= lambda: DificultadAusente(self))
        botonDificultadAusente.grid(row=1, column=1)
        
class PaginaPosicion(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFramePosicion= tk.Label(self, 
                                      text= "Posicion Patologica")
        tituloFramePosicion.config(fg="blue", bg="light blue", font=("Arial", 20))
        tituloFramePosicion.grid(row=0, column=0, columnspan=3)

        self.imagenRespiracionPosicionSi= tk.PhotoImage(file= "Imagenes\Respiracion\posicionSi.png")
        self.imagenRespiracionPosicionNo= tk.PhotoImage(file= "Imagenes\Respiracion\posicionNo.png")
        
        #posicionPatologica = Modulo.PosicionPatologicaOpcion()
        
        def PosicionSi(self):
            def posicionElegida(*args):
                comboPosicionElegida= comboPosicion.get()
                
                if comboPosicionElegida== "Tripode":
                    paramEvaluar.TEPR(False)
                elif comboPosicionElegida=="Olfateo":
                    paramEvaluar.TEPR(False)
                elif comboPosicionElegida=="Cabeceo":
                    paramEvaluar.TEPR(False)
                    
                master.switch_frame(PaginaAntecedentes)

            comboPosicion= ttk.Combobox(self)
            comboPosicion['values']= ("Tripode",
                                      "Olfateo",
                                      "Caebeceo")
            comboPosicion.state(["readonly"])
            comboPosicion.bind("<<ComboboxSelected>>", 
                               posicionElegida)
            comboPosicion.grid()
        
        def PosicionNo(self):
            paramEvaluar.TEPR(True)
            paramEvaluar.SAT(0)
            paramEvaluar.SAC(0.0)
            
            master.switch_frame(PaginaAntecedentes)

        botonPosicionSi= tk.Button(self, 
                                   image= self.imagenRespiracionPosicionSi, 
                                   command= lambda: PosicionSi(self))
        botonPosicionSi.grid(row=1, column=0)
        botonPosicionNo= tk.Button(self, 
                                   image= self.imagenRespiracionPosicionNo, 
                                   command= lambda: PosicionNo(self))
        botonPosicionNo.grid(row=1, column=1)
               
#A partir de estos frames los combobox ya no aparecen. Se mantiene la misma estructura anterior. 
class PaginaAntecedentes(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameAntecedentes= tk.Label(self, 
                                          text= "Antecedentes")
        tituloFrameAntecedentes.config(fg="blue", bg="light blue", font=("Arial", 20))
        tituloFrameAntecedentes.grid(row=0, column=0, columnspan=3)
        subtituloFrameAntecedentes= tk.Label(self, 
                                             text="Enfermedades Cronico-Degenerativas o Uso de Esteroides")
        subtituloFrameAntecedentes.config(fg="blue", bg="light blue", font=("Arial", 10))
        subtituloFrameAntecedentes.grid(row=1, column=0, columnspan=3)

        self.imagenAntecedentesSi= tk.PhotoImage(file= "Imagenes\Antecedentes\cantecedentesSi.png")
        self.imagenAntecedentesNo= tk.PhotoImage(file= "Imagenes\Antecedentes\cantecedentesNo.png")
        
        antecedentes = Modulo.AntecedentesOpcion()

        botonAntecedentesPresentes= tk.Button(self, 
                                              image= self.imagenAntecedentesSi, 
                                              command= lambda: (antecedentes.Presentes(), [master.switch_frame(PaginaAbuso)]))
        botonAntecedentesPresentes.grid(row=3, column=0)
        botonAntecedentesNegados= tk.Button(self, 
                                            image= self.imagenAntecedentesNo, 
                                            command= lambda: (antecedentes.Negados(), [master.switch_frame(PaginaAbuso)]))
        botonAntecedentesNegados.grid(row=3, column=1)

class PaginaAbuso(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tituloFrameAbuso= tk.Label(self, 
                                   text= "Datos de Abuso")
        tituloFrameAbuso.config(fg="blue", bg="light blue", font=("Arial", 20))
        tituloFrameAbuso.grid(row=0, column=0, columnspan=3)

        self.imagenAbusoSi= tk.PhotoImage(file= "Imagenes\Antecedentes\cabusoSi.png")
        self.imagenAbusoNo= tk.PhotoImage(file= "Imagenes\Antecedentes\cabusoNo.png")
        
        abuso = Modulo.AbusoOpcion()

        botonAbusoPresente= tk.Button(self, 
                                      image= self.imagenAbusoSi, 
                                      command= lambda: (abuso.Presente(), [master.switch_frame(PaginaSignosVitales)]))
        botonAbusoPresente.grid(row=1, column=0)
        botonAbusoAusente= tk.Button(self, 
                                     image= self.imagenAbusoNo, 
                                     command= lambda: (abuso.Ausente(), [master.switch_frame(PaginaSignosVitales)]))
        botonAbusoAusente.grid(row=1, column=1)

#En esta clase se muestra un frame con Entrys. Tenemos dos funciones para evitar que se ingresen caracteres alfabeticos y limitar la cantidad de caracteres numericos. 
class PaginaSignosVitales(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tituloFrameSV= tk.Label(self, text= "Signos Vitales")
        tituloFrameSV.grid(row=0, column=1, columnspan=2)
        
        #La idea crear una clase en un modulo aparte que se encargue de esto... 
        #validar= SignosVitales.Validar()
        
        def validar_datos(entrada_datos):            
            if len(entrada_datos) > 3:
                return False
            checks = [] 
            for i, char in enumerate(entrada_datos):
                if i in (3, 3):
                    checks.append(char == "/")
                else:
                    checks.append(char.isdecimal())
            return all(checks)
        
        def validar_temperatura(entrada_datos):
            if len(entrada_datos) > 5:
                return False
            checks = []
            for i, char in enumerate(entrada_datos):
                if i in (2, 2):
                    checks.append(char == ".")
                else:
                    checks.append(char.isdecimal())
            return all(checks)

        tk.Label(self, text= "Frecuencia Cardiaca").grid(row=2, column=1, sticky="e")
        freCardiaca= tk.Entry(self,
                              validate="key",
                              validatecommand=(self.register(validar_datos), "%P"))
        freCardiaca.grid(row=2, column=2)

        tk.Label(self, text= "Frecuencia Respiratoria").grid(row=3, column=1, sticky="e")
        freRespiratoria= tk.Entry(self,
                                  validate="key",
                                  validatecommand=(self.register(validar_datos), "%P"))
        freRespiratoria.grid(row=3, column=2)
        
        tk.Label(self, text= "Presion Sistolica").grid(row=4, column=1, sticky="e")
        presionSistolica= tk.Entry(self,
                                   validate="key",
                                   validatecommand=(self.register(validar_datos), "%P"))
        presionSistolica.grid(row=4, column=2)
        
        tk.Label(self, text= "Presion Diastolica").grid(row=5, column=1, sticky="e")
        presionDiastolica= tk.Entry(self,
                                    validate="key",
                                    validatecommand=(self.register(validar_datos), "%P"))
        presionDiastolica.grid(row=5, column=2)
        
        tk.Label(self, text= "Temperatura").grid(row=6, column=1, sticky="e")
        temperatura= tk.Entry(self,
                               validate="key",
                              validatecommand=(self.register(validar_temperatura), "%P"))
        temperatura.grid(row=6, column=2)
        
        tk.Label(self, text= "Saturacion de oxigeno (satO2)").grid(row=7, column=1, sticky="e")
        saturacionO2= tk.Entry(self,
                               validate="key",
                               validatecommand=(self.register(validar_datos), "%P"))
        saturacionO2.grid(row=7, column=2)
        
        botonSignosVitales= tk.Button(self, 
                                      text= "SIGUIENTE", 
                                      command= lambda: (master.switch_frame(PaginaResultado)))
        botonSignosVitales.grid(row=8, column=0, columnspan=3)

#En esta pagina se dara a conocer el resultado segun la evaluacion de los parametros descritos anteriormente. Tiene que aparecer el frame del color correspondiente a la gravedad de la urgencia medica. 
class PaginaResultado(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        resultado= Resultado.CodigoColor()
        
        if resultado.codigoRojo != 0 and resultado.codigoRojo>resultado.codigoNaranja or resultado.codigoRojo>resultado.codigoAmarillo or resultado.codigoRojo>resultado.codigoVerde or resultado.codigoRojo>resultado.codigoAzul and resultado.codigoRojo>1:
            miLabel= tk.Label(self, text= "CODIGO ROJO", bg= "red")
            miLabel.grid()
        elif resultado.codigoNaranja != 0 and resultado.codigoNaranja>resultado.codigoAmarillo or resultado.codigoNaranja>resultado.codigoVerde or resultado.codigoNaranja>resultado.codigoAzul and resultado.codigoNaranja>1:
            miLabel= tk.Label(self, text= "CODIGO NARANJA", bg= "orange")
            miLabel.grid()
        elif resultado.codigoAmarillo != 0 and resultado.codigoAmarillo>resultado.codigoVerde or resultado.codigoAmarillo>resultado.codigoAzul and resultado.codigoAmarillo>1:
            miLabel= tk.Label(self, text= "CODIGO AMARILLO", bg= "yellow")
            miLabel.grid()
        elif resultado.codigoVerde != 0 and resultado.codigoVerde>resultado.codigoAzul and resultado.codigoVerde>1:
            miLabel= tk.Label(self, text= "CODIGO VERDE", bg= "green")
            miLabel.grid()
        elif resultado.codigoAzul != 0 and resultado.codigoAzul>resultado.codigoRojo and resultado.codigoAzul>1:
            miLabel= tk.Label(self, text= "CODIGO AZUL", bg= "blue")
            miLabel.grid()
        
