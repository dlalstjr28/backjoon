## 이 문제는 정수론으로 접근하면 망함 (25% 정답)
### 간단하게 리스트에 하나하나 곱하면서 가야함
### 정수론으로도 풀수는 있겠지만, 나는 왜 오류가 나는지 모르겠음 (이진수로 지수를 분할해서 계산 속도 상승)

    testcase = int(input())
    for i in range(testcase) :
        number , exp = list(map(int,input().split()))
        idx_2 = exp
        value = ""
        while idx_2 != 0 :
            value += str(idx_2 %2)
            idx_2 = idx_2 // 2
        listing = [number%10]
        result = 1
        for i in range(1,len(value)):
            listing.append((listing[i-1]**2)%10)
        for index in range(len(value)):
            if value[index] == "1" :
                result = (result*listing[index])%10
        if result == 0 :
            print(10)
        print(result)
