# giraffe-viewer

Uses Python nltk to generate abstract syntax trees for a given giraffe programme, as defined in the [Elements of programming languages course](https://www.inf.ed.ac.uk/teaching/courses/epl/) at The University of Edinburgh.

# Instructions

### Dependencies:
- python
- nltk

### How to install
`git clone https://github.com/livecodealex/giraffe-viewer.git`<br />

### How to run
`$ python`<br />
`python> from ast import *` <br />
`python> draw()` (This will assume the filename of the grammar is *grammar* and the filename of the program is *program.gir*) <br />
`python> parse_file_with_grammar(<filename>, <grammar_filename>)`<br />

### Known limitations
- The giraffe file must be free of quotes. Please remove them, strings will be treated as literals
- The giraffe file must not contain empty strings. If it does, please replace the "" with EMPTY_STRING or another name of your choice (you need not edit the grammar)
- The tokens in the giraffe file must be space separated (i.e. `func(a:int,b:int)` is illegal, it must be `func ( a : int , b : int )`)

