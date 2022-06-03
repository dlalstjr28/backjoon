number = int(input())
listing = list(map(int,input().split()))
listing.sort()
count = 0 
for i in range(len(listing)):
    for j in range(0,i+1):
        count += listing[j]
print(count)
