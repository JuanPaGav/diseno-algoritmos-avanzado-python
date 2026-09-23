"""Decrementa y vencerás: ordenamiento topológico y moneda falsa."""

from collections import deque


def topological_sort(graph):
    vertices = len(graph)
    indegree = [0] * vertices
    for origen in range(vertices):
        for destino in range(vertices):
            if graph[origen][destino] == 1:
                indegree[destino] += 1

    cola = deque(i for i in range(vertices) if indegree[i] == 0)
    orden = []
    while cola:
        actual = cola.popleft()
        orden.append(actual)
        for vecino in range(vertices):
            if graph[actual][vecino] == 1:
                indegree[vecino] -= 1
                if indegree[vecino] == 0:
                    cola.append(vecino)

    if len(orden) != vertices:
        raise ValueError("El grafo contiene un ciclo")
    return orden


def fake_coin(coins, inicio=0, fin=None):
    """Devuelve el índice de una única moneda más ligera."""
    if fin is None:
        fin = len(coins) - 1
    if inicio == fin:
        return inicio
    cantidad = fin - inicio + 1
    if cantidad <= 3:
        return min(range(inicio, fin + 1), key=coins.__getitem__)

    tamano = cantidad // 3
    fin_1 = inicio + tamano - 1
    inicio_2, fin_2 = fin_1 + 1, fin_1 + tamano
    inicio_3 = fin_2 + 1
    peso_1 = sum(coins[inicio : fin_1 + 1])
    peso_2 = sum(coins[inicio_2 : fin_2 + 1])
    if peso_1 == peso_2:
        return fake_coin(coins, inicio_3, fin)
    if peso_1 < peso_2:
        return fake_coin(coins, inicio, fin_1)
    return fake_coin(coins, inicio_2, fin_2)


if __name__ == "__main__":
    grafo = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    print(topological_sort(grafo))
    print(fake_coin([10, 10, 9, 10, 10]))


