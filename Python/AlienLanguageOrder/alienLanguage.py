'''
Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
'''
from pprint import pformat
class AlienDictGraph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.graph = {}

    def addVertice(self, vertLabel):
        if vertLabel not in self.vertices:
            self.vertices.append(vertLabel)
            self.graph[vertLabel] = list()

    def addEdge(self, src, dst):
        if src in self.graph:
            if dst not in self.graph[src]:
                self.graph[src].append(dst)

    def printGraph(self):
        print(pformat(self.graph, width=1))

    def toposortUtil(self, vert, visited, stack):
        visited.append(vert)
        for neighbour in self.graph[vert]:
            if neighbour not in visited:
                self.toposortUtil(neighbour, visited, stack)
        stack.append(vert)

    def toposort(self):
        stack = list()
        visited = []
        for vert in self.vertices:
            if not vert in visited:
                self.toposortUtil(vert, visited, stack)

        return stack[::-1]

    def constructGraph(self, dict_words):
        for word in dict_words:
            for i in range(len(word)):
                graph.addVertice(word[i])

        for i in range(len(dict_words) -1):
            word1 = dict_words[i]
            word2 = dict_words[i+1]
            for j in range(min([len(word1), len(word2)])):
                if word1[j] != word2[j]:
                    self.addEdge(word1[j], word2[j])
                    break

    def printOrder(self):
        alphabetOrder = self.toposort()
        print(alphabetOrder)

if __name__ == '__main__':
    dict_words = ["caa", "aaa", "aab"]
    dict_words = ["baa", "abcd", "abca", "cab", "cad"]
    print(dict_words)
    graph = AlienDictGraph()
    graph.constructGraph(dict_words)
    graph.printGraph()
    graph.printOrder()

