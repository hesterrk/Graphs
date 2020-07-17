
# PLAN

# Function params 
# Input data = ancestors (graph): a list of (parent, child) pairs as tuples
# Starting_node = id of node in graph

# What graph traversal --> BFS
# Need to build a graph: intiate a graph object from our graph class
# we want to get the node that is furthest distance from input node, need to keep track of furthest node (last node in the current longest path). If the furthest path has 2 parent nodes, whichever node has smaller numerical value is the furthest node
# Also need to find longest path to get to furthest node, need to keep track of length of each path
# Use queue class for BFS


# Queue class
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# Graph class to create graph instance and add vertices and edges for parent and child nodes
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex does not exist in this graph")
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]



def earliest_ancestor(ancestors, starting_node):

    # Create a new graph object from graph class
    ancestor_graph = Graph()
    # Establish a parent-child relationship using input data (ancestors)
    # Tests use a tuple, list of tuples get passed in as ancestors
    # Parent is at 0th index, child is at 1st index in tuple

    # Go through each element in the tuple (child and parent value)
    for parent_child in ancestors:
        # Add parent and child nodes to graph and connect them using edges

        # Add the tuple first element in tuple as a parent node in graph
        ancestor_graph.add_vertex(parent_child[0])
        # Add the tuple second element in tuple as a child node
        ancestor_graph.add_vertex(parent_child[1])

        # Add connection/edge between the two nodes
            # Want the child node to add its parent node as its connection as child may have many parents
        ancestor_graph.add_edge(parent_child[1], parent_child[0])
        print(parent_child[0], parent_child[1])

    # Instantiate a new queue object from queue class
    queue = Queue()
    visited_list = []

    # Put our starting_node in a path list and push at front of queue
    queue.enqueue([starting_node])
 
    # Create longest_path variable which stores the length of the longest path we encounter as we are traversing 
    # Set to 1 initially as our initial longest path is one as we are on starting node which has length of one
    longest_path = 1

    # Set our furthest_away node value
    # Set initially to -1, incase the starting_node has no parent so this will be by default the furthest away itself, so it will skip the if statement and for loop and just return -1 at end of func
    furthest_node = -1

    # While our queue is not empty:
    while queue.size() > 0:
        # Remove the last path list added to the queue (first one in queue)
        current_node_path = queue.dequeue()
        # print(current_node_path)

        # Get the last node in the current_node_path list
        current_node = current_node_path[-1]
        # If the current node is unvisited:
        if current_node not in visited_list:
        # # Add it to the visited list
            visited_list.append(current_node)
        

        # Two checks needed to change our longest_path and furthest_node variables
        # 1. If the lenght of the current_node_path is longer than the length of the currently stored length in longest path then we need to update
        # 2. Deal with 2 parents scenario: if the child of the longest path has two parents, which both have the path length, we want to assign the furthest_node to the one which has the lowest node value
        if len(current_node_path) > longest_path or len(current_node_path) == longest_path and current_node < furthest_node:
            # Change the length of our longest_path to the length of the curr_node_path as that is now the longest length path so far 
            longest_path = len(current_node_path)
            # Update our furthest_node with the value of the current node as that is now the furthest away node so far 
            furthest_node = current_node

        # Loop through all the neighbours
        for neighbour in ancestor_graph.get_neighbors(current_node):
        # Make duplicate copy of current_node_path, then add neighbour into this path
            dup_curr_node_path = current_node_path[:]
            dup_curr_node_path.append(neighbour)
        # Put this new path into queue
            queue.enqueue(dup_curr_node_path)
        # First path in queue gets removed off queue first, as we go back to while loop

    # Return node furthest away
    print(furthest_node)
    return furthest_node


earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 1)

