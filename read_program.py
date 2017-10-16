import itertools
from nltk import CFG
import nltk

SPECIAL_CHARACTERS = [
    'let',
    'fun',
    'true',
    'false',
    'length',
    'index',
    'let',
    'in',
    'fst',
    'snd',
    '\\',
    'rec',
    'bool',
    'int',
    'str',
    '+',
    '-',
    '*',
    '==',
    '=',
    '(',
    ')',
    ',',
    ':',
    '.',
    '->',
    '"',
    'if',
    'then',
    'else'
]


def replace_quote(string):
    if '"' in string:
        return '"{}"'.format(string[1:-2])
    return string

def read_lines(filename, replace_quotes=False):
    def get_line_generator(filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                if replace_quotes:
                    yield [replace_quote(x) for x in line.split()]
                else:
                    yield line.split()


    return list(itertools.chain.from_iterable(get_line_generator(filename)))

def get_modifier(x):
    try:
        i_x = int(x)
        return 'N'
    except:
        return 'S'

def format_str(x):
    try:
        i_x = int(x)
        return '"{}"'.format(x)
    except:
        if '"' in x:
            return '{}'.format(x)
        else:
            return '"{}"'.format(x)

def get_terminal_rules(lines):
    lines = [x for x in lines if x not in SPECIAL_CHARACTERS]
    return [
        '{} -> {}'.format(get_modifier(x), format_str(x))
        for x in lines
    ]

def get_parser_for_grammar(input_code='program.gir', grammar_name='grammar'):
    terminal_rules = get_terminal_rules(
        read_lines(input_code)
    )

    with open(grammar_name, 'r') as f:
        lines = '\n'.join([x for x in f.readlines() if x[0] != '#'])
        lines = lines + '\n' + '\n'.join(terminal_rules)
        return nltk.ChartParser(CFG.fromstring(lines))

