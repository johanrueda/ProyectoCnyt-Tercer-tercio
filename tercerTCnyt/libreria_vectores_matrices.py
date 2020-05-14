import libreria as c


def sumaVectores(v1,v2):
    """
    Se ingresa cada vector, cada componente del vector es una tupla
    que contiene la parte real y la parte imaginaria, retorna la suma
    de los vectores complejos
    """
    total=[]
    if (len(v1)==len(v2)):
        for i in range(len(v1)):
            total.append(c.suma(v1[i][0],v2[i][0]))
        return(total)
                
    else:
        return ("No son compatibles")
def restaVectores(v1,v2):
    """
    Se ingresa cada vector, cada componente del vector es una tupla
    que contiene la parte real y la parte imaginaria, retorna la resta
    de los vectores complejos
    """
    total=[]
    if (len(v1)==len(v2)):
        for i in range(len(v1)):
            total.append(c.resta(v1[i][0],v2[i][0]))
        return(total)
                
    else:
        return ("No son compatibles")
def inversoAditivo(v1):
    """

    """
    total=[]
    for i in range(len(v1)):
        total.append(c.producto(v1[i][0],[-1,0]))
    return total
def escalarVector(v1,e):
    """
    Se ingresa cada vector, cada componente del vector es una tupla
    que contiene la parte real y la parte imaginaria, retorna
    la multiplicacion del vector por un escalar complejo
    """
    total=[]
    for i in range(len(v1)):
        total.append(c.producto(v1[i][0],e))
    return total

def sumaMatrices(m1,m2):
    """
    Ingresa 2 matrices de tamaño MxN, retorna la suma de las matrices
    """
    total=[]
    if (len(m1)==len(m2)):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                total.append(c.suma(m1[i][j],m2[i][j]))
        
        return total
                
    else:
        return ("No sea marica,debe ser del mismo tamaño")

def inversoAditivoM(m1):
    """
    Ingresa una matriz MxN, retorna el inverso aditivo de la matriz
    """
    total=[]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            total.append(c.producto(m1[i][j],[-1,0]))
    return total

def escalarMatriz(m1,e):
    """"
    Ingresa una matriz MxN y un escalar complejo, retorna la multiplicacion de la
    matriz por un escalar complejo
    """
    total=[]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            total.append(c.producto(m1[i][j],e))
    return total

def transpuesta(m1):
    """
    Ingresa una matriz MxN, y retorna la transpuesta de la matriz.
    """
    total=[[None for i in range(len(m1))]for i in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            total[j][i]=m1[i][j]
    return total
    
def conjugadoM(m1):
    """
    Ingresa una matriz MxN, retorna el conjugado de la matriz.
    """
    total=[]
    fila=[]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            fila.append(c.conjugado(m1[i][j]))
        total.append(fila)
        fila=[]
    return total

def daga(m1):
    """
    Ingresa una matriz MxN, retorna la adjunta de la matriz.
    """
    return transpuesta(conjugadoM(m1))
def productoM(m1,m2):
    """
    Se ingresa cada matriz, cada componente de la matriz es una tupla
    que contiene la parte real y la parte imaginaria, retorna la multiplicacion
    de las matrices complejas
    """
    filas,filas2=len(m1),len(m2)
    columnas,columnas2=len(m1[0]),len(m2[0])
    
    if columnas == filas2:
        total=[[[0,0] for columnas in range(columnas2)]for filas in range(filas)]
        for i in range(filas):
            for j in range(columnas2):
                for k in range(len(m2)):
                    total[i][j]=c.suma(total[i][j],c.producto(m1[i][k],m2[k][j]))
        return total
    else:
        return "No son compatibles"

def generaridentidad(n):
    """
    Ingresa n, como el tamaño de la matriz, y retorna la matriz identidad de tamaño
    n.
    """
    matriz = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append([1,0])
        matriz.append(l)
    return matriz

def accion(m1,m2):
    """
    Ingresa una matriz compleja de tamaño MxN y un vector complejo, y retorna la
    multiplicacion de la matriz por el vector
    """
    return productoM(m1,m2)

def productoInternoV(v1,v2):
    """
    Ingresa 2 vectores complejos, retorna el producto interno de los vectores
    """
    d= daga(v1)
    return productoM(d,v2)
def normaVector(vector):
    """
    Ingresa un vector complejo y retorna la norma del vector
    """
    return (productoInternoV(vector,vector))**0.5

def distanciaEntreVectores(vector1,vector2):
    """
    Se ingresan 2 vectores complejos , retorna la distancia entre estos
    """
    if len(vector1) != len(vector2):
        return 'Los vectores no tienen la misma longitud, su producto interno no esta definido'
    return c.modulo(restaVectores(vector1,vector2))

def esUnitaria(matriz):
    """
    Ingresa una matriz cuadrada MxN, Retorna verdadero  si la matriz es unitaria
    """
    if len(matriz) != len(matriz[0]):
        return 'La matriz no es cuadrada'
    else:
        total= productoM(matriz,daga(matriz))
        ident= identidadM(len(matriz))
        if total == ident:
            return True
        return False
def esHermitiana(matriz):
    """
    Ingresa una matriz cuadrada MxN, Retorna verdadero  si la matriz es hermitiana
    (igual a su propia traspuesta conjugada)
    """
    if len(matriz) != len(matriz[0]):
        return 'La matriz no es cuadrada'
    return matriz == daga(matriz)

def productoTensor(matriz1,matriz2):
    """
    Ingresa una matriz cuadrada MxN,retorna el producto tensor entre estos
    """
    aux = []
    subLista = []
    conta = len(matriz2)
    for i in matriz1:
        valorB = 0
        valorA = 0
        while valorA < conta:
            for num1 in i:
                for num2 in matriz2[valorB]:
                    subLista.append(c.producto(num1,num2))
            aux.append(subLista)
            subLista = []
            valorA +=1
            valorB += 1
    return aux

