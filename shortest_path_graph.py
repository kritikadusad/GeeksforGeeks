""" Given a unweighted graph, a source and a destination,
    we need to find shortest path from source to destination 
    in the graph in most optimal way.
   Input: source vertex = 0 and destination vertex is = 7.
   Output: Shortest path length is:2
           Path is::
           0 3 7

   Input: source vertex is = 2 and destination vertex is = 6.
   Output: Shortest path length is:5
           Path is::
           2 1 0 3 4 6

# Making nodes:
>>> node_0 = Node(0)
>>> node_1 = Node(1)
>>> node_2 = Node(2)
>>> node_3 = Node(3)
>>> node_4 = Node(4)
>>> node_5 = Node(5)
>>> node_6 = Node(6)
>>> node_7 = Node(7)

# Making the graph and adding nodes:
>>> g = Graph()
>>> g.add_node(node_0)
>>> g.add_node(node_1)
>>> g.add_node(node_2)
>>> g.add_node(node_3)
>>> g.add_node(node_4)
>>> g.add_node(node_5)
>>> g.add_node(node_6)

# Setting adjacent nodes:

>>> g.set_adjacent(node_0, node_1)
>>> g.set_adjacent(node_1, node_2)
>>> g.set_adjacent(node_0, node_3)
>>> g.set_adjacent(node_3, node_7)
>>> g.set_adjacent(node_3, node_4)
>>> g.set_adjacent(node_7, node_4)
>>> g.set_adjacent(node_7, node_6)
>>> g.set_adjacent(node_4, node_6)
>>> g.set_adjacent(node_5, node_6)


# Example 1:
>>> g.shortest_distance(node_0, node_7)
2
>>> g.shortest_distance(node_2, node_6)
5
    """


class Node:
    """ A node in a graph."""

    def __init__(self, data, adjacent=None):

        if adjacent is None:
            adjacent = set()

        self.data = data
        self.adjacent = adjacent

    def __repr__(self):
        return f"<Node- {self.data} and adjacent nodes: %s" % [n.data for n in self.adjacent]


class Graph:

    def __init__(self):
        """ Create empty graph."""

        self.nodes = set()

    def __repr__(self):
        """Representation of graph."""
        return "<Graph: %s>" % [node.data for node in self.nodes]

    def add_node(self, node):
        """ Add a node to the graph."""

        self.nodes.add(node)

    def set_adjacent(self, node1, node2):
        """Set two nodes adjacent to each other."""

        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def shortest_distance(self, source, destination):
        to_visit = [source]
        visited = set()
        current = source
        distances = []
        distance = 1
        while to_visit:

            visited.add(current)
            to_visit.pop(0)

            if destination not in current.adjacent:
                for node in current.adjacent:
                    if node not in visited:
                        to_visit.append(node)
                distance += 1
            else:
                return distance
            current = to_visit[0]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")


# # Making nodes:
# node_0 = Node(0)
# node_1 = Node(1)
# node_2 = Node(2)
# node_3 = Node(3)
# node_4 = Node(4)
# node_5 = Node(5)
# node_6 = Node(6)
# node_7 = Node(7)

# # Making the graph and adding nodes:
# g = Graph()
# g.add_node(node_0)
# g.add_node(node_1)
# g.add_node(node_2)
# g.add_node(node_3)
# g.add_node(node_4)
# g.add_node(node_5)
# g.add_node(node_6)
# g.add_node(node_7)

# # Setting adjacent nodes:

# g.set_adjacent(node_0, node_1)
# g.set_adjacent(node_1, node_2)
# g.set_adjacent(node_0, node_3)
# g.set_adjacent(node_3, node_7)
# g.set_adjacent(node_3, node_4)
# g.set_adjacent(node_7, node_4)
# g.set_adjacent(node_7, node_6)
# g.set_adjacent(node_4, node_6)
# g.set_adjacent(node_5, node_6)
