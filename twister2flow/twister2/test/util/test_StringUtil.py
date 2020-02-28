import unittest
from unittest import TestCase
from twister2flow.twister2.util.StringUtil import StringUtil


class TestStringUtil(TestCase):
    def test_get_words(self):
        words = StringUtil.get_words("mpirun -n 4", " ")
        self.assertEqual(words, ["mpirun", "-n", "4"])


