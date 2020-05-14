import sys


def read_list():
    guests = []
    try:
        with open('list.txt', 'r+') as file:
            for line in file:
                if(line.startswith('# ')):
                    guests.append(line.replace('# ', '').replace('\n', ''))
            file.close()
    except FileNotFoundError:
        pass
    return guests


def write_list(guests: list):
    with open('list.txt', 'w+') as file:
        for guest in guests:
            file.write(f'# {guest}\n')
        file.close()
