def is_between(before, current, after):
    items = [before, current, after]
    return items == sorted(items)


def interpret_western_sign(day, month):
    signs = [
        {'name': 'aries',       'from': (3, 21),  'to': (4, 20)},
        {'name': 'taurus',      'from': (4, 21),  'to': (5, 20)},
        {'name': 'gemini',      'from': (5, 21),  'to': (6, 20)},
        {'name': 'cancer',      'from': (6, 21),  'to': (7, 22)},
        {'name': 'leo',         'from': (7, 23),  'to': (8, 22)},
        {'name': 'virgo',       'from': (8, 23),  'to': (9, 22)},
        {'name': 'libra',       'from': (9, 23),  'to': (10, 22)},
        {'name': 'scorpio',     'from': (10, 23), 'to': (11, 21)},
        {'name': 'sagittarius', 'from': (11, 22), 'to': (12, 21)},
        {'name': 'capricorn',   'from': (12, 22), 'to': (12, 31)},
        {'name': 'capricorn',   'from': (1,  1),  'to': (1, 20)},
        {'name': 'aquarius',    'from': (2, 21),  'to': (2, 19)},
        {'name': 'pisces',      'from': (2, 19),  'to': (3, 20)},
    ]

    for sign in signs:
        if (is_between(sign['from'], (month, day), sign['to'])):
            return sign['name']


def interpret_chinese_sign(year):
    signs = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse',
             'sheep', 'monkey', 'rooster', 'dog', 'pig']

    return signs[(year - 1900) % len(signs)]


def interpret_both_signs(day, month, year):
    return (interpret_western_sign(day, month), interpret_chinese_sign(year))
