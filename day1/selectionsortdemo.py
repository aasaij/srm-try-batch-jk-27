n = int(input())
data = list(map(int, input().split()))[:n]
#implementing selection sort algorithm
for i in range(len(data)-1):
    #selecting the least value from the remaining list
    #Assumming ith element is least element
    minIndex = i
    #checking whether least is there in the remaining list than ith element or not
    for j in range(i+1,len(data)):
        if data[minIndex]>data[j]:
            #found least element
            minIndex = j
    #swapping ith element and minIndex element
    if minIndex != i:
        data[minIndex], data[i] = data[i], data[minIndex]
print(data)


# l1 = [34, 5,7 ,34,6,12]
# l1.sort()
# print(l1)


# l1 = [34, 5,7 ,34,6,12]
# l1.sort(reverse=True) #descending order
# print(l1)

# l1 = [34, 5,7 ,34,6,12]
# sorted_list = sorted(l1, reverse=True)
# print(l1)
# print(sorted_list)
