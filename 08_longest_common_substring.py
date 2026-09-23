"""Longest Common Substring con programación dinámica."""


def longest_common_substring(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    mejor = 0
    fin_a = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > mejor:
                    mejor = dp[i][j]
                    fin_a = i
    return a[fin_a - mejor : fin_a], mejor, dp


if __name__ == "__main__":
    print(longest_common_substring("ABABC", "BABCA")[:2])


