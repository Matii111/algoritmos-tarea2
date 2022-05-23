n = 3 #int(input("Ingrese un 'n' para el tamaño del bloque: "))
l = [['0','0','0']]*n
h=0
v=0

for i in l :
    if h<1:
        i[h] = "*"
    h+=1



for i in l:
    for j in i:        
        print(j,end='')
    print("\n")
        

