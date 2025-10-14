"""
    This is our Person base class.

    It is very simple because we do not need much from it.
    It is also very simple because we do not need too much 'common functionality'.

    This person has the ability to print their full name.

"""

class Person():
    """
     This example is really contrived.
     > 90% of software I've worked with has presumed that everyone has at
     least one first name and one surname, but that isn't always true.

     If you don't mind leaving people out, first_name, last_name is fine.
     If you need to serve an entire population, try thinking about what
     parts of a name you really need, and how you would present it.

     The contrived part of this example is how permissive I am about the
     name data.
    """

    def __init__(self, preferred_name="", other_names=None):
        self.preferred_name = preferred_name
        # For your interest: why have I used my default argument to last name like this?
        self.other_names = other_names or []

    def full_name(self, reverse=False):
        """
        Outputs a person's full name.
        :param reverse(bool): Specifies whether the name should be reversed
        """
        if reverse:
            name_list = self.other_names.reverse() + [self.preferred_name]
        else:
            name_list = [self.preferred_name] + self.other_names

        """
        This is a list comprehension: it's very "Pythonic"
        Other languages might write this as something like
          name_array.select((name) -> name.present?)
        I'm basically trying to kick out 'blanks' from my list.
        """
        name_list = [name for name in name_list if name]

        return " ".join(name_list)
