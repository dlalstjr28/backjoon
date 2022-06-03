sugar = int(input())
count =0
while sugar >0 :
    if sugar % 5 == 0:
        sugar -=5
        count +=1
        continue
    elif sugar % 3 == 0 :
        sugar -=3
        count+=1
        continue
    else :
        sugar -=5
        count+=1
        continue
if sugar != 0:
    count = -1
print(count)
