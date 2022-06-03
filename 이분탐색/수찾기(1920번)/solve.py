def binary_search(listing, find_value):
    start = 0
    end = len(listing)-1
    flag = 0 
    while start <= end :
        mid = (start+end)//2
        if find_value < listing[mid]:
            end = mid - 1
        elif find_value > listing[mid] :
            start = mid + 1
        else :
            flag = 1
            break
    return flag

number = int(input())
input_listing = list(map(int,input().split()))
number_1 = int(input())
find_listing = list(map(int,input().split()))
input_listing.sort()
for find_value in find_listing :
    print(binary_search(input_listing,find_value))
