from datetime import datetime

#Funcion para corroborar que se ingresen caracteres alfabeticos en el nombre y que sean en mayusculas. 
def ValidarMayuscula(*letraMayuscula):
    validacion= []
    if len(letraMayuscula) == None:
        return False
    for char in letraMayuscula:
        if char.isupper():
            validacion.append(char)
        else:
            return False
        
    #DevolverNombre(validacion)
    return all(validacion)

def DevolverNombre(nombre):
    nNombre= f"Paciente {nombre}"
    return nNombre

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
                            
        diferenciaAños= calculoEdad.days / 365
        diferenciaMeses= calculoEdad.days / 30  
        diferenciaDias= calculoEdad.days
        
        DevolverEdad(diferenciaAños, diferenciaMeses, diferenciaDias)

def DevolverEdad(años, meses, dias):  
    edadPx= None                          
    if dias < 28:
        edadPx= f"Recien Nacido {dias} dias"
    elif meses < 12:
        edadPx= f"Lactante Menor {meses} meses"
    elif meses < 24:
        edadPx= f"Lactante Mayor {meses} meses"
    elif años >2 and años <6:
        edadPx= f"Preescolar {años} años"
    elif años >6 and años <10:
        edadPx= f"Escolar {años} años"
    elif años > 11 and años <19:
        edadPx= f"Adolescente {años} años"
    
    return edadPx