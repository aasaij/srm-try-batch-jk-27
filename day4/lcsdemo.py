# Program to find length of longest common substring 
def lcs(s1, s2):
    m,n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j-1]+1 if s1[i-1]==s2[j-1] else 0
#     print (dp)
    return max(max(row) for row in dp)

#main function
s1 = input()
s2 = input()
print(lcs(s1, s2))