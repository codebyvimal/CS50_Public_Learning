import sys
from pyfiglet import Figlet
import random

x = Figlet()
all_fonts = x.getFonts()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    print("Invalid Usage")
    sys.exit(1)
if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Invalid Usage")
        sys.exit(1)

if len(sys.argv) == 1:
        random_font = random.choice(all_fonts)
        Text = input("Input: ")
        print(x.renderText(Text))

elif len(sys.argv) == 3:
    try:
        x = Figlet(font = sys.argv[2])
        Text = input("Input: ")
        print(x.renderText(Text))
    except:
        sys.exit(1)



