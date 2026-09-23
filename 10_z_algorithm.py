"""Algoritmo Z para buscar todas las apariciones de un patrón."""


def z_array(cadena):
    z = [0] * len(cadena)
    left = right = 0
    for i in range(1, len(cadena)):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < len(cadena) and cadena[z[i]] == cadena[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z


def z_search(texto, patron):
    if patron == "":
        return list(range(len(texto) + 1))
    combinado = patron + "$" + texto
    z = z_array(combinado)
    return [i - len(patron) - 1 for i, value in enumerate(z) if value == len(patron)]


if __name__ == "__main__":
    print(z_search("paypaypal", "paypal"))


