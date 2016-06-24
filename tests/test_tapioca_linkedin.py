# coding: utf-8

import unittest

from tapioca_linkedin import Linkedin


class TestTapiocaLinkedin(unittest.TestCase):

    def setUp(self):
        self.wrapper = Linkedin()


if __name__ == '__main__':
    unittest.main()
