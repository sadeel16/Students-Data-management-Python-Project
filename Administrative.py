from General import *


class Administrative(General):

    def __init__(self, ID, name, birthDate, maritalStatus, numOfChildren, gender, contactInfo, typeTime, status,
                 department,
                 startingTime, basicSalary, healthInsurance):
        super().__init__(ID, name, birthDate, maritalStatus, numOfChildren, gender, contactInfo, typeTime, status,
                         department,
                         startingTime, basicSalary, healthInsurance)
        self.__vacation = {}

    def add_vacation_days(self, year, numberOfVacDays):
        self.__vacation[year] = numberOfVacDays

    def get_vacation(self):
        return self.__vacation

