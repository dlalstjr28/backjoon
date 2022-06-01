a = int(input())
count = 0
while (count*(count+1))//2 < a :
    count +=1
a -= (count-1)*count //2
total = count +1
if count %2 == 0:
    print("{}/{}".format(a,total-a))
else :
    print("{}/{}".format(total-a,a))
