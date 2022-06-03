number, sum_penny = map(int,input().split())
listing = []
for _ in range(number):
    listing.append(int(input()))
count = 0
for i in range(len(listing)-1,-1,-1):
    if sum_penny >= listing[i]:
        count += (sum_penny//listing[i])
        sum_penny = sum_penny % listing[i]
    else :
        continue
print(count)
