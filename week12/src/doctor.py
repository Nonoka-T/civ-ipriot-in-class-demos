from person import Person

class Doctor(Person):
    def __init__(self, personal_name):
        super().__init__(personal_name, title="Dr")
        self.patients = []

    def introduce(self):
        print(f"Hello, I am {self.full_name()}.")

    def add_patient_to_queue(self, patient_name):
        self.patients.append(patient_name)

    def see_patient(self):
        # Pop raises an IndexError if the patients is empty
        # Here, we protect our code from an exception pro-actively.
        if not self.patients:
            return None
        return self.patients.pop(0)