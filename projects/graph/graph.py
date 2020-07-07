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
        # Adding new key to vertices dictionary
        # Set its value to empty set (no edges currently)
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if they are both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            # Add the connection from v1 to v2
            # Adding v2 to v1's set of edges
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex does not exist in this graph")

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
        # Instantiating a new queue object
        queue = Queue()
        # Creating a visited list, so we know if each current node we are on is visited or not
        visited_list = []

        # 1. Adding our starting node to the front of the queue
        queue.enqueue(starting_vertex)

        # While the queue is not empty: using size() method on queue class
        while queue.size() > 0:
            # Hold reference to current starting node (first time round)
            # Remove the starting node from the queue
            current_node = queue.dequeue()

            # If our current node is not visited --> add it to visited list
            if current_node not in visited_list:
                visited_list.append(current_node)
            # Print out each node we visit
                print(current_node)

            # For all of the neighbours of the starting node (or head node of the queue)
                for neighbour in self.get_neighbors(current_node):
                    # If the neighbours of the current node are unvisited
                    if neighbour not in visited_list:
                        # Place neighbours in the queue
                        queue.enqueue(neighbour)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Instiating stack object from the class
        stack = Stack()
        # Add a visited list so we know which nodes we have visited
        visited_list = []

        # 1. Adding our starting node to the stack (last in first out)
        stack.push(starting_vertex)

        # While the stack is not empty: using size() method on stack class
        while stack.size() > 0:
            # Hold reference to current starting node (first time round)
            # Remove the starting node from the top of the stack (last in)
            current_node = stack.pop()

            # Add the current node to visited list if its not visited
            if current_node not in visited_list:
                visited_list.append(current_node)
                # Print out each node we visit
                print(current_node)

                # For all of the neighbours of the starting node (or the last node in the stack)
                for neighbour in self.get_neighbors(current_node):
                    # If the neighbours of the current node are unvisited
                    if neighbour not in visited_list:
                        # Place neighbours in onto the stack
                        stack.push(neighbour)

    # Set visited_nodes to none by default at the start, this will change as this func gets called again repeatedly

    def dft_recursive(self, starting_vertex, visited_nodes=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Starting case where visited_nodes is none:
        if visited_nodes is None:
            # Make this variable point to a list where we will hold our visited nodes
            visited_nodes = []

        # Put our starting node (first time, other times: current node) in the list
        visited_nodes.append(starting_vertex)
        print(starting_vertex)

        # Loop through node's neighbours, check they are unvisited
        # Rec. will end when we reach the end of for loop 
        for neighbour in self.get_neighbors(starting_vertex):
            if neighbour not in visited_nodes:
                # Pass down each neighbour into the func call (one at a time) alongside our list of visited nodes so we know which nodes have been visited when we go into this function again
                self.dft_recursive(neighbour, visited_nodes)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Context: we want to get the shortest path:
            # For the current starting node, note the path, which is just the current node. When we move to one of its adjacent neighbours(one distance away) we note the path we have travelled from starting node to this node, then do the same with the starting node's other neighbour (if it had 2 adjacent neighbours)
            # Then check the nodes that are two distances away from starting node, which is the node's neighbours neighbours
            # Constantly keep track of the path from start -> that current node we are on
            # As we are exploring, make a list of paths travlled so far
            # Alternative is keeping track of parent node, for each node as we work our way to find destination node and then when find, work back to show path, using parent node that we have kept reference too

        
        # 1. Instantiate queue class
        queue = Queue()

        # 2. Keep track of nodes we have visited with visited list
        visited_list = []

        # 3. Add our starting node to our queue in a LIST: we want to keep track of its path, so need list format
        queue.enqueue([starting_vertex])

        # While the queue is not empty
        while queue.size() > 0:
        # Dequeue the first node path in the queue 
        # First time around is just our starting node in a list
            current_node_path = queue.dequeue()
        
        # Getting the last node in our current node list(which we just dequeed): first time is just our starting node ([-1] index)
            # Use the index, as we are getting out the last node in the path list 
            # Second time around this will be one of our starting node's neighbours depending on which neighbour we enqueued into the list first 
            current_node = current_node_path[-1]

        # Check if the current node we are on (the last node from dequeed list) has not been visited
            if current_node not in visited_list:
        #  check if it is equal to destination node
                if current_node == destination_vertex:
                # If it is, return the path we just dequeued (return the list containing all the nodes in the list 
                 # This return thus gives us the route to get to the destination node)
                    return current_node_path
                else:
            # If it is not destination node, mark it as visited by adding it to visited list
                    visited_list.append(current_node)

            # For loop to loop over each of the neighbours of the last node we pulled out of the dequeed list:
            for neighbour in self.get_neighbors(current_node):
            # For each neighbour make a duplicate copy of the dequeed list (as we need it for adding the neighbour node into this copy) can use slicing
                dup_curr_node_path = current_node_path[:]
                # For each neighbour, add the neighbour into to the copied path
                dup_curr_node_path.append(neighbour)
        # Enqueue the dupicate  list  
            # list is the same as the dequed list we did above, but is a copy and also contains the new neighbour node)
                queue.enqueue(dup_curr_node_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Similar to BFS, but using a Stack as structure

        # Instantiate a new stack object from stack class
        stack = Stack()
        # Visited list to keep track of nodes we have already visited
        visited_list = []

        # Place our starting node into a list, and push it to the stack 
        stack.push([starting_vertex])

        # While our stack is not empty:
        while stack.size() > 0:
            # Pop off the top of the stack
            # First time: will be the list containing our starting node
            # Save reference to it as our current_node_path incase we reach our destination node 
            current_node_path = stack.pop()

            # Get current node, by selecting the last node in the current_path_node list
            current_node = current_node_path[-1]

            # If the current node is unvisited:
            if current_node not in visited_list:
                # If the current node is equal to destination node then return the current node's path (path from the starting node to get to destination node)
                if current_node == destination_vertex:
                    return current_node_path
                
                # If not add it to the visited list 
                else:
                    visited_list.append(current_node)

            # For each of the current node's neighbours
            for neighbour in self.get_neighbors(current_node):
                # Make a duplicate copy of our current_node_path
                dup_curr_node_path = current_node_path[:]
                # Add neighbour to this duplicate path copy
                dup_curr_node_path.append(neighbour)
                # Add this duplicate path to the stack 
                stack.push(dup_curr_node_path)




    def dfs_recursive(self, starting_vertex, destination_vertex, visited_nodes=None, current_path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
    
        # Starting case where visited_nodes is none, assign it to an empty list:
        if visited_nodes is None:
            visited_nodes = []

        # Starting case, assign current_path to empty list
        if current_path is None:
            current_path = []


        # Add starting node to current_path list 
        # # Current path gets updated each time, with path to each current node we are on (gets passed into this func) until we find the destination
        current_path = current_path + [starting_vertex]
        
        # Our current element is always going to be our starting_vertex as thats the current node that gets passed in each time this rec. func gets called
        current_node = starting_vertex

        # If this current node has not be visited
        if current_node not in visited_nodes:
            # If its equal to our destination node, return the current node's path
            if current_node == destination_vertex:
                return current_path
                
            else:
            # If not destination node, add current node to the visited list (first time: starting node, other times: current node)
                visited_nodes.append(current_node)
                

        for neighbour in self.get_neighbors(current_node):
            if neighbour not in visited_nodes:
                move_node = self.dfs_recursive(neighbour, destination_vertex, visited_nodes, current_path)
                if move_node:
                    return move_node
            
       




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
