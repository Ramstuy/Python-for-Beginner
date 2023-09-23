from inheritance19pt2 import Student
# mengimport class Student dari file lain
class Person(Student):
    # memanggil class file lain kedalam parameter Person
    pass

p1 = Person()
print(p1.name)
print(p1.age)
