# Program to implement Rod cutting or cloth cutting problem
def maximumProfit(n, profits):
    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i] = max(dp[i], profits[j-1]+dp[i-j])
#     print(dp)
    return dp[n]

#main function
n = int(input())
profits = list(map(int, input().split()))
print(maximumProfit(n,profits))