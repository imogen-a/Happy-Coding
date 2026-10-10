import pyfiglet
from termcolor import colored

fonts = ["standard", "slant", "block", "big", "banner3-D", "digital", "isometric1", "starwars"]

for f in fonts:
    text = pyfiglet.figlet_format("Welcome To Happy Coding!", font=f)
    colored_text = colored(text, 'cyan')
    print(f"\nFont: {f}\n")
    print(colored_text)