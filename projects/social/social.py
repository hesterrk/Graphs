import random

# QUEUE for BFS 
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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    # Have random number of friends, but we need an average number, the average number of friends users has (some may have less some may have more, so we just do an average)
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph as populating this graph from scratch
        # The last_id is in add_user, increments to assign new id to new user
        self.last_id = 0
        # Nodes in grapj
        self.users = {}
        # Edges: connections between the nodes 
        self.friendships = {}

        # FIRST PASS SOLUTION
            # Take all the possible combinations of friendships, shuffle them and use the first x number  


        # 1. Generate all users (We know how many users to create from the number in params) 
        for i in range(0, num_users):
            # Gives us user 0, user 1...
            # Pass in each user number- as name param into add_user method
            # add_user:
                # increments the last_id 
                # assigns the last_id of the user as the key in self.users dict and stores a User object which has one attribute passed in: attrbute is the string 'User' followed by the index assigned in this for loop (i)
            # in this block: i = 0 --> self.add_user('User 0')
            self.add_user(f"User {i}")
            
        # Create friendships in graph: generate all friendship combinations
        # List to store all friendship combinations
        friendship_comb = []

        # Going through our self.users dict, for every user we have created based on num_users (10)
        # user_id in our dict is each user in our dict (10 keys)
        for user_id in self.users:
            # print(self.users[user_id], 'value at each key: user object containing name attribute of user')
            # print(user_id, 'USERID')
            print(self.last_id, 'last id')

            # For each user in our user dict: 
                # Assign the user all friend's in a range
                # e.g if we have 4 users: user_0 will be assigned friends with user 1, user 2, user 3, user 4
                # For user0, we start assigning friends at next user index --> user1 (user0, user1), (user0, user2), (user0, user3), (user, 0, user4)
                # For user1, we start at next user index -> user 2
                # (user1, user2) (user1, user3), (user1, user4)
                # For user2, we start at next user index --> user3
                # (user2, user3), (user2, user4)
                # For user3, we start at next user index --> user4
                # (user3, user4)
                # Explanation:
                # Start at this range to prevent duplicate frienship combo --> dont want duplicate relationship e.g (user0 and user1) and (user1 and user0)
                # as we dont want to be calling add_friendship method twice and passing in duplicate combos
                # Range STOP: is the last user_id (user4) we say plus one as if we dont stop value is not included
            for friend_id in range(user_id + 1, self.last_id + 1):
                # Getting all possible friendships for this user
                    # Add our friendship combo- current user index plus frienduser to our friendship combo list as tuple
                friendship_comb.append((user_id, friend_id))

        # Shuffle friendship combinations in our list 
        random.shuffle(friendship_comb)

        # Now we need to chose the first x friendships out of our friendship_combo list to pass into our add_friendship method
            # this method creates bi-directional connections between user and friend combo
        # The first x number we select from our list is determined by num_users * average_friendship // 2
            # num_users we have is 10, avg. friendship is 2 = 20 friendship combinations
            # We need to divide the number of friendship combinations we have selected by 2 since each add_friendship() call creates 2 friendships (creates bi-directional friendship)


        # This creates how many friendships we take out of our friendship_combo list
        for i in range(num_users * avg_friendships // 2):
            # friendship variable represents the tuple (user, friend) in our friendship_combo list
            friendship = friendship_comb[i]
            # Pull out the 2 elements in our tuple (user, friend) and pass them into add_friendship method
                # the method takes in user_id (our user in tuple) and friend_id (our friend in tuple)
                # friendship_comb[i]'s value is --> ((user, friend))
                # this method creates bi-directional relationship
            self.add_friendship(friendship[0], friendship[1])



    # Second pass Solution:
        # Lays all friendships out, randomly choose friendships
            

    # def populate_graph2(self, num_users, avg_friendships):
    #     """
    #     Takes a number of users and an average number of friendships
    #     as arguments

    #     Creates that number of users and a randomly distributed friendships
    #     between those users.

    #     The number of users must be greater than the average number of friendships.
    #     """
    #     # Reset graph as populating this graph from scratch
    #     # This id is in add_user, increments to assign new id to new user
    #     self.last_id = 0
    #     # Nodes
    #     self.users = {}
    #     # Edges: connections
    #     self.friendships = {}

    #     # Calculates our number of friendships we want to create
    #     target_friendship_num = (num_users * avg_friendships) // 2

    #     # Keep track of total friendships made so far
    #     total_friendships_num = 0

    #     # While we need to make more friendships until we reach the target num!
    #     while total_friendships_num < target_friendship_num:

    #         # Add random friendships, picking people at random
    #         # user_id each time while loop runs we pick a random user based on generating a random integer between between 1 and last user_Id (so from the first user -> last user, every user gets picked but by random each time)
    #         # Between 1 and the total number of users: grab a random user_id
    #         user_id = random.randint(1, self.last_id)
    #         # Grab a random friend_id
    #         # Try and add randomly generated user_id with the randomly generated friend_id
    #         friend_id = random.randint(1, self.last_id)
    #         self.add_friendship(user_id, friend_id)

    #         # Increment our friendship num count
    #         total_friendships_num += 1




    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

    # Plan:
    # shortest --> BFS, use queue structure at top of file
    # BFS: every node we reach we want to keep track of shortest path to that node

        queue = Queue()
        # Visited dictionary
        # key: the current node's id (current user (friend) we are on)
        # value: the path from starting user (user_id in params) to current node (current friend)
        visited = {}

        # Adding our first user node (node contains user_id) to queue 
        queue.enqueue([user_id])

        while queue.size() > 0:
            current_friend_path = queue.dequeue()
            # Get last friend in current friend path
            current_friend_node = current_friend_path[-1]

            # Lookup in our visited dict, if the current friend has already been visited
                # Friend id is key
            if current_friend_node not in visited:
                # Add friend_id which is current_friend node as the key in the visited dict, and assign its value to its current path
                visited[current_friend_node] = current_friend_path
            
            # Go through neighbours aka friends for current user/friend we are on
                # Remember self.friendships is a dict so we need to pass in the current friend node we are on to get all its friends (values in the dict)
            # Until no more neighbours
                for neighbour in self.friendships[current_friend_node]:
                    dup_curr_fr_path = current_friend_path[:]
                    dup_curr_fr_path.append(neighbour)
                    queue.enqueue(dup_curr_fr_path)
            

    #Return visited dict 
    # Dict returns every user in a specified user_id's extended network along with the shortest friendship path between each
        return visited





if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(1000, 5)
    sg.populate_graph(10, 2)
    print(sg.friendships, 'friendships')
    connections = sg.get_all_social_paths(1)
    print(connections, 'connections')

    # Second Q
    # Users in extended network: minus one as dont count yourself
    users_in_ext_net = len(connections) - 1
    # Length of total number of users (1000)
    total_users = len(sg.users)

    # Generated randmly each time so will differ slightly each time
    print(f' percentage: {users_in_ext_net / total_users * 100}')
