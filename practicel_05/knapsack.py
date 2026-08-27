def knapsack(capacity, weights, values, n):
    # Make a 2D table for dynamic programming
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table dp[i][w] in a bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # Max of including the item or excluding it
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage:
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print("Maximum value:", knapsack(W, wt, val, n))
