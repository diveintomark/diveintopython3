"""Quick-and-dirty HTML minimizer"""

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
in_pre = False
out = open(output_file, 'w')
for line in open(input_file).readlines():
    g = line.strip()
    if g.count('<pre'):
        in_pre = True
    if g.count('</pre'):
        # this will break if you have a </pre> then <pre>
        # on the same line, so don't do that
        in_pre = False
        g = line.rstrip()
    if in_pre:
        out.write(line)
    else:
        out.write(g)
out.close()
