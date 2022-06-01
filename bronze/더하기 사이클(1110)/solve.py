number = int(input())
count = 0
stop = number
while True:
    a = (number//10) + (number%10)
    a %= 10
    number = (number%10)*10 + a
    count +=1
    if stop == number :
        break
    else :
        continue
print(count)
