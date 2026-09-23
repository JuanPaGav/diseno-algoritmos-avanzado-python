"""Knuth-Morris-Pratt: búsqueda usando el arreglo LPS."""


def construir_lps(patron):
    lps = [0] * len(patron)
    longitud = 0
    i = 1
    while i < len(patron):
        if patron[i] == patron[longitud]:
            longitud += 1
            lps[i] = longitud
            i += 1
        elif longitud > 0:
            longitud = lps[longitud - 1]
        else:
            i += 1
    return lps


def kmp_search(texto, patron):
    if patron == "":
        return list(range(len(texto) + 1))
    lps = construir_lps(patron)
    encontrados = []
    i = j = 0
    while i < len(texto):
        if texto[i] == patron[j]:
            i += 1
            j += 1
            if j == len(patron):
                encontrados.append(i - j)
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    return encontrados


if __name__ == "__main__":
    print(construir_lps("paypal"))
    print(kmp_search("paypaypal", "paypal"))


