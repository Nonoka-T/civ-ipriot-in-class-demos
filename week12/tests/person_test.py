import unittest
from src.person import Person

class PersonTest(unittest.TestCase):
    """
    This is a unit test.  Don't worry about it until week 15 unless you want to preread.
    I like writing tests so that I know my code works.
    I wrote this to make sure my code worked exactly as I hoped before showing it to you.
    I *could* have sat down and made sure, with pen and paper, that my code was logically
    correct in every way, but that would take five minutes, and writing these tests took
    two.
    Also, if I change my implementation and break something by accident, then these tests
    will start failing, and let me know.
    """
    def test_full_name_has_no_extraneous_spaces(self):
        preferred_name = "John"
        other_names = ["", "Smith"]
        expected = "John Smith"
        self.assertEqual(Person(preferred_name, other_names).full_name(), expected)

    def test_full_name_handles_reverse(self):
        preferred_name = "John"
        other_names = ["Chua"]
        expected = "Chua John"
        self.assertEqual(
            Person(preferred_name, other_names).full_name(reverse=True), expected
        )
