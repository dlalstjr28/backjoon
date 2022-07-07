height , width = map(int,input().split())
graph = [[] for i in range(height)]
for i in range(height):
    string = input()
    for j in string :
        graph[i].append(int(j))
listing = [(0,0)]
step = [(-1,0),(1,0),(0,1),(0,-1)]
while listing :
    q = listing.pop(0)
    for ix in step :
        x,y = q[0]+ix[0] , q[1]+ix[1]
        if (0<= x and x<height) and (0<=y and y<width) :
            if graph[x][y] == 1:
                graph[x][y] = graph[q[0]][q[1]]+1
                listing.append((x,y))
print(graph[height-1][width-1])

## 이 문제는 DFS 로 풀 경우 recursive 갯수 제한에 걸려 X -> BFS로 풀어야함 -> 내 주변에 갈때 큐에 위치 (x,y) 기입 후 한개씩 up
