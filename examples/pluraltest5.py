'''Unit test for plural5.py'''

import plural5
import unittest

class KnownValues(unittest.TestCase):
    def test_sxz(self):
        'words ending in S, X, and Z'
        nouns = {
            'bass': 'basses',
            'bus': 'buses',
            'walrus': 'walruses',
            'box': 'boxes',
            'fax': 'faxes',
            'suffix': 'suffixes',
            'mailbox': 'mailboxes',
            'buzz': 'buzzes',
            'waltz': 'waltzes'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural5.plural(singular), plural)

    def test_h(self):
        'words ending in H'
        nouns = {
            'coach': 'coaches',
            'glitch': 'glitches',
            'rash': 'rashes',
            'watch': 'watches',
            'cheetah': 'cheetahs',
            'cough': 'coughs'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural5.plural(singular), plural)

    def test_y(self):
        'words ending in Y'
        nouns = {
            'utility': 'utilities',
            'vacancy': 'vacancies',
            'boy': 'boys',
            'day': 'days'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural5.plural(singular), plural)

    def test_default(self):
        'unexceptional words'
        nouns = {
            'papaya': 'papayas',
            'whip': 'whips',
            'palimpsest': 'palimpsests'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural5.plural(singular), plural)
        
if __name__ == '__main__':
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
