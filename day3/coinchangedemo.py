# Program to implement coin change using dp - tabulation method
def coinChange(amt,coins):
    dp = [amt+1] * (amt+1)    
    dp[0] = 0
    for coin in coins:
        for i in range(coin,amt+1):
            dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[amt] if dp[amt]!=amt+1 else -1      

# main function
amt = int(input())
#number of denominations
n = int(input())
# getting denominations 
denoms = list(map(int, input().split()))
print(coinChange(amt, denoms))
