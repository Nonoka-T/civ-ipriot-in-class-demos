from person import Person

class Lecturer(Person):
    def __init__(self, preferred_name="", other_names=None, capabilities=None):
        super().__init__(preferred_name, other_names)
        self.capabilities = capabilities or []
        self.students = []

    def list_capabilities(self):
        return f"{self.full_name()} is able to teach {", ".join(self.capabilities)}"

    def add_student(self, student):
        self.students.append(student)

    def student_full_names(self):
        return [student.full_name() for student in self.students]

    def list_all_students(self):
        if len(self.students) < 1:
            return f"{self.full_name()} does not have any students at the moment."
        return f"{self.full_name()} is teaching the following students:\n {"\n".join(self.student_full_names())}"