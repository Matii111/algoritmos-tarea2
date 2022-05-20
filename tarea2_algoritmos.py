def creaLista(lista,cantidadTubos):                                                 #la funcion creaLista, como su nombre lo indica,              
    contador = cantidadTubos                                                        #recibe dos parametros : el nombre de una  lista 
    contador_i=0                                                                    #y   la   cantidad  de tubos a rellenar, con los 
    while(contador>0):                                                              #cuales    genera    una    de  listas que seran
        lista.append([contador_i])                                                  #escenciales  para    resolver    el    problema
        contador-=1
        contador_i+=1
    return lista

def lanzarComida(listaTubos,lanzamientoDesde,lanzamientoHasta):                     #la   funcion lanzarComida introduce :"*" dentro 
        for i in listaTubos:                                                        #de la  lista  creada  con  la  funcion anterior 
            for j in i :                                                            #las   cuales   representan   a la comida de las 
                if (j != "*"):                                                      #gallinas              del              problema
                    if (j >= lanzamientoDesde and j <= lanzamientoHasta):
                        i.append("*") 
        return listaTubos

def resultadoConsultas(lista,consultaDesde,consultaHasta):                          #resultado  consultas  genera  una lista con las
        contadorComida=0                                                            #respuestas   de   las    consultas   realizadas
        for i in listaTubos:                                                        #de  esta  manera  se  pueden separa cada una de
            for j in i :                                                            #las                                   consultas
                if (j=="*" and i[0]>=consultaDesde and i[0]<=consultaHasta):  
                    contadorComida+=1
        listaConsultas.append(contadorComida)
        contadorComida = 0
        return listaConsultas

def printConsultas(listaConsultas):                                                 #printConsultas      imprime   en   pantalla los 
    contador=0                                                                      #resultados       de        cada        consulta
    for i in listaConsultas:
        contador+=1
        print("Resultado consulta {}: {}".format(contador,i))

listaConsultas=[]
lista=[]
contador_ii=0
contador_iii=0

cantidadTubos = int(input("Ingresar la cantidad de tubos: "))
listaTubos = creaLista(lista,cantidadTubos)
cantidadLanzamientos = int(input("Cantidad de lanzamientos: "))

while (contador_ii<cantidadLanzamientos):                                          
    print("Ingresar los rangos de lanzamiento {}: ".format(contador_ii+1))         
    lanzamientoDesde = int(input("Desde:  "))                                      
    lanzamientoHasta = int(input("Hasta:  "))                                       
    if(lanzamientoDesde<=lanzamientoHasta and lanzamientoHasta<=cantidadTubos):
        lanzarComida(listaTubos,lanzamientoDesde,lanzamientoHasta)
        contador_ii+=1
    else: 
        print("Rango de lanzamiento invalido, volver a intentar") 

                                                                                       
cantidadConsultas = int(input("Cantidad de consultas: "))                             

while(contador_iii<cantidadConsultas):                                                 
    print("Ingresar los rangos de la consulta {}: ".format(contador_iii+1))
    consultaDesde = int(input("Desde: "))
    consultaHasta = int(input("Hasta: "))
    if(consultaDesde<=consultaHasta):                                                
        contador_iii+=1
        resultadoConsultas(lista,consultaDesde,consultaHasta)
    else:
        print("Rango de consulta invalido, volver a intentar")                                                                                    
printConsultas(listaConsultas)
   
    
    
