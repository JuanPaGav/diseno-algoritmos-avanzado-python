"""Tres ejemplos de fuerza bruta: búsqueda, par cercano y subarreglo."""

from math import dist


def naive_string_matching(texto, patron):
    """Busca el patrón en todas las posiciones posibles del texto.

    Tiempo: O((n-m+1)m) en el peor caso, donde n=len(texto), m=len(patron).
    Espacio auxiliar: O(1); la lista de resultados ocupa O(k).
    """
    apariciones = []
    # Alinea el patrón con cada segmento del texto que tenga su misma longitud.
    for inicio in range(len(texto) - len(patron) + 1):
        coincide = True
        # Compara los caracteres de esta alineación uno por uno.
        for j in range(len(patron)):
            if texto[inicio + j] != patron[j]:
                coincide = False
                break
        # Si ningún carácter difirió, guarda el inicio de la coincidencia.
        if coincide:
            apariciones.append(inicio)
    return apariciones


def closest_pair(puntos):
    """Encuentra el par de puntos con menor distancia euclidiana.

    Tiempo: O(n^2), porque revisa todos los pares una sola vez.
    Espacio auxiliar: O(1), sin contar el par devuelto.
    """
    if len(puntos) < 2:
        raise ValueError("Se requieren al menos dos puntos")
    mejor_par = None
    mejor_distancia = float("inf")
    # El segundo índice empieza después del primero: no repite pares ni usa (p,p).
    for i in range(len(puntos) - 1):
        for j in range(i + 1, len(puntos)):
            distancia = dist(puntos[i], puntos[j])
            # Conserva solamente la mejor distancia vista hasta ahora.
            if distancia < mejor_distancia:
                mejor_distancia = distancia
                mejor_par = (puntos[i], puntos[j])
    return mejor_par, mejor_distancia


def max_subarray_brute_force(arreglo):
    """Devuelve límites y suma del subarreglo contiguo de suma máxima.

    Tiempo: O(n^2), al enumerar todos los inicios y finales.
    Espacio auxiliar: O(1).
    """
    if not arreglo:
        raise ValueError("El arreglo no puede estar vacío")
    # Inicializar con un elemento funciona también si todos son negativos.
    mejor_suma = arreglo[0]
    mejor_inicio = mejor_fin = 0
    # Fija cada inicio y extiende el subarreglo hacia la derecha.
    for inicio in range(len(arreglo)):
        suma = 0
        for fin in range(inicio, len(arreglo)):
            suma += arreglo[fin]
            # Actualiza suma e índices cuando encuentra un mejor candidato.
            if suma > mejor_suma:
                mejor_suma = suma
                mejor_inicio, mejor_fin = inicio, fin
    return mejor_inicio, mejor_fin, mejor_suma


if __name__ == "__main__":
    print(naive_string_matching("paypaypal", "paypal"))
    print(closest_pair([(0, 0), (3, 4), (1, 1)]))
    print(max_subarray_brute_force([12, 4, -5, 3, 4, -8, 12]))

