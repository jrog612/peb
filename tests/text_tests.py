import random
from unittest import TestCase

import peb

random_words = ['glue', 'stimulation', 'soft', 'medium', 'teach', 'broadcast', 'quota', 'shell', 'enter', 'honest',
                'orbit', 'initiative', 'agile', 'hell', 'sweat', 'sensation', 'hour', 'resign', 'absence',
                'entitlement', 'van', 'remember', 'beer', 'disk', 'school', 'subject', 'short', 'bar', 'scenario',
                'compound', 'chip', 'warn', 'unlawful', 'ignorant', 'south', 'decade', 'inappropriate',
                'retailer', 'dorm', 'participate', 'hostile', 'elaborate', 'bell', 'cemetery', 'ample', 'pity', 'bring',
                'disaster', 'shorts', 'coerce']


class TextTest(TestCase):
    def get_random_words(self, count):
        return random.choices(random_words, k=count)

    def test_s2c_and_c2s(self):
        for _ in range(40):
            words = self.get_random_words(random.randint(5, 10))
            snake_case_text = '_'.join(words)
            camel_case_text = words[0] + ''.join(x.title() for x in words[1:])
            self.assertEqual(peb.snake_to_camel(snake_case_text), camel_case_text)
            self.assertEqual(peb.camel_to_snake(camel_case_text), snake_case_text)

    def test_truncate(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pharetra libero ligula. Fusce eu semper massa. Quisque faucibus posuere porta. In at eleifend mauris. Integer orci quam, tempus sagittis odio eget, congue dignissim magna. Ut in nulla eu neque gravida dictum."
        suffixes = ['...', '~~~', '!!!', '@@@', '###', '$$$', '%%%', '^^^', '&&&', '***']
        for _ in range(30):
            tnum = random.randint(10, 100)
            suffix = random.choice(suffixes)
            self.assertEqual(
                peb.truncate(text, tnum, suffix),
                text[:tnum] + suffix
            )
