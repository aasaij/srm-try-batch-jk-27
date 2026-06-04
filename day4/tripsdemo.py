# Program to implement trip optimization
def tripOptimization(trips, n, days):
    dp = [[0 for _ in range(days+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,days+1):
            if j >= trips[i-1][1]:
                dp[i][j] = max(dp[i-1][j],trips[i-1][2] + dp[i-1][j - trips[i-1][1]])
            else:
                dp[i][j] = dp[i-1][j]
#     for row in dp:
#         print (row)
    return dp[n][days]
        
# main function
# number of days
days = int(input())
# number of cities to visit
n = int(input()) 
trips = []
for _ in range(n):
    trip = input().split()
    trip[1] = int(trip[1])
    trip[2]= int(trip[2])
    trips.append(trip)
# print (trips)  
print(tripOptimization(trips, n, days))
    