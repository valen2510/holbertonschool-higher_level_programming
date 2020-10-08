#!/usr/bin/python3
"""Class Student
"""


class Student:
    """Define class Student
    """
    def __init__(self, first_name, last_name, age):
        """Initialisation of public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method to retrieve a dictionary representation
            of a student instance
        """
        if attrs is not None:
            dict_student = {}
            for k in vars(self):
                if k in attrs:
                    dict_student[k] = vars(self)[k]
            return dict_student
        else:
            return vars(self)
