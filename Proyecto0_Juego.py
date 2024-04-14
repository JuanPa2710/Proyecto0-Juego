from random import randrange
historial = []

""" Funcionees que faltan por hacer:            
- verificarResultado(jugadaMaquina, jugadaUsuario)
Función que comapra las jugadas del usuario y de la máquina, imprime el ganador y devuelve la inicial en minúscula del ganador
Entradas y Restricciones:
    - jugadaMáquina
    - jugadaUsuario
    Salidas:
    - u: Victoria del usuario
    - m: Victoria de la máquina
    - e: Empate
    
- mostrarMarcador()
Procedimiento que recibe 
"""

def main():
    """
    Proyecto 0 de Taller de programación. Primer semestre del 2024.
    Algoritmo que simula el juego "Roca, papel, tijeras, lagarto y Spock".
    Creado por Felipe Torres y Juanpa Jiménez.
    """
    
    mensajeBienvenida()
    continuar = True
    nombreJugador = obtenerNombre()
    global historial
    historial = []
    while continuar == True:
        nivelDificultad = obtenerNivel()
        mismaRonda = True
        marcador = {"u": 0, "m": 0, "e": 0}
        while mismaRonda == True:
            limpiarPantalla()
            print("¡Empieza el juego¡")
            
            jugadaMaquina = obtenerJugadaMaquina(nivelDificultad)
            jugadaUsuario = obtenerJugadaUsuario()
            if jugadaUsuario != "x":
                resultado = verificarResultado(jugadaMaquina, jugadaUsuario)
                mostrarMarcador(resultado)
                marcador[resultado] += 1 
            else:
                mismaRonda == False
                
    mensajeDespedida(nombreJugador)



def limpiarPantalla():
    """
    Procedimiento que limpia la pantalla de juego, despeja esta con 40 espacio en blanco

    Entradas y restricciones:
    -Ninguna
    Salidas:
    -40 espacios en blanco
    """
    print("\n" * 40)

def mensajeBienvenida():
    """Imprime un mensaje de bienvenida al usuario
    Entradas y restricciones:
    - Ninguna
    Salidas:
    - El mensaje de bienvenida"""
    print("""
      $$$           &&&      &&&     &&&&&&&&&&&&&
  $$  $$$$$         &&&      &&&     &&&&&&&&&&&&&
$$$$  $$$$$         &&&&    &&&&     &&&&&&&&&&&&&
$$$$  $$$$$           &&    &&       &&&&&&&&&&&&&
$$$$  $$$$$ $$$       &&&&&&&&       &&&&&&&&&&&&&
$$$$$$$$$$$$$$        ++&&&&++       &&&&&&&&&&&&&
$$$$$$$$$$$$        ++++xXXx++++     &&&&&&&&&&&&&
  xxxxxxxxx         ++++++++++++     &&&&&&&&&&&&&
  ++++++++            ++    ++       &&&&&&&&&&&&&
                                                  
                                                  
        xx     xxx                                
       xxxxx   xxxxx                 XXXXXXX      
  xxxx   xxxx    xxx               XXXXXXXXXXX    
xxxxxxxxxxxxxxxxxxxxxx            XXXXXXXXXXXXXX  
xxxxxxxxxxxxxxxxxxxxxxxxx+      XXXXXXXXXXXXXXXXX 
xxxxxxxxxxxxxxxxxxxxxxxxxxx    XXXXXXXXXXXXXXXXXXX
  xxxxx  xxxx    xxx     xxx   XXXXXXXXXXXXXXXXXXX
        xxxxx  +xxxx +xxxxxx   XXXXXXXXXXXXXXXXXXX
       xxxx    xxxx  xxxxx       XXXXXXXXXXXXXXX""")
    print("")
    print("¡Bienvenido al juego de Roca, papel tijeras, lagarto y Spock!")

    

def obtenerNombre():
    """
    Pregunta al usuario, el nombre con el que desea ser conocido en el juego

    Entradas y restricciones:
    -Ninguna
    Salidas:
    -Devuelve el nombre del usuario
    """
    nombre = input("\nIngrese el  nombre con el que desea jugar: ")

    while(type(nombre) != str):
        print("!El nombre tiene que ser de tipo Str")
        nombre = input("Ingrese el  nombre con el que desea jugar: ")

    return nombre



def validarNivel(nivel):
    """
    Función que valida si el nivel ingresado por el usuario
    es un opción de tipo int

    Entradas y restricciones:
    -Opción de nivel escogida por el usuario
    Salidas:
    -True si la opción ingresada es de tipo entero, sino False
    """
    
    valido = True
    
    try:
        int(nivel)
    except:
        valido = False

    return valido



def validarArma(arma):
    """
    Función que valida si el nivel ingresado por el usuario
    es un opción valida

    Entradas y restricciones:
    -Opción de arma escogida por el usuario
    Salidas:
    -True si el arma escogida es una opción valida, sino False
    """
    armaLower = arma.lower()
    armas = ["r", "p", "t", "l", "s","x"]

    return False if(not armaLower in armas) else True



def obtenerNivel():
    """
    Pregunta al usuario, el nivel con el que desea jugar

    Entradas y restricciones:
    -Ninguna
    Salidas:
    -Devuelve el nivel de dificultad a jugar
    """

    nivel = input("\n1.Facil = 1\n2.Algo difícil = 2\n3.Difícil = 3\n4.Experto = 4\n5.Extremo = 5\n\nEscoga el nivel de dificultad: ")

    while(validarNivel(nivel) == False or (int(nivel) < 1 or int(nivel) > 5)):
        print("La opción ingresada no es valida. Por favor ingresela de nuevo")
        nivel = input("\n1.Facil = 1\n2.Algo difícil = 2\n3.Difícil = 3\n4.Experto = 4\n5.Extremo = 5\n\nEscoga el nivel de dificultad: ")

    return int(nivel)



def obtenerJugadaUsuario():
    """
    Función que obtiene el arma que usará el usuario en esta ronda

    Entradas y restricciones:
    -Ninguna
    Salidas:
    -Devuelve el arma del usuario
    """
    global historial
    arma = input("\nOpciones de arma: " +
                 "\n\nR para piedra \nP para papel \nT para tijera \nL para lagarto \nS para spock \nX para salir \n\nEscoja su arma: ")

    while(validarArma(arma) == False):
        limpiarPantalla()
        print("¡Opción invalida¡ Intente de nuevo")
        arma = input("\nOpciones de arma: " +
                 "\n\nR para piedra \nP para papel \nT para tijera \nL para lagarto \nS para spock \nX para salir \n\nEscoja su arma: ")
    historial += [arma]
    return arma



def obtenerJugadaMaquina(nivel):
    """
    Función que a partir de la jugada del usuario y nivel de dificultad de juego
    escoge el arma con la que juega la maquina

    Entradas y restricciones:
    -Nivel de dificultad: tiene que ser un número del 1 al 5
    -Arma del usuario: tiene que ser una arma de las permitidas
    Salidas:
    -De vuelve el arma con la que jugará la maquina
    """

    if(nivel == 1):
        return primerNivel()
    elif(nivel == 2):
        return primerNivel()
    elif(nivel == 3):
        return primerNivel()
    elif(nivel == 4):
        return primerNivel()
    else:
        return primerNivel()



def primerNivel():
    """
    Función que tiene una lista de jugadas y devuelve una de manera aleatoria
    Entradas y restricciones:
    - ninguna
    Salidas:
    - Una jugada (string con la letra inicial de la jugada)
    """
    posibilidades = ["r", "p", "t", "l", "s"]
    return posibilidades[randrange(5)]



def mensajeDespedida(nombreJugador):
    """
    Imprime un mensaje de despedida para cuando el usuario quiera dejar de jugar
    Entradas y restricciones:
    - El nombre del usuario
    Salidas:
    - Texto de despedida
    """
    print("Gracias por jugar, " + nombreJugador + ". Hasta la próxima...")
