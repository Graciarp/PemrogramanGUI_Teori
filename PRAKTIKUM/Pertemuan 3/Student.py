#   import data pada class Person
from Person import Person

#   Deklarasi class
class Student(Person) :
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
