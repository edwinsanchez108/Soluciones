#Para qué importas random y string?

import random
import string
# pandas


nombre_reactivo ={
    "NaOH" : "Hidroxido de sodio",
    "HCl" : "Acido clorhidrico"
}
pm = {
    "NaOH" : 40,
    "HCl" : 38
    }

"""
Falta:
- Diccionario de pureza (basado en etiqueta o ingresa por el usuario)
- Para algunos cálculo se necesita densidad y otros datos
"""

#dilucion():
#formula, pedir unidades
#hacer igual para las demas opciones
"""
Documentar cada variable
"""

def molaridad(volumen,peso_molecular,nombrer):
    concentracion: int= (input("Que concentracion [moles/L] "))
    cmolaridad=volumen*concentracion*peso_molecular #*pureza
    print ("se requieren de " + str(cmolaridad) + " g de " +str(nombrer))

    
def tipos_de_concentracion(tconcentracion,volumen,peso_molecular,nombrer):
    if tconcentracion == 1:
        molaridad(volumen,peso_molecular,nombrer) #pm
    #elif concentracion == 2:
    #    molalidad ()
    #elif concentracion == 3:
    #    normalidad()
    #elif concentracion == 4:
    #    pesopeso()
    #elif concentracion == 5:
    #    pesovolumen()
    #elif concentracion == 6:
    #    volumenvolumen()
    else:
        Er=input("Opcion no valida")  # Las variables en Python nunca empiezan por mayúsculas

def solucion():
    volumen: int= (input("Que volumen desea preparar [L]"))
    reactivo: str= (input("Formula del reactivo que va trabajar?"))
    if reactivo in nombre_reactivo: #Verificacion del reactivo en el diccionario
        nombrer=(nombre_reactivo.get(reactivo))
        peso_molecular=(pm.get(reactivo)) #Falta agregar pureza y lso demas datos, los buscadores deben estar en una función
        #pm, pureza, densidad.
    else:
        print("No se encontró el reactivo")
        #nombrer=str(input("nombre del reactivo")) #Se debe crear la función solucion rápida (manual) para correrla en todos los tipos de concentraciones
        #nombrereactivo[reactivo] = (nombrer)
           
    tconcentracion: int= (input("""Que tipo de concentracion
    1- Molaridad
    2- Molalidad
    3- Normalidad
    4- % peso/peso
    5- % peso/volumen
    6- % volumen/volumen
    """))

    tipos_de_concentracion(tconcentracion,volumen,peso_molecular,nombrer) #nombre de reactivo, pm, pureza

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
    5 - Ver lista de compuestos guardados
    6 - Ver creditos
        ****_
    """
    option=int(input(menu))

    opciones(option)


if __name__ == "__main__":
    run()