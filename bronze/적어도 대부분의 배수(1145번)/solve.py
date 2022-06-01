import itertools

listing = list(map(int,input().split()))
test = list(itertools.combinations(listing,3))
result = []
for i in test :
    for j in range(max(i[0],i[1],i[2]),(i[0]*i[1]*i[2])+1) :
        if j % i[0] == 0 and j % i[1] == 0 and j % i[2] == 0 :
                result.append(j)
                break 
        else :
                continue
print(min(result))
