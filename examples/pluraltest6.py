'''Unit test for plural6.py'''

import plural6
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
            self.assertEqual(plural6.plural(singular), plural)

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
            self.assertEqual(plural6.plural(singular), plural)

    def test_y(self):
        'words ending in Y'
        nouns = {
            'utility': 'utilities',
            'vacancy': 'vacancies',
            'boy': 'boys',
            'day': 'days'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ouce(self):
        'words ending in OUSE'
        nouns = {
             'mouse': 'mice',
             'louse': 'lice'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_child(self):
        'special case: child'
        nouns = {
             'child': 'children'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_oot(self):
        'special case: foot'
        nouns = {
             'foot': 'feet'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ooth(self):
        'words ending in OOTH'
        nouns = {
             'booth': 'booths',
             'tooth': 'teeth'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_f_ves(self):
        'words ending in F that become VES'
        nouns = {
             'leaf': 'leaves',
             'loaf': 'loaves'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_sis(self):
        'words ending in SIS'
        nouns = {
             'thesis': 'theses'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_man(self):
        'words ending in MAN'
        nouns = {
             'man': 'men',
             'mailman': 'mailmen',
             'human': 'humans',
             'roman': 'romans'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ife(self):
        'words ending in IFE'
        nouns = {
             'knife': 'knives',
             'wife': 'wives',
             'lowlife': 'lowlifes'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_eau(self):
        'words ending in EAU'
        nouns = {
             'tableau': 'tableaux'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_elf(self):
        'words ending in ELF'
        nouns = {
             'elf': 'elves',
             'shelf': 'shelves',
             'delf': 'delfs',
             'pelf': 'pelfs'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_same(self):
        'words that are their own plural'
        nouns = {
             'sheep': 'sheep',
             'deer': 'deer',
             'fish': 'fish',
             'moose': 'moose',
             'aircraft': 'aircraft',
             'series': 'series',
             'haiku': 'haiku'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_default(self):
        'unexceptional words'
        nouns = {
            'papaya': 'papayas',
            'whip': 'whips',
            'palimpsest': 'palimpsests'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)
        
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
