# Understand

# Plan
 ## Graphs problem solving
 ###Translate the problem
 ###Nodes : People
 ### Edges: when a child has a parent

###Build our graph or just define get neighbors
###Choose algorithm
 ### Either BFS or DFS
 #### DFS
 
 # How would we know if DFS happened to be the fastest?
 # import dequeue for collections

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex]
 ## Build a graph like we did to search
 ## But we do n't know when to stop until we have seen everyone      

def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph
def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)
    s = Stack()

    visited = set() 

    s.push([starting_node])
    longest_path = []
    aged_one = -1
    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]
# if path is longer or path is equal but the id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]
        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)
            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    return longest_path[-1]                

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3)) # should print 10
