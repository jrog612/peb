import random
from unittest import TestCase

import peb


class UtilTest(TestCase):
    def test_raise_or(self):
        error = ValueError('Test error')
        value = 'TEST_VALUE'

        self.assertEqual(peb.raise_or(error, value, throw=False), value)

        with self.assertRaises(ValueError) as res:
            peb.raise_or(error, value, throw=True)
            self.assertEqual(res.exception, error)

