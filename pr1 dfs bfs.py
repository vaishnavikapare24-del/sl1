graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
}

visited = set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)

print("following is the dfs:")
dfs(visited,graph,'A')

#bfs
graph = { 
    'A' : ['B', 'C'],  
    'B' : ['D', 'E'],  
    'C' : ['F'],  
    'D' : [],  
    'E' : ['F'],  
    'F' : [] 
} 
visited = []  
queue = []    

def bfs(visited, graph, node):  
    visited.append(node) 
    queue.append(node)  
    
    while queue:  
        s = queue.pop(0)  
        print(s, end=" ") 

        for neighbour in graph[s]:  
            if neighbour not in visited:  
                visited.append(neighbour)  
                queue.append(neighbour)   

print("following is the bfs:")
bfs(visited, graph, 'A')
