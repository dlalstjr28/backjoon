number = int(input())
array = list(map(int,input().split()))
dp = array.copy()
for i in range(number):
    for j in range(i):
        if array[i] > array[j] :
            dp[i] = max(dp[i],dp[j]+array[i])
print(max(dp))

## 복습하자 ! https://cotak.tistory.com/46
