import sys
from methods.file_handlers import read_list, write_list


def get_list():
    print('\nThese are your current guests:\n')
    guests = read_list()
    if len(guests) == 0:
        print('No guests in your list.')
        sys.exit()
    for i in range(len(guests)):
        print(f'{i + 1}. {guests[i]}\n')


def add_guest(name: str):
    if not name:
        print('Please enter a name')

    guests = read_list()

    if name in guests:
        print(f'\n{name} is already in your list.')
        sys.exit()

    with open('list.txt', 'a+') as file:
        file.write(f'# {name}\n')
        print(f'\n{name} was added to the list.')
        file.close()

    sys.exit()


def remove_guest(name: str):
    if not name:
        print('\nPlease enter a name')
        sys.exit()

    guests = read_list()

    if name not in guests:
        print('\nThat guest is not in the list.')

    for i in range(len(guests)):
        if guests[i] == name:
            del guests[i]
            write_list(guests)
            return print(f'\n{name} was deleted')


def dump_list():
    confirmation = input(
        '\nAre you sure want to dump your list? (Y)es or (N)o: ')

    if confirmation == 'Y' or confirmation == 'y':
        write_list([])
        print('\nYour list was successfully dumped.')
        sys.exit()


def remove_index(i: int):
    if not i:
        print('\nPlease enter a index')

    i = i - 1

    guests = read_list()

    if len(guests) == 0:
        print('There are no guests in your list.')
        sys.exit()

    if i >= len(guests) or i < 0:
        print('\nThat index is not in the list.')
        sys.exit()

    del guests[i]
    write_list(guests)
    return print(f'\nIndex {i + 1} was deleted')
