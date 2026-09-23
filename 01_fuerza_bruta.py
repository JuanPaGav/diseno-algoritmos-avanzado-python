"""Fuerza bruta: búsqueda ingenua, par más cercano y subarreglo máximo."""

from math import dist


def naive_string_matching(texto, patron):
    apariciones = []
    for inicio in range(len(texto) - len(patron) + 1):
        coincide = True
        for j in range(len(patron)):
            if texto[inicio + j] != patron[j]:
                coincide = False
                break
        if coincide:
            apariciones.append(inicio)
    return apariciones


def closest_pair(puntos):
    if len(puntos) < 2:
        raise ValueError("Se requieren al menos dos puntos")
    mejor_par = None
    mejor_distancia = float("inf")
    for i in range(len(puntos) - 1):
        for j in range(i + 1, len(puntos)):
            distancia = dist(puntos[i], puntos[j])
            if distancia < mejor_distancia:
                mejor_distancia = distancia
                mejor_par = (puntos[i], puntos[j])
    return mejor_par, mejor_distancia


def max_subarray_brute_force(arreglo):
    if not arreglo:
        raise ValueError("El arreglo no puede estar vacío")
    mejor_suma = arreglo[0]
    mejor_inicio = mejor_fin = 0
    for inicio in range(len(arreglo)):
        suma = 0
        for fin in range(inicio, len(arreglo)):
            suma += arreglo[fin]
            if suma > mejor_suma:
                mejor_suma = suma
                mejor_inicio, mejor_fin = inicio, fin
    return mejor_inicio, mejor_fin, mejor_suma


if __name__ == "__main__":
    print(naive_string_matching("paypaypal", "paypal"))
    print(closest_pair([(0, 0), (3, 4), (1, 1)]))
    print(max_subarray_brute_force([12, 4, -5, 3, 4, -8, 12]))


