class students:
    roll : ''
    gpa : ''

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, Gpa : {self.gpa}")

shibu = students(101, 2.71)
shibu.display()


ahsan = students(102, 2.72)
ahsan.display()
