import pyfiglet
import os
import subprocess
from termcolor import colored
from google import genai

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
    return username
          


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
    
    print("Welcome to Happy Coding!")

    level = input(
        "Choose assessment level:\n"
        "1. Beginner\n"
        "2. Intermediate\n"
        "3. Advanced\n"
    )

    if level == "1":
        difficulty = "Beginner"
    elif level == "2":
        difficulty = "Intermediate"
    elif level == "3":
        difficulty = "Advanced"
    else:
        print("Invalid choice. Defaulting to Beginner.")
        difficulty = "Beginner"

    print(f"\nStarting {difficulty} Assessment...")

    client = genai.Client(api_key="AQ.Ab8RN6KZXcListEzSHN8ctMeUQYneDSrVDYJQOnmDnvvInXUsw")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"""
    Create 20 {difficulty} coding multiple-choice questions.

    Use a mixture of:
    - Multiple Choice
    - True or False
    - Fill in the Blank

    Format each question as follows:

    Question Type: Multiple Choice

    Question: ...
    A) ...
    B) ...
    C) ...
    D) ...
    Correct Answer: X

    ###

    Question Type: True/False

    Question: ...
    Correct Answer: True

    ###

    Question Type: Fill in the Blank

    Question: Complete the code:
    for i in ______(5):
    Correct Answer: range

    ###

    Separate each question with ###.
    """
    )

    questions = response.text.split("###")

    score = 0

    for question_num, question in enumerate(questions, start=1):

        if not question.strip():
            continue

        print(f"\nQuestion {question_num}/20")
        print(question)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        try:
            correct_answer = (
                question.split("Correct Answer:")[1]
                .strip()[0]
                .upper()
            )

            if answer == correct_answer:
                score += 1
                print("✅ Correct!")
            else:
                print(f"❌ Incorrect. Correct answer: {correct_answer}")

        except Exception:
            print("⚠ Could not determine correct answer.")

    print("\nAssessment Complete!")
    print(f"Final Score: {score}/20")

    if score <= 7:
        result_level = "Beginner"
    elif score <= 14:
        result_level = "Intermediate"
    else:
        result_level = "Advanced"

    with open("results.txt", "a") as file:
        file.write(f" {score}/20, {result_level}\n")

    print("Results saved!")
    print("Your coding level:", result_level)


start()