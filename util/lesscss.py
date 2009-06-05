#!/usr/bin/python2.6

from pyquery import PyQuery as pq
import glob
import sys

filename = sys.argv[1]
pqd = pq(filename=filename)
raw_data = open(filename, 'rb').read()
if raw_data.count('<pre'):
    def keep(s):
        return s == '.w' or s.startswith('.w ') or s == '.b' or s.startswith('.b ')
else:
    def keep(s):
        return False

original_css = raw_data.split('<style>', 1)[1].split('</style>', 1)[0]
new_css = ''
for rule in original_css.split('}')[:-1]:
    selectors, properties = rule.split('{', 1)
    selectors = ','.join([s for s in selectors.split(',') if keep(s) or pqd(s.split(':', 1)[0])])
    if selectors:
        new_css += '%s{%s}' % (selectors, properties)
open(filename, 'wb').write(raw_data.replace(original_css, new_css))
