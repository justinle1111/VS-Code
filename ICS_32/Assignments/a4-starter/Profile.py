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


class Friends(dict):

    def __init__(self, friends:str = None, messages:str = None):
        self._friends = friends
        self.set_messages(messages)

        # Subclass dict to expose Post properties for serialization
        # Don't worry about this!
        dict.__init__(self, friends=self._friends, messages=self._messages)
    
    def set_messages(self, messages):
        self._messages = messages
        dict.__setitem__(self, 'messages', messages)

    def get_friends(self):
        return self._friends
    
    def set_friends(self, friends: str):
        self._friends = friends
        dict.__setitem__(self, 'friends', friends)

    def get_messages(self):
        return self._messages

    friends = property(get_friends, set_friends)
    messages = property(get_messages, set_messages)
    
    
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

    """

    add_post accepts a Post object as parameter and appends it to the posts list. Posts 
    are stored in a list object in the order they are added. So if multiple Posts objects 
    are created, but added to the Profile in a different order, it is possible for the 
    list to not be sorted by the Post.timestamp property. So take caution as to how you 
    implement your add_post code.

    """

    def add_friend(self, friend: Friends) -> None:
        self._friends.append(friend)

    """
    
    get_posts returns the list object containing all posts that have been added to the 
    Profile object

    """
    def get_friends(self) -> list[Friends]:
        return self._friends

    """

    save_profile accepts an existing dsu file to save the current instance of Profile 
    to the file system.

    Example usage:

    profile = Profile()
    profile.save_profile('/path/to/file.dsu')

    Raises DsuFileError

    """
    def save_profile(self, path: str) -> None:
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                data = {
                    'dsuserver': self.dsuserver,
                    'username': self.username,
                    'password': self.password,
                    '_friends': []
                }

                # Serialize each friend along with their messages
                for friend in self._friends:
                    friend_data = {
                        'friends': friend.friends,
                        'messa›ges': friend.messages
                    }
                    data['_friends'].append(friend_data)

                with open(p, 'w') as f:
                    json.dump(data, f)
            except Exception as ex:
                raise DsuFileError("Error while attempting to process the DSU file.", ex)
        else:
            raise DsuFileError("Invalid DSU file path or type")

    """

    load_profile will populate the current instance of Profile with data stored in a 
    DSU file.

    Example usage: 

    profile = Profile()
    profile.load_profile('/path/to/file.dsu')

    Raises DsuProfileError, DsuFileError

    """
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
                    friend = Friends(friend['friends'], friend['messages'])
                    self._friends.append(friend)
                f.close()
            except Exception as ex:
                raise DsuProfileError(ex)
        else:
            raise DsuFileError()
