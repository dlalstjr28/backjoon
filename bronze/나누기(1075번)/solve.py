number = int(input())
divisor = int(input())
result = 0 
for i in range(0,100):
    number = str(number)[0:-2]
    plus = ""
    if i<10 :
        plus = "0"+str(i)
        number= number + plus
    else :
        plus = str(i)
        number += plus
    if int(number)%divisor == 0 :
        result = plus
        break
print(result)
