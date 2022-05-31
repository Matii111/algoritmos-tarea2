def espacioDominoPD ( n ) :
    if n <= 2:
        return n 
    else :
        lista = [0]*( n + 1)
        lista [1] = 1
        lista [2] = 2
        lista [3] = 3
    i = 4
    while i <= n :
        lista [ i ] =  lista [i-1] + lista [i - 3]
        i = i + 1
    return lista [-2]
i = int(input("ingrese la cantidad de columnas del bloque: "))
print("La cantidad de maneras en la cual se puede rellenar el bloque de 3X1 es de:\n",espacioDominoPD(i))
