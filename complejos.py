import math
def suma(a,b):
    c = a[0]+b[0],a[1]+b[1]
    return c
def resta(a,b):
    c = a[0]-b[0],a[1]-b[1]
    return(c)
def multiplicacion(a,b):
    c = a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
    return(c)
def division(a,b):
    c = (a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2),(a[1]*b[0]-a[0]*b[1])/(b[0]**2+b[1]**2)
    return(c)
def modulo(a):
    c = (a[0]**2+a[1]**2)**(1/2)
    return(c)
def polares(a):
    c = modulo(a),math.atan(a[1]/a[0])
    return(c)
def conjugada(a):
    c = a[0], -a[1]
    return(c)
def adiciondevectores(a,b):
    c = []
    for i in range (len(a)):
        c.append(suma(a[1],b[1]))
    return c
def inversodevectores(a):
    c = []
    for i in range (len(a)):
        c.append((a[i][0]*(-1),a[i][1]*(-1)))
    return c
def inversodevectores(a):
    c = []
    for i in range (len(a)):
        c.append((a[i][0]*(-1),a[i][1]*(-1)))
    return c
def multiplicacionescalar(a,b):
    c = []
    for i in range (len(a)):
        c.append(multiplicacion(a,b[i]))
    return c
def adiciondematrices(a,b):
    c = []
    for i in range (len(a)):
        c.append([])
        for j in range (len(a)):
            c[i].append(suma(a[i][j],b[i][j]))
    return c
def inversamatrices(a):
    c = []
    for i in range (len(a)):
        c.append(inversodevectores(a[i]))
        
    return c
def multiplicacionescalarmatrices(a,b):
    c = []
    for i in range (len(a)):
        c.append(multiplicacionescalar(a,b[i]))
    return c
def transdematriz(a):
    c = []
    for i in range (len(a)):
        c.append([])
        for j in range (len(a)):
            c[i].append(a[j][i])
    return c
def conjugadamatriz(a):
    c = []
    for i in range (len(a)):
        c.append([])
        for j in range (len(a)):
            c[i].append(conjugada(a[i][j]))
    return c
def adjuntamatriz(a):
    c = conjugadamatriz(transdematriz(a))
    return c
def sumacompvector(a):
    if len(a) < 2 :
        return a[0]
    elif len(a) == 2:
        s = suma(a[0],a[1])
        return s
    else:
        s = suma(a[0],a[1])
        for i in range (2,len(a)):
            s = suma(s,a[i])
        return s
def accion(a,b):
    c = []
    d = []
    for i in range (len(a)):
        c.append([])
        for j in range (len(a)):
            c[i].append(multiplicacion(a[i][j],b[j]))
    print(c)
    for i in range (len(c)):
        d.append(sumacompvector(c[i]))
        
    return d
def main():
    a = [[(4,0),(-1,0)],[(2,0),(1,0)]]
    b =[(1,0),(2,0)]
    print(accion(a,b))
main()
