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

    def test_safeaccess(self):
        test_dict = {
            'root': {
                'children': [
                    {
                        'foo': 'bar'
                    }
                ]
            }
        }
        self.assertEqual(peb.safeaccess(test_dict, 'root.children.0.foo'), 'bar')
        self.assertIsNone(peb.safeaccess(test_dict, 'root.children.1'))
        self.assertEqual(peb.safeaccess(test_dict, 'root.children.first', 'nobar'), 'nobar')
        self.assertIsNone(peb.safeaccess(test_dict, 'root!.children().first'))
