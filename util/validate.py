import sys
try:
    import html5lib
except ImportError:
    sys.path.insert(0, '/home/pilgrim/code/html5lib/python3/src/')
    import html5lib

input_filename = sys.argv[1]
parser = html5lib.HTMLParser()
with open(input_filename, encoding='utf-8') as stream:
    data = stream.read()
html5doc = parser.parse(data, encoding='utf-8')
if parser.errors:
    for ((line, column), errtype, params) in parser.errors:
        print("Error: {} {} on line {} of {}".format(errtype, repr(params), line, input_filename), file=sys.stderr)
    sys.exit(1)

