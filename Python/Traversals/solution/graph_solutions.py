
def backtracking(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = backtracking(graph, node, end, path)
            if newpath: return newpath

    return None


if __name__ == '__main__':
    graph_dict = {'A': ['B', 'C'],
                  'B': ['C', 'D'],
                  'C': ['D'],
                  'D': ['C'],
                  'E': ['F'],
                  'F': ['C']}
    print(backtracking(graph_dict, 'A', 'D'))

