import typer
import sys, random, time
import DivItems

app = typer.Typer()
def roll():
    bija = {
        '1': 'DHIH',
        '2': 'RA',
        '3': 'PA',
        '4': 'TSA',
        '5': 'NA',
        '6': 'AH'
    }

    lot = (random.randint(1, 6), random.randint(1, 6))
    result = [bija[str(item)] for item in lot]

    for item in result:
        print(item, end=' ', flush=True)
        time.sleep(1)

    result_string = "_".join(result)
    item_function = getattr(DivItems, result_string)

    time.sleep(1)
    item_function.submenu()

def check():
    check = input("Enter the syllables of the divination: ")
    if '_' not in check:
        check = check.replace(" ", "_")
    item_check = getattr(DivItems, check)
    item_check.submenu()



def menu():
    print("\n MO DIVINATION"+ '\n')
    time.sleep(2)
    option = input("\n [1] Ask a question \n [2] Check results \n [3] Quit \n ")

    if option == '1':
        input("Focus on the question and press Enter... ")
        roll()
        time.sleep(2)
    elif option == '2':
        check()
    elif option == '3' or option.lower() == 'q':
        print("\n Good bye! \n")
        sys.exit()
    else:
        print(" \n Choose a valid option and press Enter. \n")

while True:
    menu()

if __name__ == "__main__":
    app()

#TODO: explore Typer options for running from CLI
