"""Quick-and-dirty HTML minimizer"""

import sys, re, html.entities

input_file = sys.argv[1]
output_file = sys.argv[2]
in_pre = False
out = open(output_file, 'w', encoding="utf-8") # encoding argument! important!
for line in open(input_file).readlines():
    # replace entities with Unicode characters
    for e in re.findall('&(.+?);', line):
        n = html.entities.name2codepoint.get(e)
        if not n:
            if e.count('#x'):
                # it's late, forgive me
                n = eval(e.replace('#', '0'))
            elif e.count('#'):
                n = int(e.replace('#', ''))
            else:
                continue
        line = line.replace('&' + e + ';', chr(n))

    # strip leading and trailing whitespace, except inside <pre> blocks
    g = line.strip()
    if g.count('<pre'):
        in_pre = True
    if g.count('</pre'):
        # XXX this will break if you have </pre><pre> in one line
        in_pre = False
        g = line.rstrip()
    if in_pre:
        out.write(line)
    else:
        out.write(g)
out.close()
