from random import randint
from queue import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # Add users
        for i in range(numUsers):
            name = ''
            for i in range(randint(5,9)):
                name = name + alphabet[randint(0, len(alphabet) - 1)]
            self.addUser(name)

        # Create friendships
        for key in self.users:
            for _ in range(randint(0, avgFriendships)):
                new_friend = randint(1, len(self.users)-1)
                if new_friend not in self.friendships[key] and new_friend != key:
                    self.addFriendship(key, new_friend)

        # get average friendships per user
        friendships = 0
        for key, item in self.friendships.items():
            friendships += len(item)
            
        print('average friendships', friendships/len(self.users))


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.put([userID])

        while not q.empty():
            user_path = q.get()
            user = user_path[-1]

            if user not in visited.keys():
                visited[user] = user_path
                for friend in self.friendships[user]:
                    new_path = user_path[::]
                    new_path.append(friend)
                    q.put(new_path)

        # get average degree of separation per user
        degrees = 0
        for key, item in visited.items():
            degrees += len(item)
            
        print('average degree of separation', degrees/len(self.users))

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    # print(connections)
