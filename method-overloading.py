class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = self.m3 + other.m3

        s3 = Student(m1, m2, m3)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2 + self.m3
        r2 = other.m1 + other.m2 + other.m3

        if r1 > r2:
            return True
        else:
            return False
    def show(self):
        print("Hello there!")

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s

class B(Student):
    def show(self):
        print("Hello there TWICE!!")


b = B(50, 34, 43)
b.show()

s1 = Student(50, 34, 43)
s2 = Student(97, 99, 96)
ss = Student(50,100, 99)
# s1.show()
print(ss.sum(15,500))


s3 = s1 + s2
print(s3.m3)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

