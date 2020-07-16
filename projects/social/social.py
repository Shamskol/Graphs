import random
from util import Stack, Queue  # These may come in handy

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

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")
        # Generate all friendship combinations
        possible_friendships = [] 
        # Avoid dupes by making sure first number is smaller than second 
        for user_id in self.users:  
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle all possible friendships
        random.shuffle(possible_friendships) 

        # Create for first X pairs x is total // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1]) 
        # * Hint 1: To create N random friendships you should create a
        # list with all possible friendship combinations, shuffle the
        # list, then grab the first n elements from the list. You will
        # need to import random to get shuffle 
        # * Hint 2: add friendship(1, 2) is the same as  
        #  add_friendship(2, 1). You should avoid calling one after
        # the other since it will do nothing but print a warning. You 
        # can avoid this by only creating friendships where user1 < user2 

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        # !!!! IMPLEMENT ME
        
# shortest tells us it is breadth first
# extended network - traversal, connected component

# planning

# how are e going to build a graph? we done did that one

# Start at a given user id, do a bft, return the path to each friend

#create q
        qq = Queue()

# enqueue path
        qq.enqueue([user_id])    
# create visited

        visited = {}  # Note that this is a dictionary, not a set
# while queue not empty
        while qq.size() > 0:
    # dequeue first path
            path = qq.dequeue()

        vertex = path[-1]
    # if not visited
        if vertex not in visited:
        # Do the thing!!
         # add to visited
            visited[vertex] = path
       
        # for each neighbor
            for neighbor in self.friendships[vertex]:
            # copy path and enqueue
                new_path = path.copy()
                new_path.append(neighbor)
                qq.enqueue(new_path)

        return visited
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
