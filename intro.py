import pyfiglet
from termcolor import colored

text = pyfiglet.figlet_format("Welcome To Happy Coding!", font="slant")
print(colored(text, "yellow"))