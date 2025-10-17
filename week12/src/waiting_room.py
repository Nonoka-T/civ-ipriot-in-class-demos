from doctor import Doctor


doctor = Doctor("Shah")
doctor.introduce()

doctor.add_patient_to_queue("Sarah")
print(doctor.patients)
# # now patients is ["Sarah"]
doctor.add_patient_to_queue("Diego")
print(doctor.patients)
# # now patients is ["Sarah", "Diego"]
doctor.see_patient()
print(doctor.patients)

doctor.see_patient()
print(doctor.patients)

doctor.see_patient()
print(doctor.patients)
# # now patients is ["Diego"]
# # And "Sarah" is output to the console