import pyfiglet
from termcolor import colored

fonts = ["slant"]

for f in fonts:
    text = pyfiglet.figlet_format("Welcome To Happy Coding!", font=f)
    colored_text = colored(text, 'cyan')
    print(f"\nFont: {f}\n")
    print(colored_text)
    