# arr = [[0] * 10] * 5

# arr[1][0] = 100
# for row in arr:
#     print(id(row))
# arr = [[1,2,3], [4,5,6], [7,8,9], [11,12,14]]
# arr[1][0] = 222
# for row in arr:
#     print(row)

# r = 5
# c = 5
# arr = []
# for i in range(r):
#     cols = []
#     for j in range(c):
#         cols.append(0)
#     arr.append(cols)
# arr[0][0] = 111
# print(arr)

# data = []
# for _ in range(10):
#     data.append(0)

# List comprehension
data = [[1 for _ in range(10)] for _ in range(5)]

data[0][0] = 121
for row in data:
    print(row)
    