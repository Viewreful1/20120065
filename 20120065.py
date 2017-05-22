n,m,v=map(int,input().split())
graph={}
def dfs(start):
    s=""
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            s+=str(vertex)+" "
            stack.extend(sorted(list(set(graph[vertex]) - visited),reverse=True))
    print(s)


def bfs(start):
    s=""
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            s+=str(vertex)+" "
            queue.extend(sorted(list(set(graph[vertex]) - visited)))
    print(s)
for _ in range(m):
    a,b=map(int,input().split())
    if a in graph: graph[a].append(b)
    else: graph[a]=[b]
    if b in graph: graph[b].append(a)
    else: graph[b]=[a]
dfs(v)
bfs(v)