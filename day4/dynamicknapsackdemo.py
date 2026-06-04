# Program to implement dynamic knapsack problem
def maxiProfits(products, n, size):
    dp = [[0 for _ in range(size+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,size+1):
            if j >= products[i-1][1]:
                dp[i][j] = max(dp[i-1][j],products[i-1][2] + dp[i-1][j - products[i-1][1]])
            else:
                dp[i][j] = dp[i-1][j]
#     for row in dp:
#         print (row)
    return dp[n][days]
        
# main function
# number of days
knapsackSize = int(input())
# number of cities to visit
n = int(input()) 
productsData = []
for _ in range(n):
    data = input().split()
    data[1] = int(data[1])
    data[2]= int(data[2])
    productsData.append(data)
# print (trips)  
print(maxiProfits(productsData, n, knapsackSize))