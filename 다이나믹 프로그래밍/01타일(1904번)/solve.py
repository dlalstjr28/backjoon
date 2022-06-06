number = int(input())
dp = [0]* 1000001 ## 이거 number 로 입력하면 indexerror 나옴. 문제 조건에 맞춰서 ㄱ
dp[1] = 1
dp[2] = 2
for i in range(3,number+1):
    dp[i] = dp[i-2] + dp[i-1] ## dp[i-2] 는 00타일로 묶인 것들 , dp[i-1] 앞 자리가 1인것들
    dp[i] %= 15746
print(dp[number])
