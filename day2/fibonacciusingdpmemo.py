# Program to find nth term of fibonacci series using memoization
def fib(n, dp):
    if n<= 1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

# main function
n = int(input())
dp = [-1] * (n+1)
print(fib(n,dp))