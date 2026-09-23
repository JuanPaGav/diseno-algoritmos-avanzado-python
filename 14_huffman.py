"""Códigos de Huffman: construcción del árbol y codificación."""

import heapq
from collections import Counter
from dataclasses import dataclass, field


@dataclass(order=True)
class HuffmanNode:
    frequency: int
    order: int
    char: str = field(compare=False, default=None)
    left: object = field(compare=False, default=None)
    right: object = field(compare=False, default=None)


def huffman_codes(texto):
    if not texto:
        return {}
    heap = []
    order = 0
    for char, frequency in Counter(texto).items():
        heapq.heappush(heap, HuffmanNode(frequency, order, char))
        order += 1
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(left.frequency + right.frequency, order, None, left, right)
        order += 1
        heapq.heappush(heap, parent)

    codes = {}

    def walk(node, prefix):
        if node.char is not None:
            codes[node.char] = prefix or "0"
            return
        walk(node.left, prefix + "0")
        walk(node.right, prefix + "1")

    walk(heap[0], "")
    return codes


def encode(texto, codes):
    return "".join(codes[char] for char in texto)


if __name__ == "__main__":
    mensaje = "algoritmos"
    codigos = huffman_codes(mensaje)
    print(codigos)
    print(encode(mensaje, codigos))


