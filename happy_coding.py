import keyboard

def start():
    #display welcome banner
    #welcome images
    print("Welcome to Happy Coding!\n\n\n")
    startoptions()
    
   

def startoptions():
    response = input(print("Press i and then enter to view instructions or c and then enter to continue \n\n"))
    if response == "i" or response == "I":
        features()
    elif response == "c" or response == "C":
        login()
    else:
        print("Invalid input. Please retype your choice")
        startoptions()

def features():
    print("instructions w/ log in/cre")
    login()

def login():
    print("log in")

start()
