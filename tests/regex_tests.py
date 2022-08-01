from unittest import TestCase

import peb


class RegexTest(TestCase):
    def test_is_url(self):
        test_cases = [
            ('http://google.com', True),
            ('https://www.google.com/search?q=peb+test&source=hp', True),
            ('htts://google.com', False),
            ('https://abs.co.kr', True),
            ('https://n.news.naver.com/article/000/123456789?sid=000&cds=news_media_pc', True),
            ('files:///users/root/test.pdf', False),
            ('http://!@#532@#.com', False),
            ('this.is.not.url', False),
            ('this is not url', False),
        ]

        for case in test_cases:
            self.assertEqual(peb.is_url(case[0]), case[1])

    def test_is_email(self):
        test_cases = [
            ('test@test.com', True),
            ('abs@test.co.kr', True),
            ('notemail.com', False),
            ('notemail@.com', False),
            ('@test.com', False),
            ('1234423221@test.com', True),
            ('!#%%#$@test.com', False),
            ('test@test.', False),
        ]

        for case in test_cases:
            self.assertEqual(peb.is_email(case[0]), case[1])

    def test_get_file_extension(self):
        test_cases = [
            ('testfile', None),
            ('test.file', 'file'),
            ('test.file.pdf', 'pdf'),
            ('test.file.pdf.jpg', 'jpg'),
            ('https://test.com/file.pdf', 'pdf'),
        ]

        for case in test_cases:
            self.assertEqual(peb.get_file_extension(case[0]), case[1])
