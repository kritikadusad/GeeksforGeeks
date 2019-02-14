""" Given a directed graph, check whether the graph 
contains a cycle or not. Your function should return 
true if the given graph contains at least one cycle, 
else return false. For example, the following graph 
contains three cycles 0->2->0, 0->1->2->0 and 3->3, 
so your function must return true.
   Input: source vertex = 0 and destination vertex is = 7.
   Output: Shortest path length is:2
           Path is::
           0 3 7

   Input: source vertex is = 2 and destination vertex is = 6.
   Output: Shortest path length is:5
           Path is::
           2 1 0 3 4 6

# Making nodes:
>>> g_node_0 = Node(0)
>>> g_node_1 = Node(1)
>>> g_node_2 = Node(2)
>>> g_node_3 = Node(3)

>>> f_node_0 = Node(0)
>>> f_node_1 = Node(1)
>>> f_node_2 = Node(2)
>>> f_node_3 = Node(3)
>>> f_node_4 = Node(4)


# Making the graph and adding nodes:
>>> g = Graph()
>>> f = Graph()

>>> g.add_node(g_node_0)
>>> g.add_node(g_node_1)
>>> g.add_node(g_node_2)
>>> g.add_node(g_node_3)

>>> f.add_node(f_node_0)
>>> f.add_node(f_node_1)
>>> f.add_node(f_node_2)
>>> f.add_node(f_node_3)
>>> f.add_node(f_node_4)




# Setting adjacent nodes:

>>> g.set_adjacent(g_node_0, g_node_2)
>>> g.set_adjacent(g_node_1, g_node_2)
>>> g.set_adjacent(g_node_2, g_node_0)
>>> g.set_adjacent(g_node_0, g_node_1)
>>> g.set_adjacent(g_node_2, g_node_3)
>>> g.set_adjacent(g_node_3, g_node_3)

>>> f.set_adjacent(f_node_0, f_node_1)
>>> f.set_adjacent(f_node_2, f_node_0)
>>> f.set_adjacent(f_node_2, f_node_3)
>>> f.set_adjacent(f_node_4, f_node_3)



# Tests:

>>> is_cyclic(g)
True
>>> is_cyclic(f)
False

"""


class Node:
    """ A node in a graph."""

    def __init__(self, data, adjacent=None):

        if adjacent is None:
            adjacent = set()

        self.data = data
        self.adjacent = adjacent

    def __repr__(self):
        return f"<Node- {self.data}"


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
        """Set edge from node1 to node2."""

        node1.adjacent.add(node2)


def is_cyclic(graph):
    """ Returns true if directed graph contains a cycle."""

    all_nodes = graph.nodes
    graph_nodes = set(all_nodes)
    adjacents = set()
    for node in all_nodes:
        for adjacent in node.adjacent:
            adjacents.add(adjacent)
    if len(graph_nodes - adjacents) > 0:
        return False
    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
