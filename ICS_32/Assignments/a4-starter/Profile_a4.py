# Profile.py
#
# ICS 32
#
# Justin Le
# lej42
# 50644854
import json, time
from pathlib import Path


"""
DsuFileError is a custom exception handler that you should catch in your own code. It
is raised when attempting to load or save Profile objects to file the system.

"""
class DsuFileError(Exception):
    pass

"""
DsuProfileError is a custom exception handler that you should catch in your own code. It
is raised when attempting to deserialize a dsu file to a Profile object.

"""
class DsuProfileError(Exception):
    pass

class Post(dict):
    """ 

    The Post class is responsible for working with individual user posts. It currently 
    supports two features: A timestamp property that is set upon instantiation and 
    when the entry object is set and an entry property that stores the post message.

    """
    def __init__(self, entry:str = None, timestamp:float = 0, recipient:str = None):
        self._timestamp = timestamp
        self.set_entry(entry)
        self.set_recipient(recipient)

        # Subclass dict to expose Post properties for serialization
        # Don't worry about this!
        dict.__init__(self, entry=self._entry, timestamp=self._timestamp, recipient=self._recipient)
    
    def set_entry(self, entry):
        self._entry = entry 
        dict.__setitem__(self, 'entry', entry)

        # If timestamp has not been set, generate a new from time module
        if self._timestamp == 0:
            self._timestamp = time.time()

    def get_entry(self):
        return self._entry
    
    def set_time(self, time:float):
        self._timestamp = time
        dict.__setitem__(self, 'timestamp', time)
    
    def get_time(self):
        return self._timestamp
    
    def get_recipient(self):
        return self._recipient
    
    def set_recipient(self, recipient):
        self._recipient = recipient
        dict.__setitem__(self, 'recipient', recipient)

    """

    The property method is used to support get and set capability for entry and 
    time values. When the value for entry is changed, or set, the timestamp field is 
    updated to the current time.

    """ 
    entry = property(get_entry, set_entry)
    timestamp = property(get_time, set_time)
    recipient = property(get_recipient, set_recipient)

    def update_recipient(self, new_recipient: str) -> None:
        if new_recipient is not None:  # Check if new recipient is not None
            self.recipient = new_recipient

class Message():

    def __init__(self, messages:str = None):
        if messages is None:
            messages = []
        self.set_messages(messages)

    def set_messages(self, messages):
        self._messages = messages
    
    def get_messages(self):
        return self._messages

    messages = property(get_messages, set_messages)

class Friends():

    def __init__(self, friends= None):
        if friends is None:
            friends = []
        self._friends = set(friends)

    def duplicate_friends(self, friends):
        self._friends = set(friends)

    def get_friends(self):
        return self._friends
    
    def set_friends(self, friends):
        self._friends = friends

    friends = property(get_friends, duplicate_friends)

class Profile:
    """
    The Profile class exposes the properties required to join an ICS 32 DSU server. You 
    will need to use this class to manage the information provided by each new user 
    created within your program for a2. Pay close attention to the properties and 
    functions in this class as you will need to make use of each of them in your program.

    When creating your program you will need to collect user input for the properties 
    exposed by this class. A Profile class should ensure that a username and password 
    are set, but contains no conventions to do so. You should make sure that your code 
    verifies that required properties are set.

    """

    def __init__(self, dsuserver=None, username=None, password=None):
        self.dsuserver = dsuserver # REQUIRED
        self.username = username # REQUIRED
        self.password = password # REQUIRED
        self._friends = []         # OPTIONAL
        self._posts = []
        self._messages = []

    def add_post(self, post: Post) -> None:
        self._posts.append(post)

    def del_post(self, index: int) -> bool:
        try:
            del self._posts[index]
            return True
        except IndexError:
            return False
        
    def get_posts(self) -> list[Post]:
        return self._posts

    def add_friend(self, friend: Friends) -> None:
        self._friends.append(friend)

    def get_friends(self) -> list[Friends]:
        return self._friends
    
    def get_messages(self) -> list[Message]:
        return self._messages
    
    def add_message(self, message: Message) -> None:
        self._messages.append(message)

    def save_profile(self, path: str) -> None:
        p = Path(path)
        
        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'w')
                json.dump(self.__dict__, f)
                f.close()
            except Exception as error:
                print("Error: SAVEPROFILE", error)
        else:
            raise DsuFileError("Invalid DSU file path or type")

    def load_profile(self, path: str) -> None:
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                for friend in obj['_friends']:
                    self._friends.append(friend)
                for entry in obj['_posts']:
                    post = Post(entry['entry'], entry['timestamp'])
                    self._posts.append(post)
                for message in obj["_messages"]:
                    self._messages.append(message)
                f.close()
            except Exception as ex:
                raise DsuProfileError(ex)
        else:
            raise DsuFileError()
