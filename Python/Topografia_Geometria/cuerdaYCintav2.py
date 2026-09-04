'''  Algoritmo para calcular área de un levantamiento topográfico con cuerda y cinta métrica'''
'''                          por Harbey Emir Cely - 2201128                                 '''
'''                        Universidad Industrial de Santander                              '''

# IMPORTANTE: solo funciona con poligonos de 3 a 7 vertices.
# Programacion para calcular el area de un levantamiento topografico
# de baja precision usando el metodo de cuerda y cinta metrica.

############################################################################################
# LIBRERIAS
import math
# FUNCION GENERAL
def calcularAreaPoligono():
    # Recoleccion de datos del diario de campo
    vertices = 4
    distParcial = [27.2, 11.5, 18.4, 16.26]          
    cuerdas = [8.63, 7.46, 6.88, 8.85]
    radios = [10, 5, 5, 5]
    unidad = 'm^2'
    abscisas = [
                0,3,5,10,12.2,15,20,22.94,
                25,30,35,40,45.08,
                47.24,50,55,60,62.26,
                65,70,73.57,76.44,
                79.2,85,90,93.46
                ]
    "Entre corchetes: [  valor  ,  derecha('D') o izquierda('I')   ]                                              "
    detalles = [
                [4.8,'D'],[0,'X'],[2.3,'I'],[4.26,'I'],[0,'X'],[5.08,'D'],[2.15,'D'],[0,'X'],
                [60.5,'D'],[8.26,'D'],[5.08,'D'],[7.29,'D'],[2.16,'I'],
                [0,'X'],[3.22,'D'],[4.05,'D'],[2.98,'D'],[1.06,'D'],
                [2.18,'I'],[2.89,'I'],[0,'X'],[1.8,'I'],
                [0,'X'],[0,'X'],[0,'X'],[0,'X']
                ]
    
    # Division del poligono en triangulos
    numTriangulos = int()
    if vertices > 2:
        numTriangulos = vertices - 2
    #----------------------------------------   FUNCIONES INTERNAS  ----------------------------------------------#
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
    def areaTrianguloRectangulo(base,altura):
        A = (base*altura)/2
        return A

    #-------------------------------------   AREA DEL POLIGONO   --------------------------------------------#
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
    areaP = 0
    if vertices == 3:
        areaP += calcArea(distParcial[0],distParcial[1],distParcial[2])
    if len(posAng) == 1 and vertices == 4:
        areaP += calcArea(a1,b1,inters1)
        areaP += calcArea(a2,b2,inters1)
    if len(posAng) == 2 and vertices == 5:
        areaP += calcArea(a1,b1,inters1)
        areaP += calcArea(a2,b2,inters2)
        areaP += calcArea(distParcial[3],inters1,inters2)
    if len(posAng) == 3 and vertices == 6:
        areaP += calcArea(a1,b1,inters1)
        areaP += calcArea(a2,b2,inters2)
        areaP += calcArea(a3,b3,inters3)
        areaP += calcArea(inters1,inters2,inters3)
    if len(posAng) == 4 and vertices == 7:
        areaP += calcArea(a1,b1,inters1)
        areaP += calcArea(a2,b2,inters2)
        areaP += calcArea(a3,b3,inters3)
        areaP += calcArea(a4,b4,inters4)
        areaP += calcArea(inters2,inters3,inters4)
    
    #--------------------------------------   DETALLES  --------------------------------------------------#
    aDD=0
    aDI=0
    detalle=float()
    contadorTriang = 0
    for i in range(len(detalles)-1):
        if i==0 and detalles[0][0]==0:
            detalle = detalles[1][0]
        elif i==0 and detalles[0][0]!=0:
            detalle = detalles[0][0]
        if i!=0:
            if detalles[i][0] == 0:
                if detalles[i-1][0]!=0 and i == contadorTriang+1:
                    detalle = detalles[i-1][0]
                    detalles[i][1] = detalles[i-1][1]
                elif detalles[i+1][0]!=0 and i == contadorTriang:
                    detalle = detalles[i+1][0]
                    detalles[i][1] = detalles[i+1][1]
                else:
                    detalle=0
                    
            else:
                if i == contadorTriang+1:
                    detalle = detalles[i][0]
                elif i == contadorTriang and detalles[i+1][0] != 0:
                    detalle = detalles[i+1][0]
                    detalles[i][1] = detalles[i+1][1]
                else:
                    detalle = detalles[i][0]
                    

        if detalles[i][1] == "D":
            aDD+=areaTrianguloRectangulo(abscisas[i+1]-abscisas[i],detalle)
            contadorTriang+=1
            #print(f"{i} D: {round(aDD,3)}, contador {contadorTriang}, {detalle}")
        elif detalles[i][1] == "I":
            aDI+=areaTrianguloRectangulo(abscisas[i+1]-abscisas[i],detalle)
            contadorTriang+=1
            #print(f"{i} I: {round(aDI,3)}, contador {contadorTriang}, {detalle}")
    aTotalDetalles = aDD-aDI
    aTotal = areaP + aTotalDetalles

    print("--------------------------------------------------")
    print(f"Diferencia del área de detalles: {round(aTotalDetalles,3)} {unidad}")
    print(f"Área del poligono sin detalles: {round(areaP,3)} {unidad}")
    print("--------------------------------------------------")
    # print('lista de distancias: ',distParcial)
    # print('lista de angulos: ',angInternos)
    # print('inters1: ',inters1)
    # print('perimetro: ',sum(distParcial))
    return f"Área Total del poligono de {vertices} vertices incluyendo detalles: {round(aTotal,3)} {unidad}"

print(calcularAreaPoligono())
