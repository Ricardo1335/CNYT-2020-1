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

   
