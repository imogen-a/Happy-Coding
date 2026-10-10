import pyfiglet
from termcolor import colored

text = pyfiglet.figlet_format("Welcome To Happy Coding!", font="slant")
print(colored(text, "yellow"))

#Importing a Smiley face to the bottom of the page

from ascii_magic import AsciiArt, Front

# 1. Load the image
smiley_art = AsciiArt.from_image('SmileyFace.jpeg')

# 2. Print to terminal in Yellow
smiley_art.to_terminal(columns=50, front=Front.YELLOW)