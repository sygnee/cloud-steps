def astar_search(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}    
    while(open_set):
        n = None
        for q in open_set:
            if n == None or g[q]+heuristic[q]<g[n]+heuristic[n]:
                n = q        
        if n == stop_node or n not in Graph_nodes:
            pass
        else:
            for m, weight in get_neighbours(n) or []:
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                elif m in open_set and g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)       
        if not n:
            print('Path does not exist!')
            return None       
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path:', path)
            return path      
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None
def get_neighbours(node):
    return Graph_nodes.get(node)
Graph_nodes = {}
heuristic = {}
n = int(input("Enter no of edges: "))
for _ in range(n):
    source, dest, weight = input("Enter edge (format: source destination weight): ").split()
    Graph_nodes.setdefault(source, []).append([dest, int(weight)])
    Graph_nodes.setdefault(dest, []).append([source, int(weight)])
print("Enter heuristic values: ")
for key in Graph_nodes:
    heuristic[key] = int(input(f"Node: {key} H: "))
while True:
    source = input("Enter source: ")
    destination = input("Enter destination: ")
    astar_search(source, destination)