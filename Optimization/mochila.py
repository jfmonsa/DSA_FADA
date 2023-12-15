def knapsack(capacidad, pesos, valores, n):
    # Crear una tabla para almacenar los resultados de los subproblemas
    tabla = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]

    # Llenar la tabla utilizando programación dinámica
    for i in range(n + 1):
        for w in range(capacidad + 1):
            if i == 0 or w == 0:
                tabla[i][w] = 0
            elif pesos[i - 1] <= w:
                tabla[i][w] = max(valores[i - 1] + tabla[i - 1][w - pesos[i - 1]], tabla[i - 1][w])
            else:
                tabla[i][w] = tabla[i - 1][w]

    # Construir la solución óptima
    w = capacidad
    items_seleccionados = []
    for i in range(n, 0, -1):
        if tabla[i][w] != tabla[i - 1][w]:
            items_seleccionados.append(i - 1)
            w -= pesos[i - 1]

    return tabla[n][capacidad], items_seleccionados

# Ejemplo de uso
#capacidad_mochila = 10
#pesos = [2, 3, 4, 5]
#valores = [3, 4, 5, 6]
#numero_items = len(pesos)

capacidad_mochila = 8
pesos = [1,2,4,5,7,8]
valores = [2,5,6,10,13,16]
numero_items = len(pesos)

resultado, items_seleccionados = knapsack(capacidad_mochila, pesos, valores, numero_items)

print(f"El valor máximo que se puede obtener es: {resultado}")
print("Seleccionar los siguientes items:")
for item in items_seleccionados:
    print(f"Item {item + 1} - Peso: {pesos[item]}, Valor: {valores[item]}")
