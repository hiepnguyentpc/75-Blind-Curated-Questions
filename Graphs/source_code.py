from queue import Queue

MAX = 100
V = None
E = None
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]

def BFS(s):

    #clean-up: mark all vertices as 'not visited'; mark all paths as 'N/a'
    for i in range(V):
        visited[i] = False
        path[i] = -1

    #initiate a queue, mark root as 'visited', put 'root' into queue
    q = Queue()
    visited[s] = True
    q.put(s)

    #when queue not empty
    while not q.empty():
        #get the next element in queue, treat the element as root
        u = q.get()
        for v in graph[u]:
            #for all adjacent nodes to 'root' u
            #if node not visited
            if not visited[v]:
                #mark node as visited
                visited[v] = True
                #put node into queue
                q.put(v)
                #mark the path u->v
                path[v] = u

def DFS(src):
    #clean up: mark all nodes as 'not visited', mark all paths to 'N/a"
    for i in range(V):
        visited[i] = False
        path[i] = -1

    #initiate a stack, mark the root as visited, append root to stack
    s = []
    visited[src] = True
    s.append(src)

    #while stack is not empty
    while len(s) > 0:
        #pop element from stack
        u = s.pop()
        #get adjacent vertices from stack
        for v in graph[u]:
            #if not visited, perform operatiosn
            if not visited[v]:
                visited[v] = True
                s.append(v)
                path[v] = u


def DFS_recursive(src):
    visited[src] = True
    for v in graph[src]:
        if not visited[v]:
            path[v] = s
            DFS_recursive(v)

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