import random
from unittest import TestCase

import peb
from peb import wrap_list, deep_update


class IterationTest(TestCase):
    def setUp(self):
        pass

    def test_wrap_list(self):
        self.assertEqual(wrap_list('test'), ['test'])
        self.assertEqual(wrap_list(['test']), ['test'])
        self.assertEqual(wrap_list(1), [1])
        self.assertEqual(wrap_list([1]), [1])

    def test_chunk_iter(self):
        size = 1000
        max_value = random.randint(100000, 1000000)

        divided, remain = divmod(max_value, size)
        count = 0
        for chunk in peb.chunk_iter(range(1, max_value), size):
            count += 1
            is_last = divided + 1 == count

            if remain > 0 and is_last:
                self.assertLess(len(chunk), size)
            else:
                self.assertEqual(len(chunk), size)
            self.assertEqual(chunk[0], (size * (count - 1)) + 1)

            if is_last:
                self.assertEqual(chunk[-1], max_value - 1)  # range not contain last value

    def test_isiter(self):
        self.assertTrue(peb.isiter([1, 2, 3]))
        self.assertTrue(peb.isiter((1, 2, 3)))
        self.assertTrue(peb.isiter([]))
        self.assertTrue(peb.isiter(()))
        self.assertTrue(peb.isiter({1: 1, 2: 2}))
        self.assertTrue(peb.isiter({}))
        self.assertTrue(peb.isiter({1, 2, 3}))
        self.assertTrue(peb.isiter([_ for _ in range(1, 100)]))

        self.assertFalse(peb.isiter({1: 1, 2: 2}, allow_dict=False))
        self.assertFalse(peb.isiter('1234'))
        self.assertFalse(peb.isiter(''))
        self.assertFalse(peb.isiter(1234))
        self.assertFalse(peb.isiter(None))
        self.assertFalse(peb.isiter(True))
        self.assertFalse(peb.isiter(False))
        self.assertFalse(peb.isiter(0.1234))
        self.assertFalse(peb.isiter(0))
        self.assertFalse(peb.isiter(1 + 2j))

    def test_deep_update(self):
        source_dict = {
            'test': 'test',
            'deep': {
                1: 2,
                None: 'None',
                'test': 'test',
                '2deep': {
                    'test': 'test',
                    'keep': 'keep'
                },
                'keep': 'keep'
            },
            'keep': 'keep'
        }
        update_dict = {
            'test': 'updated',
            'deep': {
                1: 3,
                None: 'updated',
                'test': 'updated',
                '2deep': {
                    'test': 'updated',
                },
            },
        }

        expect_dict = {
            'test': 'updated',
            'deep': {
                1: 3,
                None: 'updated',
                'test': 'updated',
                '2deep': {
                    'test': 'updated',
                    'keep': 'keep'
                },
                'keep': 'keep'
            },
            'keep': 'keep'
        }

        result = deep_update(source_dict, update_dict)
        self.assertEqual(expect_dict, result)
