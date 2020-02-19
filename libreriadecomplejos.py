import math

def sumacomplejos(a,b):

    return [a[0]+b[0],a[1]+b[1]]

def restacomplejos(a,b):

    return [a[0]-b[0],a[1]-b[1]]

def multiplicacioncomplejos(a,b):

    r = a[0]*b[0]+((a[1]*b[1])*-1)
    i = a[0]*b[1]+a[1]*b[0]

    return [r,i]

def conjugadocomplejo(a):

  return [a[0],a[1]*(-1)]

def divisioncomplejos(a,b):

    c = conjugadocomplejo(b)
    n = multiplicacioncomplejos(a,c)
    d = multiplicacioncomplejos(b,c)

    return [n[0]/d[0],n[1]/d[0]]

def modulocomplejo(a):

    o = (a[0]**2+a[1]**2)**(1/2)
    
    return o

def faseComplejo(a):

    return math.atan2(a[1],a[0])

def conversionComplejoPolar(a):

    m = modulocomplejo(a)
    f = faseComplejo(a)

    return [m,f]

def conversionPolarComplejo(a):

    r = a[0]*math.cos(a[1])
    i = a[0]*math.sin(a[1])

    return [r,i]


def adicionVectores(a,b):

    if len(a)!=len(b):
        print("Los vectores no pueden ser operados, no son de igual dimension")
    else:
        rta = [[None for fila in range(1)] for column in range(len(a))]

        f = len(a)
        
        for i in range(f):
            rta[i][0] = sumacomplejos(a[i][0],b[i][0])

        return rta

def restaVectores(a,b):

    if len(a)!=len(b):
        print("Los vectores no pueden ser operados, no son de igual dimension")
    else:
        rta = [[None for fila in range(1)] for column in range(len(a))]

        f = len(a)
        
        for i in range(f):
            rta[i][0] = restacomplejos(a[i][0],b[i][0])

        return rta   

def inversoAditivoVectores(a):

        rta = [[None for fila in range(1)] for column in range(len(a))]

        f = len(a)
        
        for i in range(f):
            rta[i][0] = multiplicacioncomplejos(a[i][0],[-1,0])

        return rta 

def multiplicacionEscalarVectores(a,b):

    fila = len(a)

    rta = [[None for column in range(len(a[0]))] for row in range(len(a))]

    for i in range(fila):
        rta[i][0] = multiplicacioncomplejos(a[i][0],b)

    return rta

def adicionMatrices(a,b):

    f = len(a)
    c = len(a[0])
    
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
       print("Los matrices pueden ser operadas, no son de igual dimension")
    else:
        rta = [[None for column in range(c)] for row in range(f)]

        for i in range(f):
            for j in range(c):
                rta[i][j] = sumacomplejos(a[i][j],b[i][j])

        return rta

def inversoAditivoMatrices(a):

    f = len(a)
    c = len(a[0])
    
    for i in range(f):
        for j in range(c):
            a[i][j] = multiplicacioncomplejos(a[i][j],[-1,0])

    return a

def multiplicacionEscalarMatrices(a,b):
    f = len(a)
    c = len(a[0])
    
    rta = [[None for column in range(c)] for row in range(f)]

    for i in range(f):
        for j in range(c):
            rta[i][j] = multiplicacioncomplejos(a[i][j],b)

    return rta

def transpuestaMatrizVector(a):
    f = len(a)
    c = len(a[0])
    
    t = [[None for column in range(f)] for row in range(c)]

    for i in range(f):
        for j in range(c):
            t[j][i] = a[i][j]

    return t

def conjugadoMatrizVector(a):
    f = len(a)
    c = len(a[0])
    
    rta = [[None for j in range(c)] for i in range(f)]

    if c>1:
        for i in range(f):
            for j in range(c):
                rta[i][j] = conjugadocomplejo(a[i][j])

    else:
        for i in range(f):
            rta[i][0] = conjugadocomplejo(a[i][0])

    return rta

def adjuntaMatrizVector(a):

    c = a[:]
    n = conjugadoMatrizVector(c)
    t = transpuestaMatrizVector(n)

    return t

def productoMatriz(a,b):

    fA = len(a)
    fB = len(b)
    cA = len(a[0])
    cB = len(b[0])

    if cA!=fB:
        print("Los matrices pueden ser operadas, no son compatibles")
    else:
        rta = [[[0,0] for columna in range(cB)] for fila in range(fA)]

        for i in range(fA):
            for j in range(cB):
                for k in range(fB):
                    rta[i][j] = sumacomplejos(rta[i][j],multiplicacioncomplejos(a[i][k],b[k][j]))

        return rta

def accionMatrizSobreVector(a,b):

    return productoMatriz(a,b)

def productoInternoVector(a,b):

    n = adjuntaMatrizVector(a)

    return productoMatriz(n,b)

def normaVector(a):
    
    f = len(a)
    c = len(a[0])

    rta = 0

    for i in range(f):
        for j in range(c):
            rta += a[i][j][0]**2+a[i][j][1]**2

    return math.sqrt(rta)

def distanciaVector(a,b):

    r = restaVectores(a,b)

    n = normaVector(r)

    return n

def matrizUnitaria(a):

    d = adjuntaMatrizVector(a)
    o = productoMatriz(a,d)

    f = len(a)
    c = len(a[0])

    matrizIdentidad = [[[1,0] if x==y else [0,0] for y in range(c)] for x in range(f)]

    for i in range(f):
        for j in range(c):
            o[i][j] = [round(o[i][j][0]),round(o[i][j][1])]

    if o==matrizIdentidad:
        return True
    else:
        return False

def matrizHermitiana(a):

    d = adjuntaMatrizVector(a)

    if d==a:
        return True
    else:
        return False

def productoTensorialMatrizVector(a,b):

    f = len(a)*len(b)
    c = len(a[0])*len(b[0])

    nuevaMatriz = [[None for column in range(c)] for row in range(f)]

    m = []
    pos = 0
    col = 0
    f = 0
    c = 0
    cont = 1

    for h in range(len(a)):
        for k in range(len(a[0])):
            m.append(multiplicacionEscalarMatrices(b,a[h][k]))

    for i in range(len(nuevaMatriz)):
        for j in range(len(nuevaMatriz[0])):
            nuevaMatriz[i][j] = m[pos][f][c]

            col += 1
            c += 1

            if col==len(b[0]):
                pos += 1
                c = 0
                col = 0

        if cont==len(b[0]):
            f = 0
            cont = 1
        else:
            cont += 1
            pos -= len(a[0])
            f += 1

    return nuevaMatriz
