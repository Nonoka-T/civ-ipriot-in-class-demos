from lecturer import Lecturer

para = Lecturer("Para", capabilities=["python", "javascript", "sql"])
someone_else = Lecturer("Mystery", ["Lecturer"], capabilities=["c#", "iot", "sql"])

lecturers = [para, someone_else]

for lecturer in lecturers:
    print(lecturer.list_capabilities())
    print(lecturer.list_all_students())