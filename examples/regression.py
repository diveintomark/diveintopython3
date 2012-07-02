#!/usr/bin/python3

import unittest
import os
import glob

def regressionTest():
    filenames = glob.glob('*test*.py')
    module_names = [os.path.splitext(os.path.basename(f))[0] for f in filenames]
    modules = [__import__(name) for name in module_names]
    tests = [unittest.defaultTestLoader.loadTestsFromModule(m) for m in modules]
    return unittest.TestSuite(tests)

if __name__ == '__main__':
    unittest.main(defaultTest='regressionTest')