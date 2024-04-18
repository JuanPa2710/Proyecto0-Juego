from random import randrange
import time
import keyboard

historialJugador = []
historialMaquina = []
jugadas = {"t": ["l", "p"], "p": ["r", "s"], "r": ["l", "t"], "l": ["p", "s"], "s": ["r", "t"]}
simbologia = {"r": "Roca", "p": "Papel", "t": "Tijeras", "l": "Lagarto", "s": "Spock"}

def main():
    """
    Proyecto 0 de Taller de programación. Primer semestre del 2024.
    Algoritmo que simula el juego "Roca, papel, tijeras, lagarto y Spock".
    Creado por Felipe Torres y Juanpa Jiménez.
    """
    global historialJugador
    historialJugador = []
    
    mensajeBienvenida()
    continuar = True
    
    nombreJugador = obtenerNombre()
    
        
    while continuar == True:
        opcion = menuPrincipal()
        mismaRonda = False
        resultado = ""
        
        if(opcion == 6):
            estadisticas()
        elif(opcion == 7):
            limpiarPantalla()
            continuar = False
        else:
            mismaRonda = True
            
        marcador = {"u": 0, "m": 0, "e": 0}
        while mismaRonda == True:
            
            jugadaMaquina = obtenerJugadaMaquina(opcion, resultado)
            jugadaUsuario = obtenerJugadaUsuario()
            
            if jugadaUsuario == "x":
                mismaRonda = False
                historialJugador = historialJugador[:(len(historialJugador) - 1)]
                limpiarPantalla()
            else:
                resultado = verificarResultado(jugadaMaquina, jugadaUsuario)
                mostrarMarcador(resultado, nombreJugador, jugadaUsuario, jugadaMaquina)
                marcador[resultado] += 1
                #time.sleep(4)
                #print('Presione "Enter" para continuar...')
                #keyboard.wait('enter', True)
                
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
$$$$$$$$$$$$        ++++    ++++     &&&&&&&&&&&&&
  ++++++++         +  ++++++++  +    &&&&&&&&&&&&&
  ++++++++          ++++    ++++     &&&&&&&&&&&&&
                                                  
                                                   
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


def menuPrincipal():
    """
    Pregunta al usuario el nivel con el que desea jugar, muestra opciones sobre 
    las estadísticas y le permite salir del juego.
    Entradas y restricciones:
    -Ninguna
    Salidas:
    -Devuelve el nivel de dificultad, la página de estadísticas o cierra el juego.
    """
    nivel = input("\nFacil = 1\nMedio = 2\nDifícil = 3\nExperto = 4\nExtremo = 5\n\nEstadísticas de juego = 6\nSalir del Juego = 7\n\nEscoja el nivel de dificultad: ")

    while validarNivel(nivel) == False or (int(nivel) < 1 or int(nivel) > 7 ):
        print("La opción ingresada no es valida. Por favor ingresela de nuevo")
        nivel = input("\nFacil = 1\nMedio = 2\nDifícil = 3\nExperto = 4\nExtremo = 5\n\nEstadísticas de juego = 6\nSalir del Juego = 7\n\nEscoja el nivel de dificultad: ")

    limpiarPantalla()
    
    return int(nivel)

def estadisticas():
    """
    Procedimiento que retorna las estadísticaas del juego en general e información relevante para el usuario.
    E y R:
        - Ninguna
    S:
        - Imprime la información relevante en pantalla
    """
    limpiarPantalla()
    if len(historialJugador) == 0:
        print("Aún no se han jugado partidas :p")
    else:
        victorias = 0
        derrotas = 0
        empates = 0
        armaGanadora = []
        armaPerdedora = []
        #armaFavorita = {arma: historialJugador.count(arma)for arma in historialJugador}
        for x in range(len(historialJugador)):
            if verificarResultado(historialJugador[x], historialMaquina[x]) == "m":
                victorias =+ 1
                armaGanadora += historialJugador[x]
            elif verificarResultado(historialJugador[x], historialMaquina[x]) == "u":
                derrotas =+ 1
                armaPerdedora += historialJugador[x]
            else:
                empates += 1
        print(f"Victorias: {victorias}\t{float(victorias) / len(historialJugador) * 100}%")
        print(f"Derrotas: {derrotas}\t{float(derrotas) / len(historialJugador) * 100}%")
        print(f"Empates: {empates}\t{float(empates) / len(historialJugador) * 100}%\n")
        #print(f"Arma más usada: {armaFavorita}")


def validarNivel(n):
    try:
       int(n)
       return True
    except:
        return False


def validarArma(arma):
    """
    Función que valida si el nivel ingresado por el usuario
    es un opción valida

    Entradas y restricciones:
    -Opción de arma escogida por el usuario
    Salidas:
    -True si el arma escogida es una opción valida, sino False
    """
    
    armas = ["r", "p", "t", "l", "s","x"]

    return False if(not arma in armas) else True
        

def obtenerJugadaUsuario():
    """
    Función que obtiene el arma que usará el usuario en esta ronda
    Entradas y restricciones:
    -Ninguna
    Salidas:
    -Devuelve el arma del usuario
    """
    global historialJugador
    
    arma = input("\nOpciones de arma: " +
                 "\n\nR para piedra \nP para papel \nT para tijera \nL para lagarto \nS para spock \nX para salir \n\nEscoja su arma: ")

    armaLower = arma.lower()
    
    while(validarArma(armaLower) == False):
        limpiarPantalla()
        print("¡Opción invalida¡ Intente de nuevo")
        arma = input("\nOpciones de arma: " +
                 "\n\nR para piedra \nP para papel \nT para tijera \nL para lagarto \nS para spock \nX para salir \n\nEscoja su arma: ")
        armaLower = arma.lower()

    historialJugador += armaLower 
    return armaLower

def obtenerJugadaMaquina(nivel, resultado):
    """
    Función que a partir de la jugada del usuario y nivel de dificultad de juego
    escoge el arma con la que juega la maquina
    Entradas y restricciones:
    -Nivel de dificultad: tiene que ser un número del 1 al 5
    -Resultado: ultimo ganador o empate de la partida
    Salidas:
    -De vuelve el arma con la que jugará la maquina
    """
    global historialMaquina
    jugada = ""
    if(nivel == 1):
        jugada = primerNivel()
        historialMaquina += jugada
        return jugada
    elif(nivel == 2):
        jugada = segundoNivel()
        historialMaquina += jugada
        return jugada
    elif(nivel == 3):
        jugada = tercerNivel()
        historialMaquina += jugada
        return jugada
    elif(nivel == 4):
        jugada = cuartoNivel(resultado)
        historialMaquina += jugada
        return jugada
    elif nivel == 5:
        print("simular nivel 5")
        raise Exception("Niven aún no implementado")

def verificarResultado(jugadaUsuario, jugadaMaquina):
    """
    Función que compara las jugadas del usuario y de la máquina,
    imprime el ganador y devuelve la inicial en minúscula del ganador
    
    Entradas y Restricciones:
    - jugadaMáquina
    - jugadaUsuario
    Salidas:
    - u: Victoria del usuario
    - m: Victoria de la máquina
    - e: Empate
    """
    if(jugadaUsuario == jugadaMaquina):
        return "e"
    elif(jugadaMaquina in jugadas[jugadaUsuario]):
        return "m"
    else:
        return "u"
    
def mostrarMarcador(resultado, usuario, jugUsuario, jugMaquina):
    """
    Procedimiento que recibe el resultado de la ronda e imprime la información,
    del ganador

    Entradas:
    -Resultado: string con inicial del resultado de la ronda (m = maquina, e = empate y u = usuario)
    """
    print(f"\nJugada de {usuario.capitalize()}: {simbologia[jugUsuario]}")
    print(f"Jugada de la máquina: {simbologia[jugMaquina]}")
    
    if(resultado == "e"):        
        print("\nLa ronda concluyó con empate!")
    elif(resultado == "u"):
        print(f"La victoria es de {usuario.capitalize()}!")
    else:
        print("La victoria es para la máquina!")

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

def segundoNivel():
    """
    Función que utiliza la estrategia Contra los más comunes(Explicación en
    la documentación)
    Entradasy restricciones:
    -Ninguna
    Salidas:
    -Una jugada (string con la letra inicial de la jugada escogida al azar)
    """
    if(len(historialJugador) <= 8):
        return primerNivel()
    
    historialNuevo = {( historialJugador.count(x) * 100 // len(historialJugador)): x for x in historialJugador}
    porcen = dict(sorted(historialNuevo.items(), reverse = True))

    print(porcen)
    
    for i in range(len(porcen), 2, -1):
        porcen.popitem()
    posibilidades = []

    
    for llave in jugadas:
        for valor in porcen.values():            
            if(valor in jugadas[llave]):
                posibilidades += llave
                
    eliminarRepetido(posibilidades)
    
    print(posibilidades)
    return posibilidades[randrange(len(posibilidades))]

def tercerNivel():
    """
    Función que predice que el jugador eligirá una opción que le gane a lo que él mismo
    jugó previamente, y actúa en consecuencia.
    Entradas y Restricciones:
    - Ninguna
    Salidas:
    - String (letra inicial de la jugada)
    """
    if len(historialJugador) < 1:
        return primerNivel()
    
    ultimaJugadaUsuario = []
    posibleJugadaUsuario = []
    posibilidades = []
    ultimaJugadaUsuario = historialJugador[len(historialJugador) - 1]
    for x in jugadas:
        if ultimaJugadaUsuario in jugadas[x]:
            posibleJugadaUsuario += x
    for y in posibleJugadaUsuario:
        for x in jugadas:
            if y in jugadas[x]:
                posibilidades += x
        posibilidades = eliminarRepetido(posibilidades)
        
        print(posibilidades)
        return posibilidades[randrange(len(posibilidades))]

def cuartoNivel(resultado):
    """
    Función que utiliza la estrategia Win-Stay/Lose-Shift(Explicación en
    la documentación)

    Entradas y restricciones:
    -Resultado: esto indica quien ganó la última partida
    Salidas:
    -Una jugada (string con la letra inicial de la jugada escogida al azar)
    """
    if(resultado == ""):
        return primerNivel()
    posibilidades = []
    if(resultado == "u"):
        ultimaJugada = historialJugador[len(historialJugador) - 1] #t: s, p
        posibilidades = [x for x in jugadas if ultimaJugada in jugadas[x]] 
        return posibilidades[randrange(len(posibilidades))]
    elif(resultado == "m" or resultado == "e"):
        ultimaJugada = historialMaquina[len(historialMaquina) - 1]
        posibleAtaque = [x for x in jugadas if ultimaJugada in jugadas[x]]
        i = 0
        posibleContra = []
        for jugada in jugadas:
            for i in range(2):
                if(posibleAtaque[i] in jugadas[jugada]):
                    posibleContra += jugada
        posibilidades = [x for x in posibleContra if posibleContra.count(x) >= 2]
        posibilidaes = eliminarRepetido(posibilidades)
        return posibilidades[randrange(len(posibilidades))]

    

def eliminarRepetido(L):
    """
    Función que elimina valores repetidos si lo hay en una lista
    Entradas y restricciones:
    -L: lista de valores cualesquiera
    Salidas:
    -Lista con valores repetidos eliminados si lo hay, sino
    devuelve la misma lista
    """
    for letra in L:
        if(L.count(letra) > 1):
            for i in range(L.count(letra) - 1):
                L.remove(letra)
    return L


    
def mensajeDespedida(nombreJugador):
    """
    Imprime un mensaje de despedida para cuando el usuario quiera dejar de jugar
    Entradas y restricciones:
    - El nombre del usuario
    Salidas:
    - Texto de despedida
    """
    print("Gracias por jugar, " + nombreJugador + ". Hasta la próxima...")
