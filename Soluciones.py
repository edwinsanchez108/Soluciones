import random
import string
# pandas


nombrereactivo ={
    "NaOH" : "Hidroxido de sodio",
    "HCl" : "Acido clorhidrico"
}
pm = {
    "NaOH" : 40,
    "HCl" : 38
    }

#Falta el diccionario de pureza ( la de la etiqueta comercial, o se puede dejar abierta), eqgramo, densidad
#diccionario o base de datos
#Para algunos calculos se necesita la densidad y otros datos

#dilucion():
#formula, pedir unidades
#hacer igual para las demas opciones


###
def molaridad(volumen,pesomolecular,nombrer):
    concentracion=int(input("Que concentracion [moles/L] "))
    cmolaridad=volumen*concentracion*pesomolecular #*pureza
    print ("se requieren " + str(cmolaridad) + " g de " +str(nombrer))
    
def molalidad(volumen,pesomolecular,nombrer):
    concentracion=int(input("Que concentración [mol soluto/Kg de solvente]"))
    cmolalidad=volumen*0.001*concentracion*pm #*pureza
    print ("Se requieren " + str(cmolalidad) + " g de " +str(nombrer))

def normalidad (volumen,pesomolecular,nombrer):
    concentracion=int(input("Que concentración [equivalente gramo / L de soliución] [N]"))
    cnormalidad = volumen*concentracion*pesomolecular #*pureza*eqgramo
    print ("Se requieren " + str(cnormalidad) + " g de " +str(nombrer))

#def pesopeso():

#def pesovolumen():

#def volumenvolumen():

####

def tipos_de_concentracion(tconcentracion,volumen,pesomolecular,nombrer):
    if tconcentracion == 1:
        molaridad(volumen,pesomolecular,nombrer)
    elif tconcentracion == 2:
        molalidad (volumen,pesomolecular,nombrer) #densidad, falta llamar el dato
    elif tconcentracion == 3:
        normalidad(volumen,pesomolecular,nombrer) #equivalente gramo
    #elif concentracion == 4:
    #    pesopeso()
    #elif concentracion == 5:
    #    pesovolumen()
    #elif concentracion == 6:
    #    volumenvolumen()
    else:
        Er=input("Opcion no valida")  

def solucion():
    volumen=int(input("Que volumen desea preparar [L]"))
    reactivo=str(input("Formula del reactivo que va trabajar?"))
    if reactivo in nombrereactivo: #Verificacion del reactivo en el diccionario
        nombrer=(nombrereactivo.get(reactivo))
        pesomolecular=(pm.get(reactivo)) #Falta agregar pureza y lso demas datos, los buscadores deben estar en una función
        #pm, pureza, densidad.
    else:
        print("No se encontró el reactivo")
        #nombrer=str(input("nombre del reactivo")) #Se debe crear la función solucion rápida (manual) para correrla en todos los tipos de concentraciones
        #nombrereactivo[reactivo] = (nombrer)
           
    tconcentracion=int(input("""Que tipo de concentracion
    1- Molaridad
    2- Molalidad
    3- Normalidad
    4- % peso/peso
    5- % peso/volumen
    6- % volumen/volumen
    """))

    tipos_de_concentracion(tconcentracion,volumen,pesomolecular,nombrer) #nombre de reactivo, pm, pureza

def opciones(option):
    
    if option == 1:
        solucion()   
    #elif option == 2:
    #    dilucion()
    #elif option == 3:
    #    estandarizacion()
    #elif option == 4:
    #    creditos() #y demás opciones
    else:
        numero=input("Opcion no valida")  
        #devolver al menu, revisar errores 

def run():

    menu = """
    Bienvenidos a la preparacion de soluciones

    Que desea hacer hoy

    1 - Solucion
    2 - Dilucion
    3 - Estandarizacion
    4 - Conversor de concentraciones
    3 - Ver lista de compuestos guardados
    4 - Ver creditos
        ****_
    """
    option=int(input(menu))

    opciones(option)


if __name__ == "__main__":
    run()