'''Grap module.'''
from utils.edge import Edge
from utils.vertice import Vertice
from typing import List

class Graph:

    def __init__(self):
        self.edges = list()
        self.vertices = list()

    def addVertice(self, key: str):
        node = Vertice(key)
        self.vertices.append(node)

    def addEdges(self, src: str, dst_l: List[str]):
        src_node = self.getVertice(src)
        for dst in dst_l:
            dst_node = self.getVertice(dst)
            if not dst_node:
                raise Exception("Trying to add Edges to non-existing vertices")
            edge = Edge(src_node, dst_node)
            self.edges.append(edge)

    def addEdge(self, src: str, dst: str):
        src_node = self.getVertice(src)
        dst_node = self.getVertice(dst)

        if not src_node or not dst_node:
            raise Exception("Trying to add Edges to non-existent veritces")

        edge = Edge(src_node, dst_node)
        self.edges.append(edge)

    def getVertice(self, key: str) -> Vertice:
        for node in self.vertices:
            if node.key == key:
                return node
        return None

    def isVerticeExists(self, key: str) -> bool:
        return False if not self.getVertice(key) else True
