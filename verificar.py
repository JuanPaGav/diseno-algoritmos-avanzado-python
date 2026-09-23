"""Pruebas rápidas sin dependencias externas."""

import importlib.util
from pathlib import Path


def load(filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(filename, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    brute = load("01_fuerza_bruta.py")
    decrease = load("02_decrementa_venceras.py")
    divide = load("03_divide_venceras.py")
    dp = load("04_programacion_dinamica.py")
    backtracking = load("05_backtracking.py")
    bnb = load("06_branch_and_bound.py")
    greedy = load("07_greedy.py")
    lcs = load("08_longest_common_substring.py")
    kmp = load("09_kmp.py")
    z = load("10_z_algorithm.py")
    manacher = load("11_manacher.py")
    suffix = load("12_suffix_array.py")
    trie = load("13_trie.py")
    huffman = load("14_huffman.py")

    assert brute.naive_string_matching("aaaa", "aa") == [0, 1, 2]
    assert decrease.fake_coin([10, 9, 10, 10]) == 1
    assert divide.quicksort([3, 1, 2]) == [1, 2, 3]
    assert dp.coin_change_tabulation([1, 2, 5], 5) == 4
    assert len(backtracking.resolver_n_reinas(4)) == 2
    matrix = [[0, 1, 0], [2, 0, 3], [0, 4, 5]]
    assert bnb.coin_collecting_branch_and_bound(matrix)[0] == 11
    assert greedy.greedy_knapsack([(2, 12), (1, 10)], 2)[2] == 10
    assert lcs.longest_common_substring("ABABC", "BABCA")[:2] == ("BABC", 4)
    assert kmp.kmp_search("paypaypal", "paypal") == [3]
    assert z.z_search("paypaypal", "paypal") == [3]
    assert len(manacher.manacher("babad")) == 3
    assert suffix.suffix_array("banana") == [5, 3, 1, 0, 4, 2]
    assert trie.build_suffix_trie("banana").starts_with("ana")
    assert huffman.encode("aaaa", huffman.huffman_codes("aaaa")) == "0000"
    print("14 módulos verificados correctamente")


if __name__ == "__main__":
    main()

