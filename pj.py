import json

with open("source.json", "r") as read_file:
    data = json.load(read_file)


def simple_convert(file):
    for elem in file:
        key = elem['title']
        value = elem['body']
        print(f'<h1>{key}</h1><p>{value}</p>', end='')


def full_convert(file):
    for key, value in file.items():
        print(f'<{key}>{value}</{key}>', end='')


def make_list(file):
    print('<ul>', end='')
    for elem in file:
        print('<li>', end='')
        for key, value in elem.items():
            if type(value) is list:
                print(f'<{key}>', end='')
                make_list(value)
                print(f'</{key}>', end='')
            else:
                print(f'<{key}>{value}</{key}>', end='')
        print('</li>', end='')
    print('</ul>', end='')


def combine(file):
    if type(file) is list:
        make_list(file)
    else:
        full_convert(file)
