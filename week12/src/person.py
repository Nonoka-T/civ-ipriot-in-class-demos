"""
    This is our Person base class.

    It is very simple because we do not need much from it.
    It is also very simple because we do not need too much 'common functionality'.

    This person has the ability to print their full name.

"""

class Person():
    def __init__(self, personal_name="", title=""):
        self.personal_name = personal_name
        self.title = title

    def full_name(self):
        if self.title:
            return f"{self.title} {self.personal_name}"
        return self.personal_name
