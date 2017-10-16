from read_program import get_parser_for_grammar, read_lines
from nltk.draw.tree import TreeView


def parse_file_with_grammar(filename='program.gir', grammar='grammar'):
    parser = get_parser_for_grammar(filename, grammar)
    prog_lines = read_lines(filename, replace_quotes=True)

    for elem in parser.parse(prog_lines):
        elem.draw()
        return

def draw():
    parse_file_with_grammar()

if __name__ == '__main__':
    parse_file_with_grammar()