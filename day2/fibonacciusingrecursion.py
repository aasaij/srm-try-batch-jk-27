# Program to find nth term fibonacci series using recursion
cnt = 0
def fib(n):
    global cnt
    cnt += 1
    #base case
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
print(cnt)