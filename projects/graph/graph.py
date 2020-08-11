"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #print(starting_vertex)
        # Make a queue
        q = Queue()
        # Enqueue a starting node
        q.enqueue(starting_vertex)
        # Make a set to track if we been there before
        visited = set()                          
        # while our queue is n't empty
        while q.size() > 0:
            ## Dequeue whatever is at the front of our queue,
            ## this is our current_node
            current_node = q.dequeue()
            ## If we hane n't the node yet
            if current_node not in visited:
                ### Mark as visited
                visited.add(current_node)
                ### Get it's neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors
                for neighbor in neighbors:
                    #### add to the queue
                    q.enqueue(neighbor)




    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Make a stack
        s = Stack()
        # Push on our starting node
        s.push(starting_vertex)
        # Make a set to track if we have been there before
        visited = set()
        # while our stack is n't empty
        while s.size() > 0:
            ## pop off whatevr is on top, 
            ## this is our current_node
            current_node = s.pop()
            ## if we have n't visited this vertex before
            if current_node not in visited:
                ### run function / print
                print(current_node)
                ### mark as visited
                visited.add(current_node)
                ### get it's neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors
                for neighbor in neighbors:
                    #### add to the stack
                    s.push(neighbor)


                                                                   

    def dft_recursive(self, starting_vertex, visited =set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # mark this vertex as visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
        ## if it's not visited
            if neighbor not in visited:
        ### recurse on the neighbor 
                self.dft_recursive(neighbor, visited)         
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
    # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
    # Create a Set to store visited vertices
        visited = set()
    # While the queue is not empty...
        while q.size() > 0:
        # Dequeue the first PATH
            current_node = q.dequeue()
        # Grab the last vertex from the PATH
            l = current_node[-1]
        # If that vertex has not been visited...
            if l not in visited: 
            # CHECK IF IT'S THE TARGET
                if l is destination_vertex:
              # IF SO, RETURN PATH
                    return current_node
            # Mark it as visited...
                visited.add(l)    
            # Then add A PATH TO its neighbors to the back of the queue
                for neighbors in self.get_neighbors(l):
              # COPY THE PATH
                    new_path = current_node + [neighbors]
              # APPEND THE NEIGHOR TO THE BACK
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s= Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0 :
            v = s.pop()
            l = v[-1]
            if l not in visited:
                if l is destination_vertex:
                    return v
                visited.add(l)
            for next_v in self.get_neighbors(l):
                new_path = v + [next_v]
                s.push(new_path)
        

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None,visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path =  []
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex is destination_vertex:
            return path
        for x in self.get_neighbors(starting_vertex):
            if x not in visited:
                new_path = self.dfs_recursive(starting_vertex=x, destination_vertex=destination_vertex, path=path, visited=visited)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
