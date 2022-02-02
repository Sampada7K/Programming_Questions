class Graph:
    def __init__(self, graph_dict=None):
        if not graph_dict:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def neighbours(self, vertex):
        if vertex and vertex in self.graph_dict:
            return self.graph_dict[vertex]

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2:
            if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
                self.graph_dict[vertex1] = vertex2


def depth_first_traversal(graph: Graph, vertex):
    visited = set()

    def dfs_util(graph1: Graph, visited1: set, vertex1):
        if vertex1 not in visited1:
            print(vertex1)
            visited1.add(vertex1)
            for neighbour in graph1.neighbours(vertex1):
                dfs_util(graph1, visited1, neighbour)

    dfs_util(graph, visited, vertex)


def breadth_first_traversal(graph: Graph, vertex):
    q = []
    visited = set()
    if vertex in graph.graph_dict:
        visited.add(vertex)
        q.append(vertex)

    while len(q) != 0:
        vertex1 = q.pop(0)
        print(vertex1)
        for neighbour in graph.neighbours(vertex1):
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)


def route_between_nodes(graph: Graph, node1, node2):
    q = []
    visited = set()
    if node1 in graph.graph_dict:
        visited.add(node1)
        q.append(node1)

    while len(q) != 0:
        vertex1 = q.pop(0)
        print(vertex1)
        if vertex1 == node2:
            return True

        for neighbour in graph.neighbours(vertex1):
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)
    return False


g = {"a": ["d"],
     "b": [],
     "c": ["b", "c", "e"],
     "d": ["a", "c"],
     "e": [],
     "f": []
     }

graph_1 = Graph(g)

print(graph_1.vertices())
# depth_first_traversal(graph_1, "c")
# breadth_first_traversal(graph_1, "a")
print(route_between_nodes(graph_1, "a", "e"))






