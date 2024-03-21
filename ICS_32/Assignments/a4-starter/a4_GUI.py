import tkinter as tk
from tkinter import ttk, filedialog
from typing import Text
import ds_messenger
import tkinter.messagebox as messagebox
import Profile_a4
from pathlib import Path
import json

class Body(tk.Frame):
    def __init__(self, root, recipient_selected_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the Body instance
        self._draw()

    def node_select(self, event):
        index = int(self.posts_tree.selection()[0])
        entry = self._contacts[index]
        if self._select_callback is not None:
            self._select_callback(entry)

    def insert_contact(self, contact: str):
        self._contacts.append(contact)
        id = len(self._contacts) - 1
        self._insert_contact_tree(id, contact)

    def _insert_contact_tree(self, id, contact: str):
        if len(contact) > 25:
            entry = contact[:24] + "..."
        id = self.posts_tree.insert('', id, id, text=contact)

    def insert_user_message(self, message:str):
        self.entry_editor.insert(1.0, message + '\n', 'entry-right')

    def insert_contact_message(self, message:str):
        self.entry_editor.insert(1.0, message + '\n', 'entry-left')

    def get_text_entry(self) -> str:
        return self.message_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text:str):
        self.message_editor.delete(1.0, tk.END)
        self.message_editor.insert(1.0, text)
        
    def clear_messages(self):
        # Clear the message display area (e.g., Text widget)
        self.entry_editor.delete('1.0', tk.END)

    def _draw(self):
        posts_frame = tk.Frame(master=self, width=250)
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP,
                             expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        message_frame = tk.Frame(master=self, bg="yellow")
        message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        self.message_editor = tk.Text(message_frame, width=0, height=5)
        self.message_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                                 expand=True, padx=0, pady=0)

        self.entry_editor = tk.Text(editor_frame, width=0, height=5)
        self.entry_editor.tag_configure('entry-right', justify='right')
        self.entry_editor.tag_configure('entry-left', justify='left')
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                               expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame,
                                              command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT,
                                    expand=False, padx=0, pady=0)


class Footer(tk.Frame):
    def __init__(self, root, send_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._draw()

    def send_click(self):
        if self._send_callback is not None:
            self._send_callback()

    def _draw(self):
        save_button = tk.Button(master=self, text="Send", width=20, command=self.send_click)
        # You must implement this.
        # Here you must configure the button to bind its click to
        # the send_click() function.
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)


class NewContactDialog(tk.simpledialog.Dialog):
    def __init__(self, root, title=None, user=None, pwd=None, server=None):
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        super().__init__(root, title)

    def body(self, frame):
        self.server_label = tk.Label(frame, width=30, text="DS Server Address")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, self.server)
        self.server_entry.pack()

        self.username_label = tk.Label(frame, width=30, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, self.user)
        self.username_entry.pack()

        # You need to implement also the region for the user to enter
        # the Password. The code is similar to the Username you see above
        # but you will want to add self.password_entry['show'] = '*'
        # such that when the user types, the only thing that appears are
        # * symbols.
        #self.password...
        self.password_label = tk.Label(frame, width=30, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(frame, width=30)
        self.password_entry.insert(tk.END, self.pwd)
        self.password_entry['show'] = '*'
        self.password_entry.pack()

    def apply(self):
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()
        self.server = self.server_entry.get()

class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        file_username = input("Thank You! Please Enter Your Username You Want: \n")
        file_password = input("Thank You! Please Enter Your Password You Want: \n")
        server = input("Please Enter the IP Address for the Server: \n")
        user_input = input("Welcome! Do you want to create or load a DSU file (type 'c' to create or ‘o' to load): \n")
        global file_path
        if user_input == "c":
            file_name = input("Great! What would you like the name the File? \n")
            file_path = input("Thank You! Where would you like the file to be placed? (Send the Path) \n")

            try:
            
                file_path = file_path + "/" + file_name + ".dsu"
                file_Path = Path(file_path)

                if file_Path.exists():
                    print("Your File Has Already Been Created")
                    user_profile = Profile_a4.Profile()
                    user_profile.load_profile(file_path)
                    print("File has been Loaded Successfully")
                else:
                    file_Path.touch()
                    print("Your File Has Been Created")
                    user_profile = Profile_a4.Profile(dsuserver=file_path, username=file_username, password=file_password)
                    user_profile.save_profile(file_path)
                    user_profile.load_profile(file_path)
            except Exception as error:
                print("Error: a4.py create", error)
        elif user_input == "o":
            try:
                file_path = str(input("Great! What is the name of the file you would like to load? \n"))
                if ".dsu" in file_path:
                    user_profile = Profile_a4.Profile()
                    user_profile.load_profile(file_path)
                    print("Your File Has Been Loaded")
                else:
                    print("Invalid File Path (user_input o error)")
            except Exception as error:
                print("Error: a4.py load", error)
        self.username = file_username
        self.password = file_password
        self.server = server #"168.235.86.101"
        self.recipient = None
        self.dsu_file = file_path
        # You must implement this! You must configure and
        # instantiate your DirectMessenger instance after this line.
        #self.direct_messenger = ... continue!
        self.direct_messenger = ds_messenger.DirectMessenger(self.server, self.username, self.password)
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the root frame
        self._draw()
        with open(self.dsu_file, "r") as file:
            profile_data = json.load(file)
        friends_list = profile_data["_friends"]

        for friend in friends_list:
            self.body.insert_contact(friend)

    def send_message(self):
        # You must implement this!
        message = self.body.get_text_entry()
        send_msg = self.direct_messenger.send(message, self.recipient)

        post = Profile_a4.Post()
        post.set_entry(message)
        post.set_recipient(self.recipient)
        post.update_recipient(self.recipient)

        user_profile = Profile_a4.Profile()
        user_profile.load_profile(file_path)
        user_profile.get_posts()
        user_profile.add_post(post)
        user_profile.save_profile(file_path)
        self.publish(send_msg)

    def add_contact(self):
        # You must implement this!
        # Hint: check how to use tk.simpledialog.askstring to retrieve
        # the name of the new contact, and then use one of the body
        # methods to add the contact to your contact list
        contact = tk.simpledialog.askstring("Contact", "Add your contact:")
        if contact not in self.body._contacts:
            self.body.insert_contact(contact)
            friend = Profile_a4.Friends()
            friend.set_friends(contact)
            user_profile = Profile_a4.Profile()
            user_profile.load_profile(file_path)
            user_profile.add_friend(contact)
            user_profile.save_profile(file_path)
        else:
            messagebox.showinfo("Contact Exists", f"The contact '{contact}' already exists.")


    def recipient_selected(self, recipient):
        self.recipient = recipient
        self._current_recipient = recipient
        # Clear the message display area
        self.body.clear_messages()

        self.publish_recipient()
        self.body.set_text_entry("")

    def configure_server(self):
        ud = NewContactDialog(self.root, "Configure Account",
                              self.username, self.password, self.server)
        self.username = ud.user
        self.password = ud.pwd
        self.server = ud.server
        # You must implement this!
        # You must configure and instantiate your
        # DirectMessenger instance after this line.
        self.direct_messenger = ds_messenger.DirectMessenger(self.server, self.username, self.password)

    def publish(self, message:str):
        message = self.body.get_text_entry()
        # You must implement this!
        self.body.insert_user_message(message)

    def publish_recipient(self):
        self.body.clear_messages()
        try:
            all_messages = self.direct_messenger.retrieve_all()
            for message in all_messages:
                if message['from'] == self.recipient:
                    self.body.insert_contact_message(message['message'])
                    friend = Profile_a4.Friends()
                    friend.set_friends(message['from'])
                    profile_message = Profile_a4.Message()
                    profile_message.set_messages(message)
                    user_profile = Profile_a4.Profile()
                    user_profile.load_profile(file_path)
                    user_profile.get_messages()
                    user_profile.add_message(message)
                    user_profile.save_profile(file_path)
        except:
            user_profile = Profile_a4.Profile()
            user_profile.load_profile(file_path)
            all_messages = user_profile.get_messages()
            for message in all_messages:
                if message['from'] == self.recipient:
                    self.body.insert_contact_message(message['message'])


    def check_new(self):
        # You must implement this!
        new_messages = self.direct_messenger.retrieve_new()
        for message in new_messages:
            if message['from'] == self.recipient:
                self.body.insert_contact_message(message['message'])
                friend = Profile_a4.Friends()
                friend.set_friends(message['from'])
                profile_message = Profile_a4.Message()
                profile_message.set_messages(message)
                user_profile = Profile_a4.Profile()
                user_profile.load_profile(file_path)
                print("Your File Has Been Loaded")
                user_profile.get_messages()
                user_profile.add_message(message)
                user_profile.save_profile(file_path)
        self.root.after(2000, self.check_new)

    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New')
        menu_file.add_command(label='Open...')
        menu_file.add_command(label='Close')

        settings_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=settings_file, label='Settings')
        settings_file.add_command(label='Add Contact',
                                  command=self.add_contact)
        settings_file.add_command(label='Configure DS Server',
                                  command=self.configure_server)
        # The Body and Footer classes must be initialized and
        # packed into the root window.
        self.body = Body(self.root,
                         recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.footer = Footer(self.root, send_callback=self.send_message)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)

if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social Messenger")

    # This is just an arbitrary starting point. You can change the value
    # around to see how the starting size of the window changes.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that
    # some modern OSes don't support. If you're curious, feel free to comment
    # out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the
    # widgets used in the program. All of the classes that we use,
    # subclass Tk.Frame, since our root frame is main, we initialize
    # the class with it.
    app = MainApp(main)

    # When update is called, we finalize the states of all widgets that
    # have been configured within the root frame. Here, update ensures that
    # we get an accurate width and height reading based on the types of widgets
    # we have used. minsize prevents the root window from resizing too small.
    # Feel free to comment it out and see how the resizing
    # behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    id = main.after(2000, app.check_new)
    print(id)
    # And finally, start up the event loop for the program (you can find
    # more on this in lectures of week 9 and 10).
    main.mainloop()
