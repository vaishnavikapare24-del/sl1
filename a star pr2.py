graph = {
    'S': {'B': 4, 'C': 3},
    'B': {'F': 5, 'E': 12},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {},
    'G': {}
}

heuristic = {
    'S': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 7,
    'G': 0
}

# Function to calculate f(n) = g(n) + h(n)
def f_cost(item):
    node = item[0]
    g = item[2]
    h = heuristic[node]
    return g + h

def a_star_search(start, goal):
    open_list = [(start, [start], 0)]  # (node, path_so_far, g_score)
    closed_set = set()

    while open_list:
        open_list.sort(key=f_cost)  # Sort by f(n)
        current_node, path, g_score = open_list.pop(0)

        if current_node == goal:
            print("Path found:", ' -> '.join(path))
            print("Total cost:", g_score)
            return

        closed_set.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_set:
                cost = graph[current_node][neighbor]
                total_cost = g_score + cost
                open_list.append((neighbor, path + [neighbor], total_cost))

    print("No path found.")

# Run the search
a_star_search('S', 'G')

