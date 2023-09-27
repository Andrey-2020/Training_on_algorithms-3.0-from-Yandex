def calc_sequence(n) -> int:
    dp = [0]*(n + 2)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


def read_input() -> int:
    n = int(input())
    return n


if __name__ == '__main__':
    print(calc_sequence(read_input()))
