n = int(input())
list = []
for i in range(2,n):
    for num in range(2,i):
        if i % num == 0:
            break
    else:
        list.append(i)
print(len(list))




