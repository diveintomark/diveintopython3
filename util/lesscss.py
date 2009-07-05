#!/usr/bin/python2.6

from pyquery import PyQuery as pq
import glob
import sys

# These selectors are kept regardless of whether this script thinks they are used.
# Most of these match nodes that are dynamically inserted or manipulated by script
# after the page has loaded, which is why a static analysis thinks they're unused.
SELECTOR_EXCEPTIONS = ('.w', '.b', '.str', '.kwd', '.com', '.typ', '.lit', '.pun', '.tag', '.atn', '.atv', '.dec', 'pre .u', 'pre .u span')

filename = sys.argv[1]
pqd = pq(filename=filename)
raw_data = open(filename, 'rb').read()
if raw_data.count('<pre><code') or raw_data.count('<pre class=screen>'):
    def keep(s):
        for selector in SELECTOR_EXCEPTIONS:
            if s == selector: return True
            if s.startswith(selector + ' '): return True
        return False
else:
    def keep(s):
        return False

original_css = raw_data.split('<style>', 1)[1].split('@media', 1)[0]
new_css = ''
for rule in original_css.split('}')[:-1]:
    selectors, properties = rule.split('{', 1)
    selectors = ','.join([s for s in selectors.split(',') if keep(s) or pqd(s.split(':', 1)[0])])
    if selectors:
        new_css += '%s{%s}' % (selectors, properties)
open(filename, 'wb').write(raw_data.replace(original_css, new_css))
