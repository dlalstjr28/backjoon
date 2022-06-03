number , lan_number = map(int,input().split())
all_lan = []
for i in range(number):
    all_lan.append(int(input()))
start = 1
final = max(all_lan)
flag = 0
while(start<=final):
    mid = (start+final)//2
    total = 0
    for lan in all_lan:
        total += (lan//mid)
    if total < lan_number :
        final = mid -1
    else :
        flag = mid
        start = mid +1
print(flag)
