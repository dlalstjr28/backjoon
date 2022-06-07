number = int(input())
init = [1] * 10
init[0] = 0 
for _ in range(number-1):
    temp = [0] * 10
    for n in range(10):
        if n-1 >= 0 :
            temp[n-1] += init[n]
        if n+1 <= 9 :
            temp[n+1] += init[n]
    init = temp
print(sum(init)%1000000000)

##https://myjamong.tistory.com/312
