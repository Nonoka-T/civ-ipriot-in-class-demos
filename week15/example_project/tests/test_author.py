from author import Author
from unittest import TestCase

class TestAuthor(TestCase):
    def test_blank_name_rejected(self):
        original_name = "Martha Wells"
        test_author = Author(original_name)
        self.assertEqual(test_author.name, original_name)
        test_author.name = ""
        self.assertEqual(test_author.name, original_name)

    def test_filled_name_accepted(self):
        original_name = "David Barnes"
        test_author = Author(original_name)
        self.assertEqual(test_author.name, original_name)
        test_author.name = "Michael Kolling"
        self.assertEqual(test_author.name, "Michael Kolling")

