import sys, random, time
import DivItems, funcs, styles

from rich.styled import Styled
from rich.console import Console

console = Console()

def menu():

    title_txt = Styled("\n\n   MO DIVINATION \n\n\n", styles.title)
    console.print(title_txt, justify="center")
    time.sleep(1)

    options_txt = Styled("[1] Ask a question \n [2] Browse results \n [3] Quit", styles.regular)
    console.print(options_txt, justify="center")

    console.print(" \n\n\n\n original text by Jamgon Mipham, trans. by Jay Goldberg and Lobsang Dakpa \n all rights belong to their rightful owners", style="gray35", justify="center")


    option = input()

    if option == '1':
        console.print(Styled(" \n\n Focus on the question and press Enter... \n\n", styles.regular), justify="center")
        input()
        funcs.roll()
        time.sleep(2)
    elif option == '2':
        funcs.check()
    elif option == '3' or option.lower() == 'q':
        console.print(Styled("\n Good bye! \n", styles.regular), justify="center")
        sys.exit()
    else:
        console.print(Styled(" \n Choose a valid option and press Enter. \n", styles.regular), justify="center")

while True:
    menu()

if __name__ == "__main__":
    menu()
