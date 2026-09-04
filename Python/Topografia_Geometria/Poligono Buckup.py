'''  Algoritmo para calcular area de un levantamiento topografico con cuerda y cinta metrica'''
'''                          por Harbey Emir Cely - 2201128                                 '''
'''                        Universidad Industrial de Santander                              '''

# IMPORTANTE: solo funciona con poligonos de 3 a 7 vertices.

############################################################################################
# LIBRERIAS
import math
# FUNCION
def calcularAreaPoligono():
    # Recoleccion de datos del diario de campo
    vertices = 5
    # distParcial = list()
    # for i in range(vertices-1):
    #     pInicial = 1
    #     distParcial.insert(i,float(input(f"Ingrese el valor de la distancia parcial de {i+1} a {i+2}: ")))
    #     if i == vertices-2:
    #         distParcial.insert(i+1,float(input(f"Ingrese el valor de la distancia parcial de {i+2} a {pInicial}: ")))

    # cuerdas = list()
    # for i in range(vertices):
    #     cuerdas.insert(i,float(input(f"Ingrese la longitud de la cuerda de {i+1}: ")))

    # radios = list()
    # for i in range(vertices):
    #     radios.insert(i,float(input(f"Ingrese el radio de {i+1}: ")))
    # unidad = input("Ingrese unidad de medida de las distancias: ")

    
    # Predefinir valores
    distParcial = [22.94, 22.14, 17.18, 14.18, 17.02]          #[27.2, 11.5, 18.4, 16.26]
    cuerdas = [8.63, 7.46, 6.88, 8.85]
    radios = [10, 5, 5, 5]
    unidad = 'm'
    abscisas = [
                0,3,5,10,12.2,15,20,22.94,
                25,30,35,40,45.08,
                47.24,50,55,60,62.26,
                65,70,73.57,76.44,
                79.2,85,90,93.46
                ]
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
    
    # Calcular detalles
    aDetD = 0
    aDetI = 0
    # for i in range(len(detalles)-2):
        
    #     if abscisas[0] == 0:
    #         if detalles[0][0] != 0 and detalles[i+2][0] != 0:
    #             if detalles[0][1] == 'D':
    #                 aDetD += areaTrianguloRectangulo((abscisas[1]-abscisas[0]),detalles[0][0])
    #             elif detalles[0][1] == 'I':
    #                 aDetI += areaTrianguloRectangulo((abscisas[1]-abscisas[0]),detalles[0][0])
                
    #             if detalles[i+2][0] != 0:
    #                 detalle = float()
    #                 if detalles[i+2][0] != 0:
    #                     detalle = detalles[i+2][0]
    #                 else:
    #                     detalle = detalles[i+1][0]
    #             elif detalles[i+2][0] == 0:
    #                 detalle = 0
                
    #             if detalles[i+2][1] == 'D':
    #                 aDetD += areaTrianguloRectangulo((abscisas[i+2]-abscisas[i+1]),detalle)
    #             elif detalles[i+2][1] == 'I':
    #                 aDetI += areaTrianguloRectangulo((abscisas[i+2]-abscisas[i+1]),detalle)
              
    #     elif abscisas[0] != 0:
    #         print('La abscisa inicial debe ser 0')

    ar1 = areaTrianguloRectangulo(abscisas[1],detalles[0][0])
    ar2 = areaTrianguloRectangulo(abscisas[2]-abscisas[1],detalles[2][0])
    ar3 = areaTrianguloRectangulo(abscisas[3]-abscisas[2],detalles[3][0])
    ar4 = areaTrianguloRectangulo(abscisas[4]-abscisas[3],detalles[3][0])
    ar5 = areaTrianguloRectangulo(abscisas[5]-abscisas[4],detalles[5][0])
    ar6 = areaTrianguloRectangulo(abscisas[6]-abscisas[5],detalles[6][0])
    arB = areaTrianguloRectangulo(abscisas[7]-abscisas[6],detalles[6][0])
    ar7 = areaTrianguloRectangulo(abscisas[8]-abscisas[7],detalles[8][0])
    ar8 = areaTrianguloRectangulo(abscisas[9]-abscisas[8],detalles[9][0])
    ar9 = areaTrianguloRectangulo(abscisas[10]-abscisas[9],detalles[10][0])
    ar10 = areaTrianguloRectangulo(abscisas[11]-abscisas[10],detalles[11][0])
    arC = areaTrianguloRectangulo(abscisas[12]-abscisas[11],detalles[12][0])
    ar11 = areaTrianguloRectangulo(abscisas[13]-abscisas[12],detalles[12][0])
    ar12 = areaTrianguloRectangulo(abscisas[14]-abscisas[13],detalles[14][0])
    ar13 = areaTrianguloRectangulo(abscisas[15]-abscisas[14],detalles[15][0])
    ar14 = areaTrianguloRectangulo(abscisas[16]-abscisas[15],detalles[16][0])
    arD = areaTrianguloRectangulo(abscisas[17]-abscisas[16],detalles[17][0])
    ar15 = areaTrianguloRectangulo(abscisas[18]-abscisas[17],detalles[18][0])
    ar16 = areaTrianguloRectangulo(abscisas[19]-abscisas[18],detalles[19][0])
    ar17 = areaTrianguloRectangulo(abscisas[20]-abscisas[19],detalles[19][0])
    arE = areaTrianguloRectangulo(abscisas[21]-abscisas[20],detalles[21][0])
    ar18 = areaTrianguloRectangulo(abscisas[22]-abscisas[21],detalles[21][0])
    ar19 = areaTrianguloRectangulo(abscisas[23]-abscisas[22],detalles[22][0])
    ar20 = areaTrianguloRectangulo(abscisas[24]-abscisas[23],detalles[23][0])
    arA = areaTrianguloRectangulo(abscisas[25]-abscisas[24],detalles[24][0])
    print(arA)
    I = ar2+ar3+ar4+arC+ar11+ar15+ar16+ar17+arE+ar18
    D = ar1+ar5+ar6+arB+ar7+ar8+ar9+ar10+ar12+ar13+ar14+arD
    print("I/D",I,D)
    print(len(detalles))
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
            print(f"{i} D: {round(aDD,3)}, contador {contadorTriang}, {detalle}")
        elif detalles[i][1] == "I":
            aDI+=areaTrianguloRectangulo(abscisas[i+1]-abscisas[i],detalle)
            contadorTriang+=1
            print(f"{i} I: {round(aDI,3)}, contador {contadorTriang}, {detalle}")

    print("aDI y aDD",aDI,aDD)
    print('area de detalle derecha e izquierda',aDetD,aDetI)

    # print('lista de distancias: ',distParcial)
    # print('lista de angulos: ',angInternos)
    # print('inters1: ',inters1)
    # print('perimetro: ',sum(distParcial))
    return f"Area Total del poligono de {vertices} vertices: {round(areaP,3)} {unidad}"
print(calcularAreaPoligono())
