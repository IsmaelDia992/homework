class Student:
    def __init__(self, id, name, email): 
        self.id = id
        self.name = name
        self.email = email

    def print_details(self):
        return 'Id: {}, Name: {}, Email:{}'.format(self.id, self.name, self.email)


student_1 = Student("xnct0258","John Smith", "johnsmith@leeds.ac.uk")
print("Student 1's name:", student_1.name)
student_2 = Student("jytbuwqr","Varia Costantine", "v.constantine@leeds.ac.uk")
print("Student 2's email:", student_2.email)
