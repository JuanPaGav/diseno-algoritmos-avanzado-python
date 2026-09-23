"""Branch and Bound: máximo de monedas moviéndose abajo o a la derecha."""

import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class Nodo:
    prioridad: int
    fila: int = field(compare=False)
    columna: int = field(compare=False)
    valor: int = field(compare=False)
    camino: str = field(compare=False)


def upper_bound(fila, columna, valor, coins):
    rows, columns = len(coins), len(coins[0])
    cota = valor
    for diagonal in range(fila + columna + 1, rows + columns - 1):
        candidatos = []
        for row in range(fila, rows):
            column = diagonal - row
            if columna <= column < columns:
                candidatos.append(coins[row][column])
        if candidatos:
            cota += max(candidatos)
    return cota


def coin_collecting_branch_and_bound(coins):
    rows, columns = len(coins), len(coins[0])
    inicial = coins[0][0]
    cola = [Nodo(-upper_bound(0, 0, inicial, coins), 0, 0, inicial, "")]
    mejor_valor = float("-inf")
    mejor_camino = ""

    while cola:
        nodo = heapq.heappop(cola)
        if -nodo.prioridad <= mejor_valor:
            continue
        if nodo.fila == rows - 1 and nodo.columna == columns - 1:
            if nodo.valor > mejor_valor:
                mejor_valor, mejor_camino = nodo.valor, nodo.camino
            continue
        for df, dc, movimiento in ((1, 0, "D"), (0, 1, "R")):
            fila, columna = nodo.fila + df, nodo.columna + dc
            if fila < rows and columna < columns:
                valor = nodo.valor + coins[fila][columna]
                cota = upper_bound(fila, columna, valor, coins)
                if cota > mejor_valor:
                    heapq.heappush(cola, Nodo(-cota, fila, columna, valor, nodo.camino + movimiento))
    return mejor_valor, mejor_camino


if __name__ == "__main__":
    print(coin_collecting_branch_and_bound([[0, 1, 0], [2, 0, 3], [0, 4, 5]]))


