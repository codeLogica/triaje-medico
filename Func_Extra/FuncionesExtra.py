from datetime import date, datetime

#Funcion para corroborar que se ingresen caracteres alfabeticos en el nombre y que sean en mayusculas. 
def ValidarMayuscula(*letras):
    validacion= []
    if len(letras) == None:
        return False
    for char in letras:
        if char.isupper():
            validacion.append(char)
        else:
            return False
        
    DevolverNombre(validacion)
    return all(validacion)

def DevolverNombre(nombre):
    nNombre= nombre

#Funcion para corrobar el ingreso de la fecha de nacimiento con datos numericos y con 8 digitos a lo maximo (2 dia/2 mes/4 año).
def ValidarEdad(*f_nacimiento):
    validacion = [] 
    if len(f_nacimiento) == None:
        return False
    for char in f_nacimiento:
        if len(char) > 10:
            return False
        elif char.isdecimal(): #Corroborar que sea caracter numerico
            validacion.append(char) 
            
            listaDias= ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
            listaMeses= ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
            listaAgnos= list(range(1901, 3001))
            
            #Corroborar que la fecha sea valida. 
            if len(validacion[0])==2:
                if (validacion[0][:2]) not in listaDias:
                    return False
            elif len(validacion[0])==4:
                if (validacion[0][2:4]) not in listaMeses:
                    return False
            elif len(validacion[0])==8:
                if int(validacion[0][4:]) not in listaAgnos:
                    return False
                elif len(validacion[0])==8:
                    hoy= datetime.now()

                    while True:
                        try:
                            fechIngresada= datetime.strptime(validacion[0], "%d%m%Y")
                            if fechIngresada > hoy:
                                return False
                            break
                        except ValueError:
                            print("Fecha inválida")
                            return False
        else:
            return False

    CalcularEdad(validacion[0])
    return all(validacion)

def CalcularEdad(f_nacimiento_comprobacion):    
    #Se comprueba que se tengan los 10 caracteres (8 digitos)
    if len(f_nacimiento_comprobacion) == 8:
        diaActual= datetime.now()
        diaNacimiento= datetime.strptime(f_nacimiento_comprobacion, "%d%m%Y")
        calculoEdad= (diaActual - diaNacimiento)
                            
        diferenciaAgnos= calculoEdad.days / 365
        diferenciaMeses= calculoEdad.days / 30  
        diferenciaDias= calculoEdad.days
        
        DevolverEdad(diferenciaAgnos, diferenciaMeses, diferenciaDias)

def DevolverEdad(agnos, meses, dias):  
    edadPx= None                          
    if dias < 28:
        edadPx= f"{dias} dias"
    elif meses < 12:
        edadPx= f"{meses} meses"
    elif meses < 24:
        edadPx= f"{meses} meses"
    elif agnos >2 and agnos <6:
        edadPx= f"{agnos} años"
    elif agnos >6 and agnos <10:
        edadPx= f"{agnos} años"
    elif agnos > 11 and agnos <19:
        edadPx= f"{agnos} años"
    
    return edadPx