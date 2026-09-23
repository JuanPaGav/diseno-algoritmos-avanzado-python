"""Divide y vencerás: QuickSort y exponenciación rápida."""


def partition(lista, inicio, fin):
    pivote = lista[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1


def quicksort(lista, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    if inicio < fin:
        pivote = partition(lista, inicio, fin)
        quicksort(lista, inicio, pivote - 1)
        quicksort(lista, pivote + 1, fin)
    return lista


def potencia_rapida(base, exponente):
    if exponente < 0:
        return 1 / potencia_rapida(base, -exponente)
    if exponente == 0:
        return 1
    mitad = potencia_rapida(base, exponente // 2)
    if exponente % 2 == 0:
        return mitad * mitad
    return mitad * mitad * base


if __name__ == "__main__":
    print(quicksort([8, 3, 1, 7, 0, 10, 2]))
    print(potencia_rapida(3, 4))


