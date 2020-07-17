from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# FIRST ATTEMPT

# TODO: fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#  # Set up
# # Visited node dict: which keeps track of nodes we have been too
#     # Key is the node, value is nested dictionary
# visited_dict = {}

# # Directions (edges_ with their associated opposite directions
# opposites = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}


# # Nested dict: value for our visited_dict
# # Key is each direction in opposites list
# # Values are all initially '?' as these directions are unexplored
# # direction_to_node_dict = {key: '?' for key in opposites}
# direction_to_node_dict = {}

# # Our current node (room object) - need room object so we can access the methods on Room class! like get_exits later on
# current_node = player.current_room

# # Instantiate stack
# stack = Stack()

# # Add Starting node to stack, plus nested dict
# stack.push((current_node, direction_to_node_dict))


# # While nodes in stack AND we havent finished traversing
# # Finished traversing graph condition: when the length of our visited_dict is same length as room_graph (means we have 0 to 500 node as our keys)
# while stack.size() > 0 and len(visited_dict) < len(room_graph):

#     # Get reference to current node in stack: node number and its nested dict
#     # Dont want to remove it as not all directions are visited yet, so we use peek from func in util on stack class
#     current_node = stack.peek(stack)
#     # print(current_node, 'current node in stack')

#     # Get the room object out of tuple (first element)
#     node_obj = current_node[0]
#     # print(node_obj)
#     # Get nested dict out of tuple (second element)
#     nested_dict = current_node[1]
#     # print(nested_dict, 'huuwibe')

#     # If our current node id (room object) is not a key in our visited_dict (new node we are visiting)
#     # Add the room object's id (tells us node number) as key
#     if node_obj.id not in visited_dict:
#         # if len(nested_dict) == 1:
#         #     for key, value in nested_dict.items():
#         #         direction_to_node_dict[key] = value
#         #         visited_dict[node_obj.id] = direction_to_node_dict
#         if len(nested_dict) == 1:
#             # element being direction
#             direction_to_node_dict[nested_dict] = node_obj.id

#             # Else: havent moved from another node
#         visited_dict[node_obj.id] = direction_to_node_dict
#         # print(visited_dict, 'visited dict')


#     # Get directions we can take for the current node obj we are on using get_exits() method on Room class
#     # returns list of possible directions it can take
#     possible_directions = node_obj.get_exits()
#     # print(possible_directions, 'possible directions for node')
#     # Possible directions returns a list of possible directions so check length of list
#     if len(possible_directions) > 0:
#         # Get a random UNEXPLORED direction from starting node, the player is on
#         # We can use the possible_directions list to randomly select a direction
#         random_direction = random.choice(possible_directions)
#         # print(random_direction, 'random direction selected')
#         # Add each random direction (as while loop runs) to traversal_path list as it expects to be given a list of directions to walk in as we are traversing the graph
#         traversal_path.append(random_direction)
#         # print(traversal_path, 'T list path')


#         # Fill out which node the random direction takes me to, and update visited_dict nested dict with the node assigned to the random direction
#         direction_to_node = node_obj.get_room_in_direction(random_direction)
#         # print(direction_to_node, 'next node')

#         # Update current node's direction in nested dict with this next node it can visit from random direction
#         # visited_dict[node_obj.id[random_direction]] = direction_to_node.id

#         # print(visited_dict[node_obj.id][random_direction], 'WORKING ON THIS ')

#         # Add the next node we got from going in the current node's direction to the stack
#             # We need to set their nested dict's oppsite to the direction that we travelled in (if we travlled north to this node, we need to set their south to current node we are)
#             # Use opposite directions func which returns us the opposite direction for next node
#             # Pass in the random_direction

#         # opp_direction = find_opp_direction(random_direction)
#         # Passing in current node number for func
#         # opp_direction = find_opp_direction(random_direction, node_obj.id)
#         # print(node_obj.id)

#         # Push next node object onto stack alongside dictionary with one key:value which has its directions from its previous node it came from -> both stored in tuple

#         stack.push((direction_to_node, opposites[random_direction]))


#     # BACKTRACK:
#         # The node has to be removed from stack so we can go back to the previous node in the stack, until we can get a direction we can travel too from a node
#     else:
#         stack.pop()
    # Add backed up direction to directions path
#         traversal_path.append(nested_dict)


# SECOND PASS

# TODO: WHAT DO I DO TO THE NODES THAT I VISIT?
# DONT RE-VISIT NODES THAT I HAVE EXPLORED ALL THEIR POSSIBLE DIRECTIONS IN 
# MAKE DIRECTIONS BEEN IN AS VALUE IN VISITED DICT


# Dict to keep track of directions the current node has visits
    # key is current node number (id) that is being explored
    # value is directions that the node has explored (keep track so if we backtrack to the current node, it doesnt go back in the same direction it has already been in), include backtrack directions as values too
visited_dict = {}

# Directions (edges) with their associated opposite directions 
opposites = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# Our current node (room object): need room object so we can access the methods on Room class! like get_exits later on
    # Each node is a room object
current_node = player.current_room

# Instantiate stack, which keeps track of current node object and current opposite direction that brought us to this node (from its prev node) 
    # First node will just be the current node object with current direction as None, as it hasnt come from any other node
stack = Stack()

# Add starting node to stack, plus its direction which is None as it hasnt moved
stack.push((current_node, None))

# While there are tuples in stack AND we havent finished traversing the graph (visited all rooms)
# Finished traversing graph condition: when the length of our visited_dict is same length as room_graph (means we have 0 to 500 node as our keys)
while stack.size() > 0 and len(visited_dict) < len(room_graph):
    # Get reference to current tuple in the stack (last in first out)
    # Dont want to remove it as not all directions are visited yet, so we use peek() method on stack class
    current_node = stack.peek(stack)
    # print(current_node, 'current node in stack')

    # Get the node object out of tuple (first element)
    node_obj = current_node[0]
    # print(node_obj)
    # Get current direction out of tuple (second element)
    curr_direction = current_node[1]
    # print(curr_direction, 'curr direction')
    
    # If the current node number we are on has not been visited, add the current node number as a key to dict (adding roomid)
        # Assign all the value as empty array (which we will append directions too if we encounter this node again)
    if node_obj.id not in visited_dict:
        visited_dict[node_obj.id] = []
        # print(visited_dict)


    # If the current node is visited (key in the visited_dict): means we have backtracked to it
    if node_obj.id in visited_dict:
        # Update this current_node's value in the dict, with the direction it has come from (curr_direction)
        visited_dict[node_obj.id].append(curr_direction)
  
    # Get all possible directions we can take for the current node object --> get_exits() method on Room class --> returns list of possible directions the current node can take can take
    possible_directions = node_obj.get_exits()
    # print(possible_directions, 'possible directions for node')

    # Also need to check if the each of the directions that is returned has already been travelled to by our current_node
        # Find and return a list of any directions that arent already a value in the current node's visited dict
    unvisited_dir = [direction for direction in possible_directions if direction not in visited_dict[node_obj.id]]
    # Whilst there is a unexplored direction the node can take aka unvisited_dir is not empty
    if len(possible_directions) > 0 and len(unvisited_dir) > 0:
        # print(unvisited_dir, 'updated upvisited list')

        # Use unvisited_dir to select a random direction for the current_node to go in
        random_direction = random.choice(unvisited_dir)
        # print(random_direction, 'random direction selected')

        # Add each random direction (as while loop runs) to traversal_path list as it expects to be given a list of directions to walk in as we are traversing the graph

        # Add random direction to TP list (expects list of directions to walk in as we traverse the graph)
        traversal_path.append(random_direction)
        # print(traversal_path, 'TRAVERSAL PATH')

        # Find out which node object the random unexplored direction goes to from current node (next node we will explore)
        direction_to_node = node_obj.get_room_in_direction(random_direction)

        # Update the visited_dict's value (list of directions that the current_node has explored) with the random direction chosen
        visited_dict[node_obj.id].append(random_direction)
        # print(visited_dict)

        
        # Add the next node object (direction_to_node - next node where random direction leads to) to the stack alongside the the opposite direction of the random direction the current node travels in (as it tells us that the node has already explored the node that the direction points to as its just come from there) -> find this using opposites dict (pass random direction in as key and get the value which is the opposite direction)
            # This node in the tuple becomes the next thing the stack explores (last in)
        stack.push((direction_to_node, opposites[random_direction]))


    # There are no more unexplored directions the current_node can take aka unvisited_dir is empty 
    else:
    # (walk back to the nearest room that does contain an unexplored path)
        # As all its possible directions have been travlled too, we remove it from the stack so we can travel back to the current_Node's previous node, until we get to a node that has an unexplored direction
        stack.pop()
        # BACKTRACK time:
        # As we are going back to the previous node (once we pop off current tuple from stack) the last one on stack will become previous node, so we want to tell our TP list of directions that we need to walk back to the direction of previous node (which is our curr_direction) => backtracking direction 
        traversal_path.append(curr_direction)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
