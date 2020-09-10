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
        else:
            raise IndexError("That vertex does not exist!")

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
        # Create an empty Queue
        q = Queue()
        # Create a set to store the visited nodes
        visited = set()
        # Initialize : enqueue the starting node
        q.enqueue(starting_vertex)
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # if it's not been visited
            if v  not in visited:
                # Mark as visited i. e. add to visited set
                print(f"Visited {v}")
                visited.add(v)
                # Do something with the node
                
                # Add all neighbors in the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack to hold nodes to visit
        to_visit = Stack()
        # Create a set to hold visited nodes
        visited = set()
        # Initialize: add the staring node to the stack
        to_visit.push(starting_vertex)
        # while stack not empty:
        while  to_visit.size() > 0:
            # pop off the top of the stack
            v = to_visit.pop()
            #check  if not  in  visited
            if v not in visited:
                # Visit the node(print it out)
               # print(v)

                # Add it to the visited set
                visited.add(v)
                # enqueue all the neighbors
                for n in self.get_neighbors(v):
                    print(f"Adding: {n}")
                    to_visit.push(n)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
       
        # mark this as visited
        if visited == None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
        
        
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
        ## if it's not visited
            if neighbor not in visited:
        ### recurse on the neighbor
                self.dft_recursive(neighbor, visited)        
        #return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
       
        # Create a Set to store visited vertices
        visited = set() 
        path = [starting_vertex]
        q.enqueue(path)
        
        # While the queue is not empty...
        while q.size() > 0:
           
        
        # Dequeue the first PATH
            current_path = q.dequeue()
        # Grab the last vertex from the PATH
            current_node = current_path[-1] 
        #if this node is our target node
            if current_node == destination_vertex:
                ### return it !! return true
                return current_path

        # If that vertex has not been visited...
            if current_node not in visited:
                ## mark as visited
                visited.add(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each neighbor
                for neighbor in neighbors:
                    ## copy path so we don't mutate the original path to different nodes
                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                    ### add to our queue
                    q.enqueue(path_copy)                
           
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack to hold nodes to visit
        stack = Stack()
        # Create a set to hold visited nodes
        visited = set()
        # Initialize: add the staring node to the stack
        path = [starting_vertex]
        stack.push(path)
        # while stack not empty:
        while  stack.size() > 0:
            # pop off first entry
            current_path = stack.pop()

            current_vertex = current_path[-1]
            # if not visited
            
            if current_vertex == destination_vertex:
                return current_path
                # Visit the node(print it out)
                #print(current)
            if current_vertex not in visited:
                # Add it to the visited set
                visited.add(current_vertex)
                # enqueue all the neighbors
                for n in self.get_neighbors(current_vertex):
                    print(f"Adding: {n}")
                    stack.push(current_path + [n])

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
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
