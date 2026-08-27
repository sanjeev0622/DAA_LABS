def knapsack(weights, profit, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                profit[i] + dp[w - weights[i]]
            )
    return dp[capacity]
n = int(input("Enter number of items: "))
weights = []
profit = []
for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    p = int(input(f"Enter profit of item {i + 1}: "))
    weights.append(w)
    profit.append(p)
capacity = int(input("Enter knapsack capacity: "))
result = knapsack(weights, profit, capacity)
print("Maximum profit:", result)
