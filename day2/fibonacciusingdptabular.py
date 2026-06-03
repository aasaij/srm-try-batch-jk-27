# Program to find nth term of fibonacci series using tabular
def fib(n):
    dp = []
    dp.append(0)
    dp.append(1)
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

# main function
n = int(input())
print(fib(n))