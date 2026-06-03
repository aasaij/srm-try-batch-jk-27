# Program to implement fractional knapsack 
class Product:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.ratio = self.profit / self.weight
    def __str__(self):
        return str(self.profit) + ", " + str(self.weight) + ", " + str(self.ratio)
                 
knapsackSize = int(input())        
n = int(input())
objs = []
for _ in range(n):
    objs.append(Product(*list(map(int,input().split()))))
objs.sort(key=lambda p:p.ratio,reverse=True)
index = 0
maxProfit = 0
while knapsackSize>0 and index < n:
    if objs[index].weight <= knapsackSize:
        maxProfit += objs[index].profit
        knapsackSize -= objs[index].weight
    else:
        maxProfit += objs[index].ratio * knapsackSize;
        knapsackSize = 0
    index += 1

print(maxProfit)
