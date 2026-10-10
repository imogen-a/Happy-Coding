import pyfiglet
import os
import subprocess
from termcolor import colored

prohibited_usernames = {
    "admin", "administrator", "root", "support", "moderator", "sysadmin", "hostmaster", "postmaster", "api", "www", "ftp", "dns", "http", "mailto", "ssl", "localhost", "abuse", "security", "spam", "spamtrap", "mailer-daemon", "snapchat", "instagram"
}

# Storing registered usernames -
registered_users = [" "]

def terminalcleared():
    if os.name == "nt":
        cmd = "cls"
    else: 
        cmd = 'clear'
        subprocess.call(cmd, shell=True)    

def start():
    text = pyfiglet.figlet_format("Welcome To Happy Coding!", font="slant")
    print(colored(text, "yellow"))
    
    from ascii_magic import AsciiArt, Front

    # 1. Load the image
    smiley_art = AsciiArt.from_image('SmileyFace.jpeg')

    # 2. Print to terminal in Yellow
    smiley_art.to_terminal(columns=50, front=Front.YELLOW)
    startoptions()
    

def startoptions():
    print("========================================================================")
    print("""----> Type i and then press enter to view instructions \n----> Type c and then press enter to continue \n\n""")
    response = input()
    if response == "i" or response == "I":
        show_instructions()
    elif response == "c" or response == "C":
        login()
    else:
        print("Invalid input. Please retype your choice\n")
        return startoptions()
       
    
def show_instructions():
    terminalcleared()
    instruction = """
    =================================
         HOW TO USE HAPPY CODING
    =================================

    STEP 1: GET STARTED
    - Start with creating a username - this will allow you to save your progress.
    - The details of creating a username are in Step 2.
    - Next, select a programming language you would like to learn.
    - Then, select the level of difficulty you would like to begin with, and start coding!

    STEP 2: CREATE A USERNAME
    - Create a username - you may use a combination of letters, numbers and special symbols.
    - Note: You may get an error if the username already exists, in that case you must try a different one.
    - Once your username is created, you can log in using the 'Enter Your Username' option.

    ===================
    """

    print(instruction)
    login()
    

def login():
    
    guide = """
        ========================
                 LOG IN
        ========================

        Do you have a username?
        
            Type Y for Yes
            Type N for No
        
        ========================
        """
    
    print(guide)

    while True:
        choice = input("Enter your choice (Y/N): ").strip().lower()

        if choice == "y":
            login_username()
            break

        elif choice == "n":
            register_user()
            break
        else:
            print("Invalid choice. Please enter 'Y'or N")



# Create New Username -
def create_username(username):
    username = username.strip().lower()

    for word in prohibited_usernames:
        if word in username:
            raise ValueError(f"The username contains a prohibited word: '{word}'. Please choose a different username.")
    
    return(username)


    
# successful username creation -
def register_user():
    username = input("Create a New Username: ")
    username = create_username(username)
    print(f"Username: '{username}' Has been created successfully.")
          


# Enter the username - 
def login_username():
    username = input("Enter your Username: ").strip().lower()

    if username in registered_users:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Username not found. Please create a username.")
        return register_user()



def questions():
    pass


start()