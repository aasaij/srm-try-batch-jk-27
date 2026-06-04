# Program to find longest increasing subsequence
def lis(n, data):
    dp = [1] * n;
    for i in range(1, n):
        for j in range(i):
            if data[i]>data[j]:
                dp[i] = max(dp[i], 1+dp[j])
    return max(dp)

# main function
n = int(input())
data = list(map(int, input().split()))[:n]
print(lis(n, data))