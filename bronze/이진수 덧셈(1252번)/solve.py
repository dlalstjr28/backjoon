number1, number2 = list(input().split())
number1 = number1[::-1]
number2 = number2[::-1]
number1_10 = 0
number2_10 = 0 

for i in range(len(number1)):
    number1_10 += int(number1[i])*(2**i)
for i in range(len(number2)):
    number2_10 += int(number2[i])*(2**i)
sum_number = number1_10 + number2_10
result = ""
while True:
    result += str(sum_number % 2)
    sum_number = sum_number //2
    if sum_number == 0 :
        break
print(result[::-1])
