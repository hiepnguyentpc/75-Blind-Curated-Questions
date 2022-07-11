from queue import Queue

MAX = 100
V = None
E = None
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]

def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1

    q = Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u

def DFS(src):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                path[v] = u

def printPath_Recursive(s,f):
    if s == f:
        print(f, end = ' ')
    else:
        if path[f] == -1:
            print("No path")
        else:
            printPath_Recursive(s,path[f])
            print(f, end=' ')


def printPath_nonRecursive(s,f):
    b = []
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print("No path")
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    for i in range(len(b)-1,-1,-1):
        print(b[i], end=' ')


if __name__ == '__main__':
    V,E = map(int,input().split())
    for i in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 0
    f = 5

    DFS(s)
    BFS(s)
    printPath_Recursive(s,f)