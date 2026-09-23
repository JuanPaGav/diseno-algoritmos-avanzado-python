"""Backtracking: problema de las N reinas."""


def es_valida(columnas, fila, columna):
    for fila_anterior in range(fila):
        columna_anterior = columnas[fila_anterior]
        if columna_anterior == columna:
            return False
        if abs(fila_anterior - fila) == abs(columna_anterior - columna):
            return False
    return True


def resolver_n_reinas(n):
    soluciones = []
    columnas = [-1] * n

    def colocar(fila):
        if fila == n:
            soluciones.append(columnas.copy())
            return
        for columna in range(n):
            if es_valida(columnas, fila, columna):
                columnas[fila] = columna
                colocar(fila + 1)
                columnas[fila] = -1

    colocar(0)
    return soluciones


def tablero(solucion):
    return [" ".join("R" if solucion[fila] == col else "-" for col in range(len(solucion))) for fila in range(len(solucion))]


if __name__ == "__main__":
    for solucion in resolver_n_reinas(4):
        print(*tablero(solucion), sep="\n")
        print()


