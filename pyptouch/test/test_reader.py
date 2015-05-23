#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyptouch
----------------------------------

Tests for `pyptouch` module.
"""

from __future__ import print_function

import os
import unittest

from pyptouch.reader import PTReader

testdir = os.path.dirname(__file__)


class TestPTReader(unittest.TestCase):

    def setUp(self):  # NOQA
        self.ptr = PTReader(os.path.join(testdir, "python.ptouch"))

    def test_read(self):
        self.ptr.read()

    def tearDown(self):  # NOQA
        pass

if __name__ == '__main__':
    unittest.main()
