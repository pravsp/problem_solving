'''Traversing a Graph using breadth first serach'''
import __init__
__init__.REPO_PATH
from utils.edge import Edge
from utils.vertice import Vertice
from utils.graph import Graph

class BreadthFirstSearch:
    @staticmethod
    def traverse(graph: Graph, start_node: str, dst_node: str) -> list:
        st_vert = graph.getVertice(start_node)
        path = list()
        if not st_vert:
            print("No vertice {} found in graph".format(start_node))
            return path
        path_vert = [st_vert]
        path.append(st_vert.getKey())
        while len(path_vert) > 0:
            current_vert = path_vert.pop(0)
            if current_vert.getKey() == dst_node:
                print("Reached destination")
                return path
            for edge in current_vert.getAllEdges():
                vert = edge.getDestination()
                if vert.getKey() not in path:
                    path_vert.append(vert)
                    path.append(vert.getKey())

        print("No path to destination\nTraversed path:", path)
        return False


def createGraph(graph_nodes: dict) -> Graph:
    graph = Graph()
    for k,_ in graph_nodes.items():
        graph.addVertice(k)

    for k,v in graph_nodes.items():
        graph.addEdges(k, v)

    return graph

if __name__ == '__main__':
    graph_dict = {'A': ['B', 'C'],
                  'B': ['C', 'D'],
                  'C': ['D'],
                  'D': ['C'],
                  'E': ['F'],
                  'F': ['C']}
    graph_dict = {'A': ['B', 'D'],
                  'B': ['A', 'C', 'D'],
                  'C': ['B', 'E'],
                  'D': ['A', 'B', 'E'],
                  'E': ['C', 'D']}
    graph = createGraph(graph_dict)
    src = 'A'
    dst = 'E'
    traversed_path = BreadthFirstSearch.traverse(graph, src, dst)
    print("Path to reach dst {} is {}".format(dst, traversed_path))
