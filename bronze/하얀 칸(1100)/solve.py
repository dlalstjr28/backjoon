chess = [] 
for i in range(8):
    chess.append(list(input()))
flag = 0
count = 0 
for row in chess :
    if flag == 0 :
        for knight in range(len(row)) : 
            if knight % 2 == 0 and row[knight] =="F":
                count +=1
        flag = 1
        continue
    else :
        for knight in range(len(row)) : 
            if knight % 2 == 1 and row[knight] =="F":
                count +=1
        flag = 0
        continue
print(count)
