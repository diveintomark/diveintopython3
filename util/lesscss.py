#!/usr/bin/python2.5

from pyquery import PyQuery as pq
import glob
import sys

# These selectors are kept regardless of whether this script thinks they are used.
# Most of these match nodes that are dynamically inserted or manipulated by script
# after the page has loaded, which is why a static analysis thinks they're unused.
SELECTOR_EXCEPTIONS = ('.w', '.b', '.str', '.kwd', '.com', '.typ', '.lit', '.pun', '.tag', '.atn', '.atv', '.dec', 'pre .u', 'pre .u span', 'td .u', 'li ol', 'a.hl:link', 'a.hl:visited', 'a.hl:hover', 'h2[id]:hover a.hl', 'h3[id]:hover a.hl')

filename = sys.argv[1]
cssfilename = sys.argv[2]
pqd = pq(filename=filename)
raw_data = open(filename, 'rb').read()
if raw_data.count('</a><script src=j/'): # HACK HACK HACK
    def keep(s):
        for selector in SELECTOR_EXCEPTIONS:
            if s == selector: return True
            if s.startswith(selector + ' '): return True
        return False
else:
    def keep(s):
        return False

original_css = open(cssfilename, 'rb').read();
new_css = ''
for rule in original_css.split('}')[:-1]:
    selectors, properties = rule.split('{', 1)
    selectors = ','.join([s for s in selectors.split(',') if keep(s) or pqd(s.split(':', 1)[0])])
    if selectors:
        new_css += '%s{%s}' % (selectors, properties)

sys.stdout.write(new_css)
