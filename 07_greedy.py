"""Greedy: mochila 0/1 heurística y recolección local de monedas."""


def greedy_knapsack(objects, capacity):
    ordered = sorted(objects, key=lambda item: item[1] / item[0], reverse=True)
    selected, total_weight, total_value = [], 0, 0
    for weight, value in ordered:
        if total_weight + weight <= capacity:
            selected.append((weight, value))
            total_weight += weight
            total_value += value
    return selected, total_weight, total_value


def greedy_coin_collecting(coins):
    rows, columns = len(coins), len(coins[0])
    row = column = 0
    total = coins[0][0]
    path = [(0, 0)]
    while row < rows - 1 or column < columns - 1:
        if row == rows - 1:
            column += 1
        elif column == columns - 1:
            row += 1
        elif coins[row][column + 1] >= coins[row + 1][column]:
            column += 1
        else:
            row += 1
        total += coins[row][column]
        path.append((row, column))
    return total, path


if __name__ == "__main__":
    print(greedy_knapsack([(2, 12), (1, 10), (3, 20), (2, 15)], 5))
    print(greedy_coin_collecting([[0, 1, 0], [2, 0, 3], [0, 4, 5]]))


