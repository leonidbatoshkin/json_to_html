import json

with open("source.json", "r") as read_file:
    data = json.load(read_file)


def simple_convert(file):
    for elem in file:
        key = elem['title']
        value = elem['body']
        print(f'<h1>{key}</h1><p>{value}</p>', end='')
