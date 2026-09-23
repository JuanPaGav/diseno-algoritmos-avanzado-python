"""Manacher: palíndromo más largo en tiempo lineal."""


def manacher(cadena):
    texto = "^#" + "#".join(cadena) + "#$"
    radios = [0] * len(texto)
    centro = limite = 0
    for i in range(1, len(texto) - 1):
        espejo = 2 * centro - i
        if i < limite:
            radios[i] = min(limite - i, radios[espejo])
        while texto[i + radios[i] + 1] == texto[i - radios[i] - 1]:
            radios[i] += 1
        if i + radios[i] > limite:
            centro, limite = i, i + radios[i]
    longitud = max(radios, default=0)
    centro_maximo = radios.index(longitud) if radios else 0
    inicio = (centro_maximo - longitud) // 2
    return cadena[inicio : inicio + longitud]


if __name__ == "__main__":
    print(manacher("babad"))


