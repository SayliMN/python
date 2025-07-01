class Student:
    school = "ABC High"  # static variable

    def __init__(self, name, rollno, m1, m2, m3):  # constructor
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.book = self.Books()

    def avg(self):  # instance method --> works with objects, used with instance vars
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):  # class method --> works with class variables
        return cls.school

    @staticmethod
    def info():  # static method --> nothing to do with class or object
        print("This school is founded in 1934")

    def show(self):
        print(self.name, self.rollno, self.m1, self.m2, self.m3, self.avg())
        self.book.show()

    class Books:
        def __init__(self):
            self.genre = "Sci-fi"
            self.nums = "100"
            self.color = "multi"

        def show(self):
            print(self.genre, self.nums, self.color)


s1 = Student('Jay',1,45,60,55)
s2 = Student('Lata',2,70,96,100)

print(Student.getSchool())
print(Student.info())
s1.show()
s2.show()