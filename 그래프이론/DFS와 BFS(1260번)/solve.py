def dfs(graph,start,visited):
    visited[start]= 1
    print(start,end=' ')
    sorted_graph = graph[start].copy()
    sorted_graph.sort()
    for i in sorted_graph:
        if visited[i] == 0 :
            dfs(graph,i,visited)
def bfs(graph,start,bfs_visited):
    queue = [start]
    bfs_visited[start] = 1
    while queue :
        get_vertex = queue.pop(0)
        print(get_vertex,end=' ')
        sorted_graph = graph[get_vertex].copy()
        sorted_graph.sort()
        for i in sorted_graph:
            if bfs_visited[i] == 0 :
                queue.append(i)
                bfs_visited[i] = 1

vertex_number , edge_number, start = map(int,input().split())
graph = [[] for i in range(vertex_number+1)]
for _ in range(edge_number):
    vertex_start , vertex_end = map(int,input().split())
    graph[vertex_start].append(vertex_end)
    graph[vertex_end].append(vertex_start)
visited=[0 for i in range(vertex_number+1)]
bfs_visited=visited.copy()
dfs(graph,start,visited)
print()
bfs(graph,start,bfs_visited)

## 필자는 리스트로 queue를 구현하고자 하기 때문에, deque로 이용하지 않습니다. 
