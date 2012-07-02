from alphametics import solve
import unittest

class KnownValues(unittest.TestCase):
    def test_out(self):
        '''TO + GO == OUT'''
        self.assertEqual(solve('TO + GO == OUT'), '21 + 81 == 102')

    def test_too(self):
        '''I + DID == TOO'''
        self.assertEqual(solve('I + DID == TOO'), '9 + 191 == 200')

    def test_mom(self):
        '''AS + A == MOM'''
        self.assertEqual(solve('AS + A == MOM'), '92 + 9 == 101')

    def test_best(self):
        '''HES + THE == BEST'''
        self.assertEqual(solve('HES + THE == BEST'), '426 + 842 == 1268')

    def test_late(self):
        '''NO + NO + TOO == LATE'''
        self.assertEqual(solve('NO + NO + TOO == LATE'), '74 + 74 + 944 == 1092')

    def test_onze(self):
        '''UN + UN + NEUF == ONZE'''
        self.assertEqual(solve('UN + UN + NEUF == ONZE'), '81 + 81 + 1987 == 2149')

    def test_deux(self):
        '''UN + DEUX + DEUX + DEUX + DEUX == NEUF'''
        self.assertEqual(solve('UN + DEUX + DEUX + DEUX + DEUX == NEUF'), '25 + 1326 + 1326 + 1326 + 1326 == 5329')

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
