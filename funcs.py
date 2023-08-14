import random, time
import DivItems, styles

from rich.console import Console


console = Console()
result_string = ''
primary_color = []
secondary_color = []


def color_picker(item):
    color = ''
    if item == 'DHIH':
        color = 'magenta'
    if item == 'RA':
        color = 'red'
    if item == 'PA':
        color = 'white'
    if item == 'TSA':
        color = 'green'
    if item == 'NA':
        color = 'yellow'
    if item == 'AH':
        color = 'cyan'

    return color


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

    primary_color.append(color_picker(result[0]))
    secondary_color.append(color_picker(result[1]))


    # Calculate and print the padding for centering
    total_line_length = sum(len(f'{item} ') for item in result) - 1
    padding = (console.width - total_line_length) // 2
    console.print(' ' * padding, end='')

    for item in result:
        console.print(f'[bold {color_picker(item)}]{item}[/]', end=' ')
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
