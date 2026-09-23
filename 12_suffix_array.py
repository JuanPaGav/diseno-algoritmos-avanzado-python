"""Suffix Array sencillo mediante ordenamiento de sufijos."""


def suffix_array(texto):
    sufijos = [(texto[i:], i) for i in range(len(texto))]
    sufijos.sort()
    return [indice for _, indice in sufijos]


if __name__ == "__main__":
    print(suffix_array("banana"))


