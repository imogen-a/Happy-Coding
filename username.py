# Usernames Prohibited to use -
prohibited_usernames = {
    "admin", "administrator", "root", "support", "moderator", "sysadmin", "hostmaster", "postmaster", "api", "www", "ftp", "dns", "http", "mailto", "ssl", "localhost", "abuse", "security", "spam", "spamtrap", "mailer-daemon", "snapchat", "instagram"
}

# converts to lowercase to catch the prohibited names -
def is_valid_username(username):
    cleaned_username = username.strip().lower()

    if cleaned_username in prohibited_usernames:
        return False
    return True

# terminal cleared -
# def terminalcleared():
#     if os.name == "nt":
#         cmd = "cls"
#     else: 
#         cmd = 'clear'
#         subprocess.call(cmd, shell=True) 


# User jumps to login/create username -
def login():
    #terminalcleared()
    #print("Please enter your username")
    
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
    choice = input("Enter your choice (Y/N): ").strip().lower()

    if choice == "y":
        login_username()

    elif choice == "n":
        create_username(username)
    
    # Create New Username -
    def create_username(username):
        username = username.strip().lower()

        for word in prohibited_usernames:
            if word in username:
                raise ValueError(f"The username contains a prohibited word: '{word}'. Please choose a different username.")
        
        return(username)

    # successful username creation -
    while True:
        username = input("Create a New Username: ")

        try:
            username = create_username(username)
            print(f"Username: '{username}' Has been created successfully.")
            break

        except ValueError as error:
            print(error)


    # Storing registered usernames -
    registered_users = [username]

    # Enter the username - 
    def login_username():
        username = input("Enter your Username: ").strip().lower()

        if username in registered_users:
            print(f"Welcome back, {username}!")
            return username
        else:
            print("Username not found. Please try again.")
            return None

login()

