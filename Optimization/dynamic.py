def planif_prod(demanda:list[int],cu:float,ci:float,cv:float,max_prod:int,max_inv:int):
    def c(x,cu,ci):
        "Costo de producir"
        if x !=0:
            return x*cu+ci
        else:
            return x*cu

    def f(s,x,mes):
        """
        Funcion recursiva que se encarga de calcular el costo total de una
        etapa dados unos parametros
        """
        #costo del mes actual
        costo_mes = cv*(s+x-demanda[mes-1])+c(x,cu,ci)

        #busco en la tabla si ya existe el valor para no volver a calcularlo
        if matriz_optimos[mes-1][s][0] != float("inf"): 
                return matriz_optimos[mes-1][s][0]
        #caso base
        elif mes == len(demanda):
            return costo_mes
        #caso recursivo
        else:
            s_next = s+x-demanda[mes-1]
            return costo_mes + f(s_next,x,mes+1)

    n=len(demanda)
    
    estados = max(max_inv, max_prod)  
    
    """
    En la matriz_optimos vamos a almacenar tuplas que contienen (fi,xi)
    donde xi es la cantidad más optima que vamos a producir según un estado
    y fi es el costo más optimo para producir según un estado, esto para cada etapa

    Esta matriz la vamos a recorrer al final para dar la solución
    """
    matriz_optimos = [[ [float('inf'),float('inf')] for _ in range(0,estados+1)] for _ in range(1,n+1)]

    
    #recorrer de atras hacia adelante las etapas
    for mes in range(n,0,-1):
        #casos especiales 
        if mes == n: #mes 
            #recorrer para cada posibl1e estado (s) 
            for s in range(0,estados+1):
                
                x4 = demanda[mes-1]-s #cantidad a producir para el mes 
                f4 = f(s,x4,mes)
                
                matriz_optimos[mes-1][s] = [ f4 , x4 ]

            
        #el resto de meses: 
        else:
            for s in range(0,estados+1):
                opt = [float('inf'),float('inf')]
                
                lim_sup = max_prod-abs(demanda[mes-1]-s)-1 if demanda[mes-1]-s <=0 else max_prod
                lim_inf = max(0,demanda[mes-1]-s)
                for x in range(lim_inf,lim_sup+1):

                    fi = f(s,x,mes)

                    #hallar el minimo de lo que se calcule
                    #y guardarlo en la matriz de optimos
                    
                    if fi<opt[0]:
                        opt[0]=fi
                        opt[1]=x

                matriz_optimos[mes-1][s] = opt

    #recorrer la matriz_optimos para presentar la solucion optima
    resultados_producion = []
    
    #(único estado posible, el inventario debe estar vacio en el mes 1)
    costo_total_optimo = matriz_optimos[mes-1][0][0]
    sn=0

    for mes in range(1,n+1):
        #cantidad a producir (desicion) segun el estado optimo del mes actual
        xn=matriz_optimos[mes-1][sn][1]
        
        resultados_producion.append(xn)

        #damanda para el mes actual
        dn=demanda[mes-1]
        
        #estado optimo del siguiente mes (sn+1) según la formula sn+1=sn+xn-dn
        #sn: estado optimo mes actual
        #xn: produccio optima mes actual
        #dn: demanda mes actual
        
        sn=abs(sn+xn-dn)
          
    return resultados_producion , costo_total_optimo

if __name__ == "__main__":
    #ejemplo presentado en el enunciado
    """
    demanda = [1,3,2,4]
    ci = 3
    cu = 1
    cv = 0.5
    max_prod = 5
    max_inv = 4
    """
    demanda = [2, 4, 1, 6, 3]
    ci = 2
    cu = 0.8
    cv = 0.3
    max_inv = 5
    max_prod = 6

    print(planif_prod(demanda,cu,ci, cv, max_prod, max_inv), "...............")
    #print(planif_prod([4,2,2,3,5,1], 1, 3, 0.5, 5, 4))
    #print(planif_prod([4,5,3,1], 1, 3, 0.5, 8, 7))
    #print(planif_prod([5,1,1,4,2,3], 1, 3, 0.5, 7, 6))