import random
from unittest import TestCase

import peb


class NumberTest(TestCase):
    def setUp(self):
        pass

    def test_percent_to_num(self):
        for _ in range(5000):
            whole = random.randint(1, 9999999)
            percent = random.randint(1, 100)
            num = peb.percent_to_num(whole, percent)
            expect = whole * percent / 100
            self.assertEqual(num, expect)

    def test_num_to_percent(self):
        for _ in range(5000):
            whole = random.randint(1, 9999999)
            part = random.randint(1, whole)
            percent = peb.num_to_percent(part, whole)
            expect = part * 100 / whole
            self.assertEqual(percent, expect)
