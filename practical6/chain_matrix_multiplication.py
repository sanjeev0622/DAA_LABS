def matrix_chain_order(p, n):

    # dp[i][j] = minimum multiplication cost
    # from matrix i to matrix j
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Length of chain
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


# Example
p = [10, 20, 30, 40]
n = len(p) - 1

result = matrix_chain_order(p, n)

print("Minimum number of multiplications:", result)