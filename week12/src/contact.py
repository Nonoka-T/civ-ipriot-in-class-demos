from person import Person
# import person
# person.Person()

class Contact(Person):
    def __init__(self, personal_name, phone_number):
        super().__init__(personal_name)
        self.phone_number = phone_number

