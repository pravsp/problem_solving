import samplegraph

def dfs(graph, src, visited = []):
    if src not in visited:
        visited.append(src)
        for neighbour in graph[src]:
            dfs(graph, neighbour, visited)


def bfs(graph, src):
    visited = []
    queue = []
    visited.append(src)
    queue.append(src)
    if src not in graph.keys():
        raise Exception("Source node not part of graph")
    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

if __name__ == '__main__':
    graph = samplegraph.graph
    src = 'A'
    print(bfs(graph,src))
    path = []
    dfs(graph, src, path)
    print(path)
