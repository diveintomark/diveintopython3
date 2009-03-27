"""Unit test for plural2.py

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/03/17 14:34:40 $"
__copyright__ = "Copyright (c) 2004 Mark Pilgrim"
__license__ = "Python"

from plural2 import plural
import unittest, new

class KnownValues(unittest.TestCase):
    nouns = {'bass': 'basses',
             'bus': 'buses',
             'walrus': 'walruses',
             'box': 'boxes',
             'fax': 'faxes',
             'suffix': 'suffixes',
             'mailbox': 'mailboxes',
             'buzz': 'buzzes',
             'waltz': 'waltzes',
             'coach': 'coaches',
             'glitch': 'glitches',
             'rash': 'rashes',
             'watch': 'watches',
             'cheetah': 'cheetahs',
             'cough': 'coughs',
             'utility': 'utilities',
             'vacancy': 'vacancies',
             'boy': 'boys',
             'day': 'days',
             'computer': 'computers',
             'rock': 'rocks',
             'paper': 'papers',
             }

for noun, pluralnoun in KnownValues.nouns.items():
    func = lambda self, noun=noun, pluralnoun=pluralnoun: \
           KnownValues.failUnlessEqual(self, plural(noun), pluralnoun)
    func.__doc__ = "%s --> %s" % (noun, pluralnoun)
    instanceMethod = new.instancemethod(func, None, KnownValues)
    setattr(KnownValues, "test_%s" % noun, instanceMethod)

if __name__ == "__main__":
    unittest.main()

# Copyright (c) 2009, Mark Pilgrim, All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
