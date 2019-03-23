import json
import re

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


def raw_html(code: str):
    return code.replace('<', '&lt;').replace('>', '&gt;')


def make_selector(file):
    pattern_id = r'#[\w-]+'
    pattern_cls = r'\.[\w-]+'

    for key, value in file.items():
        _id = re.findall(pattern_id, key)
        _cls = re.findall(pattern_cls, key)
        tg = key.split('#' if 0 < key.find('#') < key.find('.') else '.')[0]
        render_id = [tag[1:] for tag in _id]
        render_cls = [tag[1:] for tag in _cls]

        if render_id and not render_cls:
            print('<{0} id="{1}">{2}</{3}>'.format(tg, ' '.join(render_id), raw_html(value), tg), end='')
        if render_cls and not render_id:
            print('<{0} class="{1}">{2}</{3}>'.format(tg, ' '.join(render_cls), raw_html(value), tg), end='')
        else:
            print('<{0} id="{1}" class="{2}">{3}</{4}>'.format(tg, ' '.join(render_id), ' '.join(render_cls), raw_html(value), tg), end='')
