#create a dictionary(KEY:VALUE pairs) named as graph to store the nodes in your tree
graph = {
    'S': ['A', 'B'],   #list[] to store the nodes
    'A':['C','D'],
    'B':['G','H'],
    'C':['E','F'],
    'D':[],
    'E':['K'],
    'F':[],
    'G':['I'],
    'H':[],
    'I':[],
    'K':[],
}

visited=[] #List of visited nodes.
queue=[]   #initialization of queue

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m , end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("The Result of Breadth First Search is as follows: ")
bfs(visited,graph,'S')

