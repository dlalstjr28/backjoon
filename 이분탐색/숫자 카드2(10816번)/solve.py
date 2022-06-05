import sys
number = input()
listing = list(map(int,sys.stdin.readline().split()))
number1 = input()
find = list(map(int,sys.stdin.readline().split()))
dic = {}
for i in listing:
    if i not in dic:
        dic[i] = 1
    else :
        dic[i] +=1
for find_count in find :
    if dic.get(find_count) is not None :
        print(dic[find_count],end=' ')
    else :
        print(0,end=' ')
## 이문제는 binary Search를 통해서 풀어야 하지만
## count 문제로 나옴으로써 꼬아짐
## 오히려 binary Search를 안써도 풀리는 문제이며, 굳이 binary search를 쓴다면 dict 값을 찾는 용도로는 가능
