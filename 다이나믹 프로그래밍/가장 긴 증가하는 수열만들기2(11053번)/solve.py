N = int(input())
array= list(map(int,input().split()))
result = [1]* N 
for i in range(1,N):
    for j in range(i):
        if array[j] < array[i]:
            result[i] = max(result[i],result[j]+1)
print(max(result))
