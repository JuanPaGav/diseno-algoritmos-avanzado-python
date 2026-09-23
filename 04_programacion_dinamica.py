"""Programación dinámica: cambio de monedas y recolección en matriz."""

from functools import lru_cache


def coin_change_tabulation(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] += dp[value - coin]
    return dp[amount]


def coin_change_memo(coins, amount):
    @lru_cache(maxsize=None)
    def solve(n, remaining):
        if remaining == 0:
            return 1
        if n == 0 or remaining < 0:
            return 0
        return solve(n, remaining - coins[n - 1]) + solve(n - 1, remaining)

    return solve(len(coins), amount)


def coin_collecting(coins):
    rows, columns = len(coins), len(coins[0])
    dp = [[0] * columns for _ in range(rows)]
    dp[0][0] = coins[0][0]
    for column in range(1, columns):
        dp[0][column] = dp[0][column - 1] + coins[0][column]
    for row in range(1, rows):
        dp[row][0] = dp[row - 1][0] + coins[row][0]
    for row in range(1, rows):
        for column in range(1, columns):
            dp[row][column] = coins[row][column] + max(
                dp[row - 1][column], dp[row][column - 1]
            )
    return dp[-1][-1], dp


if __name__ == "__main__":
    print(coin_change_tabulation([1, 2, 5, 10], 10))
    print(coin_change_memo((1, 2, 5, 10), 10))
    print(coin_collecting([[0, 1, 0], [1, 1, 1], [0, 0, 1]])[0])


