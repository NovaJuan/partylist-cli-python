# Create a party list usign python and commands
# '--add' or '-a' to add a new guest
# '--list' or '-l' to get the list of guests
# '--remove' or '-r' to remove a guest
# '--remove-index' or '-ri' to remove a guest with a specific index
# '--dump' or '-D' to dump the list

import sys
import os
import platform
from methods.list_handlers import add_guest, remove_guest, remove_index, get_list, dump_list


def commands():
    print('\nThese are the available commands:')
    print('\n%-14s  %-4s to add a new guest' % ('--add', '-a'))
    print('%-14s  %-4s to get the list of guests' % ('--list', '-l'))
    print('%-14s  %-4s to remove a guest' % ('--remove', '-r'))
    print('%-14s  %-4s to remove a guest with a specific index' %
          ('--remove-index', '-ri'))
    print('%-14s  %-4s to dump the list' % ('--dump', '-d'))


def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Darwin' or system == 'Linux':
        os.system('clear')


if __name__ == "__main__":
    clear_terminal()

    command = None
    try:
        command = sys.argv[1]
    except IndexError:
        print('\nPlease enter a command')
        print('Use \'python main.py --help\' to see all commands.')
        sys.exit()

    if command == '--add' or command == '-a':
        guest = input('Enter the guest\'s name: ')
        add_guest(guest)

    elif command == '--list' or command == '-l':
        get_list()

    elif command == '--remove' or command == '-r':
        guest = input('Enter the guest\'s name: ')
        remove_guest(guest)

    elif command == '--remove-index' or command == '-ri':
        get_list()
        index = None
        try:
            index = int(input('\nEnter the guest\'s index: '))
        except ValueError:
            print(f'\nIndex has to be a number.')
            sys.exit()
        remove_index(index)

    elif command == '--dump' or command == '-d':
        dump_list()

    elif command == '--help' or command == '-h':
        commands()

    else:
        print(f'\nCommand \'{command}\' is not valid.')
        print('Use \'python main.py --help\' to see all commands.')
