import json
import re

with open("source.json", "r") as read_file:
    data = json.load(read_file)
    result = ''


def simple_convert(file):
    global result
    for elem in file:
        key = elem['title']
        value = elem['body']
        result += f'<h1>{key}</h1><p>{value}</p>'
    return result


def full_convert(file):
    global result
    for key, value in file.items():
        result += f'<{key}>{value}</{key}>'
    return result


def make_list(file):
    global result
    result += '<ul>'
    for elem in file:
        result += '<li>'
        for key, value in elem.items():
            if type(value) is list:
                result += f'<{key}>'
                make_list(value)
                result += f'</{key}>'
            else:
                result += f'<{key}>{value}</{key}>'
        result += '</li>'
    result += '</ul>'
    return result


def combine(file):
    if type(file) is list:
        return make_list(file)
    else:
        return full_convert(file)


def raw_html(code: str):
    return code.replace('<', '&lt;').replace('>', '&gt;')


def make_selector(file):
    global result
    pattern_id = r'#[\w-]+'
    pattern_cls = r'\.[\w-]+'

    for key, value in file.items():
        _id = re.findall(pattern_id, key)
        _cls = re.findall(pattern_cls, key)
        tg = key.split('#' if 0 < key.find('#') < key.find('.') else '.')[0]
        render_id = [tag[1:] for tag in _id]
        render_cls = [tag[1:] for tag in _cls]

        if render_id and not render_cls:
            result += '<{0} id="{1}">{2}</{3}>'.format(tg, ' '.join(render_id), raw_html(value), tg)
        if render_cls and not render_id:
            result += '<{0} class="{1}">{2}</{3}>'.format(tg, ' '.join(render_cls), raw_html(value), tg)
        else:
            result += '<{0} id="{1}" class="{2}">{3}</{4}>'.format(tg, ' '.join(render_id), ' '.join(render_cls), raw_html(value), tg)
    return result
