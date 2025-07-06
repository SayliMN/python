from abc import ABC, abstractmethod


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

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        m3 = self.m3 - other.m3

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


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def restart(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Processing data...")

    def restart(self):
        print("Restarting in 3, 2, 1...")


class Whiteboard():
    def write(self):
        print("writing and not debugging")


class IPhone():
    def application(self, com):
        print("updating application...")
        com.process()


class Programmer:
    def work(self, com):
        print("debugging...")
        com.process()
        com.restart()


com1 = Laptop()
# com1.process()
# com1.restart()

iph1 = IPhone()
whi1 = Whiteboard()
prog1 = Programmer()

iph1.application(com1)


b = B(50, 34, 43)
b.show()

s1 = Student(50, 34, 43)
s2 = Student(97, 99, 96)
s1.show()

ss = Student(50,100, 99)
print(ss.sum(15,500))


s3 = s1 + s2
print(s3.m3)

sb = s1 - s2
print(sb.m3)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

