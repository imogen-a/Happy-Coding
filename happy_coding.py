
def start():
    #display welcome banner
    #welcome images
    print("Welcome to Happy Coding!\n")
    startoptions()
    


def startoptions():
    print("""----> Type i and then press enter to view instructions \n----> Type c and then press enter to continue \n\n""")
    response = input()
    if response == "i" or response == "I":
        features()
    elif response == "c" or response == "C":
        login()
    else:
        print("Invalid input. Please retype your choice\n")
        startoptions()



def features():
    print("instructions w/ log in option at bottom")
    login()

def login():
    print("Please enter your username")
    

start()
