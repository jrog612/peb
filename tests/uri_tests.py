from unittest import TestCase

import peb


class UriTest(TestCase):
    def test_path_join(self):
        def testing(p1, p2, expect):
            self.assertEqual(peb.join_path(p1, p2), expect)

        testing('foo', '/var', 'foo/var')
        testing('foo/', 'var', 'foo/var')
        testing('https://test.com/', '/test/path', 'https://test.com/test/path')
        testing('foo/path', 'var/path', 'foo/path/var/path')
