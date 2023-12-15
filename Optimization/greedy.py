def planificacion_produccion(demanda, cu, ci, cv, u, m):
    n = len(demanda)
    inventario = 0
    costo_total = 0
    t = 0     
    demanda_uso = list(demanda)                         #Creo una copia de demanda para modificar
    unidades_producidas=[]                              #Creo una lista para guardar las unidades producidas

    for i in range(n):                                  #Itero en toda la lista demanda para hayar las producciones optimas de cada mes
        produccion_maxima = min(u, m)                   # Capacidad de la maquinaria y límite del almacén
        
        if (demanda_uso[i] == 0 and inventario != 0):   #Reviso si la demanda_uso es 0 y el inventario es diferente de 0, este caso es cuando en alguna iteracion se devoro
                                                        #a mas de un mes por lo que debemos realizar la venta teniendo en cuenta demanda que es la lista sin modificar
            inventario -= demanda[i]
            produccion = 0
            demanda[i] = 0

        if (inventario - demanda[i] > 0):               #Reviso si la demanda ya esta en el inventario si esta no hay necesidad de producir nada por lo que ese mes no se generan gastos

            inventario = inventario - demanda[i]
            produccion = 0
            demanda[i] = 0
        else:
            inventario -= demanda[i]
            actual = demanda[i]
            costo_temporal = 0
            w = 0
            if i + 1 < n:                                          #Reviso si demanda i + 1 existe, revisar que no esta fuera de rango
                for i in range(t,n):                               #Para iterar desde la poscicion actual hasta la cantidad de meses 

                    costo_temporal += demanda_uso[i]               #Un contador que va sumando cada mes para luego verificar si pasa o no los condicionales

                    #Reviso que el costo de producir lo actual sea menor al costo de guardar lo tomado, reviso que no supere la produccion maxima, 
                    # ni que excesa la capacidad de las maquinas 
                    if (cu * actual > cv * (costo_temporal - actual) and (costo_temporal - actual) < produccion_maxima and costo_temporal <= u):

                        w = costo_temporal                         #Si se cumple lo anterior acepto el costo_temporal y lo guardo en w
                        demanda_uso[i] = 0                         #En la lista modificable elimino el valor devorado por costo_temporal
                             
                    else: 
                        costo_temporal -= demanda_uso[i]            #En caso de que no se cumpla le resto lo sumado a costo_temporal
                        w                                           #Y recupero w que es la que tiene el valor sin sumar el costo aceptado anterior
                  
            else:  w = demanda_uso[i]                               #Si demanda i + 1 no existe simplemente le mando la demanda actual

            produccion = w                                          #Se le pasa el valor demandado para producir
            inventario += produccion                                #Se agrega lo producido al inventario


        t += 1                                                      #Se aumenta el contador para empezar desde la proxima posicion en la siguiente iteracion
        unidades_producidas.append(produccion)                      #Se crea una lista con la cantidad producida cada mes
            
        if produccion == 0: cia = 0                                 #Se revisa el caso en el que no se produce para que no se sume el cia
        else: cia = ci                                              #En caso de que si se produsca pues cia = ci

        costo_mes = cia + cu * produccion + cv * inventario         #Se hace la operacion para el costo del mes

        costo_total += costo_mes                                    #Un acumulador para el costwe total
    return costo_total,unidades_producidas                          


# Ejemplo de uso
demanda = [2, 4, 1, 6, 3]
ci = 2
cu = 0.8
cv = 0.3
u = 6
m = 5

costo_optimo = planificacion_produccion(demanda, cu, ci, cv, u, m)
print(f"La solución óptima tiene un costo total de ${costo_optimo[0]} USD. {costo_optimo[1]}")
#print(planificacion_produccion([4,2,2,3,5,1], 1, 3, 0.5, 5, 4))
#print(planificacion_produccion([4,5,3,1], 1, 3, 0.5, 8, 7))
#print(planificacion_produccion([5,1,1,4,2,3], 1, 3, 0.5, 7, 6))

#ci + cu * produccion + cv * inventario
#La solución óptima tiene un costo total de $20.0 USD. [1, 5, 0, 4]
#(33.0, [4, 4, 0, 3, 5, 1])
#(23.5, [4, 8, 0, 1])
#(27.5, [7, 0, 0, 6, 0, 3])