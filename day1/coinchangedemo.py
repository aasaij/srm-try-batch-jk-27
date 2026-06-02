#Program to implement coin change using greedy approach
amt = int(input())
n = int(input())
coins = list(map(int, input().split()))[:n]
#sorting the denominations in descending order - highest denomination will be first
coins.sort(reverse=True)
if amt >=coins[n-1]:
    coinCnt = 0
    index =0;
    while index < n and amt != 0:
        if amt >= coins[index]:
            coinCnt += amt // coins[index]
            amt %= coins[index]
        index += 1
    print(-1 if amt else coinCnt)
else:
    print("-1")
