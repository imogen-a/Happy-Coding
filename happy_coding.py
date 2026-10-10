import pyfiglet
import os
import subprocess
from termcolor import colored

prohibited_usernames = {
    "admin", "administrator", "root", "support", "moderator", "sysadmin", "hostmaster", "postmaster", "api", "www", "ftp", "dns", "http", "mailto", "ssl", "localhost", "abuse", "security", "spam", "spamtrap", "mailer-daemon", "snapchat", "instagram"
}

def terminalcleared():
    if os.name == "nt":
        cmd = "cls"
    else: 
        cmd = 'clear'
        subprocess.call(cmd, shell=True)    

def start():
    text = pyfiglet.figlet_format("Welcome To Happy Coding!", font="slant")
    print(colored(text, "yellow"))
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
    
    print(guide)


start()