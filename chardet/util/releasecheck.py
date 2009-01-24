import sys, re, time
import os
print os.getcwd()
print sys.path
import chardet
import chardet.constants

if chardet.constants._debug:
    sys.stderr.write('constants._debug == 1\n')
    sys.exit(1)

makefile_version = None
chardet_version = None
setup_version = None
docs_version = None
docs_date = None

makefile_re = re.compile(r'^VERSION\s*=\s*(.*?)$')
for line in file('Makefile'):
    m = makefile_re.search(line)
    if m:
        makefile_version = m.group(1)
        break
if not makefile_version:
    sys.stderr.write('could not determine Makefile version\n')
    sys.exit(1)

chardet_version = chardet.__version__
if not chardet_version:
    sys.stderr.write('could not determine chardet/__init__.py version\n')
    sys.exit(1)

docs_re = re.compile(r'^<!ENTITY\s*chardet_version\s*["\'](.*?)["\']>$')
for line in file('docs/xml/chardet.xml'):
    m = docs_re.search(line)
    if m:
        docs_version = m.group(1)
        break
if not docs_version:
    sys.stderr.write('could not determine chardet docs version\n')
    sys.exit(1)

setup_re = re.compile(r'^\s*version\s*=\s*["\'](.*?)["\']\s*,\s*$')
for line in file('setup.py'):
    m = setup_re.search(line)
    if m:
        setup_version = m.group(1)
        break
if not setup_version:
    sys.stderr.write('could not determine setup.py version\n')
    sys.exit(1)
    
if makefile_version != chardet_version:
    sys.stderr.write('Makefile version = %s, but chardet/__init__.py version = %s\n' % (makefile_version, chardet_version))
    sys.exit(1)

if makefile_version != docs_version:
    sys.stderr.write('Makefile version = %s, but docs version = %s\n' % (makefile_version, docs_version))
    sys.exit(1)

if makefile_version != setup_version:
    sys.stderr.write('Makefile version = %s, but setup.py version = %s\n' % (makefile_version, setup_version))
    sys.exit(1)
    
if chardet_version != docs_version:
    sys.stderr.write('chardet/__init__.py version = %s, but docs version = %s\n' % (chardet_version, docs_version))
    sys.exit(1)

if chardet_version != setup_version:
    sys.stderr.write('chardet/__init__.py version = %s, but setup.py version = %s\n' % (chardet_version, setup_version))
    sys.exit(1)

if docs_version != setup_version:
    sys.stderr.write('docs version = %s, but setup.py version = %s\n' % (docs_version, setup_version))
    sys.exit(1)

date_re = re.compile(r'^<!ENTITY\s*fileversion\s*["\'](.*?)["\']>$')
for line in file('docs/xml/version.xml'):
    m = date_re.search(line)
    if m:
        docs_date = m.group(1)
if not docs_date:
    sys.stderr.write('could not determine chardet docs date\n')
    sys.exit(1)

todays_date = time.strftime('%Y-%m-%d')
if docs_date != todays_date:
    sys.stderr.write('docs date = %s but today is %s\n' % (docs_date, todays_date))
    sys.exit(1)
