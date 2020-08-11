'''Edge of the graph.'''

class Edge:

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

        src.addEdge(self)

    def getDestination(self):
        return self.dst

