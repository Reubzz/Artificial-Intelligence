graph = {
    '3':['5','8','25'],
    '5':['1','2'],
    '8':[],
    '25':['12','8'],
    '1':[],
    '2':[],
    '12':['6'],
    '6' :['4','9'],
    '4':[],
    '9':[]
    }

visited = set()
.;'p'[-p
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

dfs(visited,graph,'3')

