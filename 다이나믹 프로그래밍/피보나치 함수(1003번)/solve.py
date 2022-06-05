number = int(input())
for _ in range(number) :
    count = int(input())
    fibo_zero = [0] * 41
    fibo_one = [0] * 41
    fibo_zero[0] = 1
    fibo_one[1] = 1
    if count == 0 :
        print("{} {}".format(fibo_zero[0],fibo_one[0]))
    elif count == 1 :
        print("{} {}".format(fibo_zero[1],fibo_one[1]))
    else :
        for i in range(2,count+1) :
            fibo_zero[i]= fibo_zero[i-1]+fibo_zero[i-2]
            fibo_one[i] = fibo_one[i-1]+fibo_one[i-2]
        print("{} {}".format(fibo_zero[count],fibo_one[count]))
