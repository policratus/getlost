"""
Graph Structures
"""
class Graph:
    """
    Defines graph data structures
    """
    def __init__(self):
        self.graph = {}

    def neighbours(self, vertex):
        """
        Returns all vertices neighbourhood
        of vertex

        Parameters
        ----------
        vertex: str
            Name of analyzed vertice
        """
        try:
            return list(self.graph[vertex].keys())
        except KeyError:
            print('Vertex %s not found.' % vertex)

    def add(self, vertex, neighbours):
        """
        Add a new vertice (and its neighbours)
        on graph

        Parameters
        ----------
        vertex: str
            Name of the new vertex

        neighbours: dict
            Containing the neighbours and theirs
            weights
        """
        self.graph[vertex] = neighbours

    def weight(self, vertex_a, vertex_b):
        """
        Returns the weight between vertex_a
        and vertex_b
        """
        try:
            return self.graph[vertex_a][vertex_b]
        except KeyError:
            print('Vertex %s not found or has no edge with %s.' % (vertex_a, vertex_b))
