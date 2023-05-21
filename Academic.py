from General import *


class Academic(General):

    def __init__(self, ID, name, birthDate, maritalStatus, numOfChildren, gender, contactInfo, typeTime, status,
                 department,
                 startingTime, basicSalary, healthInsurance):
        super().__init__(ID, name, birthDate, maritalStatus, numOfChildren, gender, contactInfo, typeTime, status,
                         department,
                         startingTime, basicSalary, healthInsurance)
        self.__experience = {}

    def add_expireence(self, year, semester, listOfCourses):
        yearsemester: str = year + "-" + semester
        self.__experience[yearsemester] = listOfCourses

    def get_experience(self):
        return self.__experience
