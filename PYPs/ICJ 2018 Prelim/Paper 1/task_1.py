from typing import List


DRINKS_FILEPATH = 'DRINKS.txt'


def read_file() -> List[List[str]]:
    '''Read DRINKS_FILEPATH line by line and return 2D list of drinks'''

    result = [[], [], []] # brewed coffee, brewed tea drinks, others

    with open(DRINKS_FILEPATH, 'r') as f:
        line = True
        while line:
            line = f.readline().strip()
            if line:
                first = line.split()[0]
                if first == 'Kopi':
                    result[0].append(line)
                elif first == 'Teh':
                    result[1].append(line)
                else:
                    result[2].append(line)
    return result


def main():
    '''Main program'''

    Drinklist = read_file()
    print('''Menu
    1.	Brewed coffee
    2.	Brewed tea
    3.	Other drinks
    ''')

    while 1:
        choice = input('Select an option: ')
        if choice.isdigit() and 1 <= int(choice) <= 3:
            choice = int(choice)
            break
        print('Please enter a number from 1-3, inclusive\n')
            
    print('-----------------')
    print(
        'Brewed coffee' if choice == 1 else \
        'Brewed tea drinks' if choice == 2 else \
        'Others'
    )
    
    for drink in Drinklist[choice-1]:
        print(drink)
    
    print(f'\nTotal items: {len(Drinklist[choice-1])}')

    
main()