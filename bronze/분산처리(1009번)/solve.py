testcase = int(input())
for i in range(testcase) :
    number , exp = list(map(int,input().split()))
    result = 1
    for _ in range(exp):
        result = (result*number)%10
    if result == 0 : 
        print(10)
    else :
        print(result)
        
## 백준 컴파일러 절대! pypy3 로 작동!
