from pathlib import Path
import Profile_a4
def main():
    user_input = input("Welcome! Do you want to create or load a DSU file (type 'c' to create or ‘o' to load): \n")
    if user_input == "c":
        file_name = input("Great! What would you like the name the File? \n")
        file_path = input("Thank You! Where would you like the file to be placed? (Send the Path) \n")
        file_username = input("Thank You! Please Enter Your Username You Want: \n")
        file_password = input("Thank You! Please Enter Your Password You Want: \n")
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
            file_name = str(input("Great! What is the name of the file you would like to load? \n"))
            if ".dsu" in file_name:
                user_profile = Profile_a4.Profile()
                user_profile.load_profile(file_name)
                print("Your File Has Been Loaded")
            else:
                print("Invalid File Path (user_input o error)")
        except Exception as error:
            print("Error: a4.py load", error)
    elif user_input == "add post":
        file_name = str(input("Great! What is the name of the file you would like to load? \n"))
        recipient = input("Who would you like to send the post to? \n")
        if ".dsu" in file_name:
            post = Profile_a4.Post()
            post.set_entry("HUHYUNJINLOVER")
            post.set_recipient(recipient)
            user_profile = Profile_a4.Profile()
            user_profile.load_profile(file_name)
            print("Your File Has Been Loaded")
            user_profile.get_posts()
            user_profile.add_post(post)
            user_profile.save_profile(file_name)
            print("Post has been Uploaded")
        else:
            print("Invalid File Path (user_input o error)")
        '''
        except Exception as error:
            print("Error: ", error)
        '''
    elif user_input == "add friend":
        file_name = str(input("Great! What is the name of the file you would like to load? \n"))
        recipient = input("Enter your friend? \n")
        if ".dsu" in file_name:
            friend = Profile_a4.Friends()
            friend.set_friends(recipient)
            user_profile = Profile_a4.Profile()
            user_profile.load_profile(file_name)
            print("Your File Has Been Loaded")
            user_profile.get_friends()
            user_profile.add_friend(recipient)
            user_profile.save_profile(file_name)
            print("Friend has been Uploaded")
        else:
            print("Invalid File Path (user_input o error)")
        '''
        except Exception as error:
            print("Error: add friend", error)
        '''
    elif user_input == "add message":
        file_name = str(input("Great! What is the name of the file you would like to load? \n"))
        recipient = input("Enter your friend? \n")
        if ".dsu" in file_name:
            friend = Profile_a4.Friends()
            friend.set_friends(recipient)
            user_profile = Profile_a4.Profile()
            user_profile.load_profile(file_name)
            print("Your File Has Been Loaded")
            user_profile.get_friends()
            user_profile.add_friend(recipient)
            user_profile.save_profile(file_name)
            print("Friend has been Uploaded")
        else:
            print("Invalid File Path (user_input o error)")

if __name__ == "__main__":
    main()