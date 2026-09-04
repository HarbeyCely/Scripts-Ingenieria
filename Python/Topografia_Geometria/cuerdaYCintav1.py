'''  Algoritmo para calcular area de un levantamiento topografico con cuerda y cinta metrica'''
'''                          por Harbey Emir Cely - 2201128                                  '''

# IMPORTANTE: solo funciona con poligonos de 3 a 7 vertices.

############################################################################################
# LIBRERIAS
import math
# FUNCION
def calcularAreaPoligono():
    # Recoleccion de datos del diario de campo
    vertices = 4
    distParcial = list()
    for i in range(vertices-1):
        pInicial = 1
        distParcial.insert(i,float(input(f"Ingrese el valor de la distancia parcial de {i+1} a {i+2}: ")))
        if i == vertices-2:
            distParcial.insert(i+1,float(input(f"Ingrese el valor de la distancia parcial de {i+2} a {pInicial}: ")))

    cuerdas = list()
    for i in range(vertices):
        cuerdas.insert(i,float(input(f"Ingrese la longitud de la cuerda de {i+1}: ")))

    radios = list()
    for i in range(vertices):
        radios.insert(i,float(input(f"Ingrese el radio de {i+1}: ")))
    unidad = input("Ingrese unidad de medida de las distancias: ")

    '''
    # Predefinir valores
    distParcial = [27.2, 11.5, 18.4, 16.26]
    cuerdas = [8.63, 7.46, 6.88, 8.85]
    radios = [10, 5, 5, 5]
    unidad = 'm'
    '''
    # Division del poligono en triangulos
    numTriangulos = int()
    if vertices > 2:
        numTriangulos = vertices - 2

    # Funcion para calcular angulo interno
    def calcAngulo(cuerda,radio):
        angulo = 2 * math.asin(cuerda/(2*radio))
        angulo = math.degrees(angulo)
        return angulo
    # Funcion para calcular la interseccion por medio de teorema de cosenos
    def calcularInterseccion(b,c,angulo):
        a = math.sqrt((b**2)+(c**2)-2*b*c*math.cos(angulo))
        return a
    # teorema de senos para calcular angulo
    def teoremaSenosAngulo(b,B,a):
        A = math.asin( (a*math.sin(B)) /b )
        A = math.degrees(A)
        return A
    # Funcion para calcular Area usando formula de Heron y hallando semiperimetro en el proceso
    def calcArea(a,b,c):
        perim = a + b + c
        semip = perim/2
        A = math.sqrt(semip*(semip-a)*(semip-b)*(semip-c))
        return A


    # Guardar angulo y su posicion en listas
    angInternos = list()
    posAng = list()

    for i in range(numTriangulos-1):
        angInternos.insert(i,calcAngulo(cuerdas[2*i],radios[2*i]))
        posAng.append(2*i)

    # Comprobar que posiciones se guardaron para calcular su interseccion
    if 0 in posAng:
        a1 = distParcial[0]
        b1 = distParcial[-1]
        inters1 = calcularInterseccion(a1,b1,angInternos[i])
        a2 = distParcial[1]
        b2 = distParcial[2]
        if 2 in posAng:
            inters2 = calcularInterseccion(a2,b2,angInternos[i])
            
            if 4 in posAng:
                a3 = distParcial[3]
                b3 = distParcial[4]
                inters3 = calcularInterseccion(a3,b3,angInternos[i])
                if 6 in posAng:
                    a4 = distParcial[5]
                    b4 = inters1 
                    # El angulo corregido es el angulo interno necesario para calcular el triangulo 4
                    angCorreg = angInternos[6] - teoremaSenosAngulo(inters1,angInternos[0],distParcial[0])
                    inters4 = calcularInterseccion(a4,b4,angCorreg)
    # Dependiendo del numero de vertices del poligono se suman las areas que lo componen al acumulador areaT
    areaT = 0
    if vertices == 3:
        areaT += calcArea(distParcial[0],distParcial[1],distParcial[2])
    if len(posAng) == 1 and vertices == 4:
        areaT += calcArea(a1,b1,inters1)
        areaT += calcArea(a2,b2,inters1)
    if len(posAng) == 2 and vertices == 5:
        areaT += calcArea(a1,b1,inters1)
        areaT += calcArea(a2,b2,inters2)
        areaT += calcArea(distParcial[3],inters1,inters2)
    if len(posAng) == 3 and vertices == 6:
        areaT += calcArea(a1,b1,inters1)
        areaT += calcArea(a2,b2,inters2)
        areaT += calcArea(a3,b3,inters3)
        areaT += calcArea(inters1,inters2,inters3)
    if len(posAng) == 4 and vertices == 7:
        areaT += calcArea(a1,b1,inters1)
        areaT += calcArea(a2,b2,inters2)
        areaT += calcArea(a3,b3,inters3)
        areaT += calcArea(a4,b4,inters4)
        areaT += calcArea(inters2,inters3,inters4)

    # print('lista de distancias: ',distParcial)
    # print('lista de angulos: ',angInternos)
    # print('inters1: ',inters1)
    # print('perimetro: ',sum(distParcial))
    return f"Area Total del poligono de {vertices} vertices: {round(areaT,3)} {unidad}"

print(calcularAreaPoligono())
