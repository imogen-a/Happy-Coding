import pyfiglet
from termcolor import colored

def start():
    #display welcome banner
    #welcome images
    fonts = ["slant"]

    for f in fonts:
        text = pyfiglet.figlet_format("Welcome To Happy Coding!", font=f)
        colored_text = colored(text, 'cyan')
        print(f"\nFont: {f}\n")
        print(colored_text)
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
        startoptions()


    
def show_instructions():
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
    print("Please enter your username")
    

start()
