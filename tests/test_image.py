#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module contains a object that represents Tests for Image"""

import unittest
import os
import sys
import datetime

sys.path.append('.')

from greenart.image import Image


class ImageTest(unittest.TestCase):
    """This object represents Tests for Image."""

    def test_get_commands(self):
        """Test Image.get_commands method"""
        cwd = os.path.dirname(os.path.abspath(__file__))
        im = Image(os.path.join(cwd, 'fixtures/greenart.png'))
        act = im.get_commands()
        self.assertIsNotNone(act)

    def test_get_days_ago_when_was_first_sunday(self):
        """Test Image._get_days_ago_when_was_first_sunday method"""
        exp = 365 + datetime.datetime.now().weekday()
        self.assertEqual(Image._get_days_ago_when_was_first_sunday(), exp)

    def test_get_commit_from_past(self):
        """Test Image._get_commit_from_past method"""
        exp = r'^git commit -m([^-]+)--date "(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+).(\d+)"$'
        self.assertRegex(Image._get_commit_from_past(1), exp)

    def test_get_github_color_from_grey(self):
        """Test Image._get_github_color_from_grey method"""
        self.assertEqual(Image._get_github_color_from_grey(50), 7)
        self.assertEqual(Image._get_github_color_from_grey(100), 5)
        self.assertEqual(Image._get_github_color_from_grey(150), 3)
        self.assertEqual(Image._get_github_color_from_grey(200), 1)
        self.assertEqual(Image._get_github_color_from_grey(255), 0)


if __name__ == '__main__':
    unittest.main()
