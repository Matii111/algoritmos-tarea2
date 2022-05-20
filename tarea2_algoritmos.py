#recibe una 'cantidad de tubos' y crea una lista de listas llamada "listaTubos"

listaConsultas=[]
listaTubos=[]
contador_i=0
contador_ii=0
contador_iii=0
contador_iv=0
contadorComida=0

cantidadTubos = int(input("Ingresar la cantidad de tubos: "))

contador=cantidadTubos

while(contador>0):
    listaTubos.append([contador_i])
    contador-=1
    contador_i+=1

#recibe una 'cantidad de lanzamientos' y dos parametros que conforman los 'rangos de lanzamiento' 
#luego comprueba mediante un ciclo while que se cumplan las condiciones: 
# ' 0 <= lanzamiento desde <= lanzamiento hasta <= cantidad de tubos '


cantidadLanzamientos = int(input("Cantidad de lanzamientos: "))

while (contador_ii<cantidadLanzamientos):
    print("Ingresar los rangos de lanzamiento {}: ".format(contador_ii+1))
    lanzamientoDesde = int(input("Desde:  "))
    lanzamientoHasta = int(input("Hasta:  "))
    if(lanzamientoDesde<=lanzamientoHasta and lanzamientoHasta<=cantidadTubos):
        contador_ii+=1
    else: 
        print("Rango de lanzamiento invalido, volver a intentar")
#el siguiente fragmento se encarga de ingresar un '*' entre los rangos de 'lanzamientoDesde' y 'lanzamientoHasta'        
    for i in listaTubos:
        for j in i :
            if j != "*":    
                if j >= lanzamientoDesde and j <= lanzamientoHasta:
                    i.append("*")

#de la misma manera recibe una 'cantidad de consultas' y sus respectivos parametros, luego 
#comprueba las condiciones : ' 0 <= consulta desde <= consulta hasta <= cantidad de consultas'

cantidadConsultas = int(input("Cantidad de consultas: "))
while(contador_iii<cantidadConsultas):
    print("Ingresar los rangos de la consulta {}: ".format(contador_iii+1))
    consultaDesde = int(input("Desde: "))
    consultaHasta = int(input("Hasta: "))
    if(consultaDesde<=consultaHasta):
        contador_iii+=1
    else:
        print("Rango de consulta invalido, volver a intentar")
#en esta seccion se buscan todos los '*' contandolos y separandolos en argumentos dentro de una lista segun la consulta
    for i in listaTubos:        
            for j in i :
                if (j=="*" and i[0]>=consultaDesde and i[0]<=consultaHasta):  
                    contadorComida+=1
    listaConsultas.append(contadorComida)
    contadorComida = 0
#print de los resultados de las consultas 
for i in listaConsultas:
    contador_iv+=1
    print("Resultado consulta {}: {}".format(contador_iv,i))

# print("\n\
#          | | | | | | | |\n\
#          | | | | | | | |\n\
#          |0|1|2|3|4|5|6|")