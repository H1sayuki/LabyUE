class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        # obliczamy średnią ocen
        avg = sum(self.marks) / len(self.marks)
        return avg > 50


student1 = student("Anna", [60, 70, 80])
student2 = student("Piotr", [30, 40, 50])

print(student1.name, "passed?", student1.is_passed())
print(student2.name, "passed?", student2.is_passed())
