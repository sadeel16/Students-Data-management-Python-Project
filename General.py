class General:
    _finalSalary = 0
    numOfAcademic = 0
    numOfAdmin = 0
    numOfAll = 0
    numOfFullTime = 0
    numOfMale = 0
    numOfFemale = 0

    def __init__(self, ID, name, birthDate, maritalStatus, numOfChildren, gender, contactInfo, typeTime, status, department,
                 startingTime, basicSalary, healthInsurance):
        self._ID = ID
        self._name = name
        self._birthDate = birthDate
        self._maritalStatus = maritalStatus
        self._numOfChildren = numOfChildren
        # -------------
        if gender == "Female":
            General.numOfFemale = General.numOfFemale + 1
        elif gender == "Male":
            General.numOfMale = General.numOfMale + 1
        # -------------
        self._gender = gender
        self._contactInfo = contactInfo
        # -------------
        if typeTime == "Academic":
            General.numOfAcademic = General.numOfAcademic + 1
        elif typeTime == "Administrative":
            General.numOfAdmin = General.numOfAdmin + 1
        # -------------
        self._typeTime = typeTime
        # -------------
        if status == "Full-time":
            General.numOfFullTime = General.numOfFullTime + 1
        # -------------
        self._status = status
        self._department = department
        self._startingTime = startingTime
        self._basicSalary = basicSalary
        self._healthInsurance = healthInsurance
        General.numOfAll = General.numOfAll + 1

    def get_id(self):
        return self._ID

    def get_name(self):
        return self._name

    def get_birth_date(self):
        return self._birthDate

    def get_marital_status(self):
        return self._maritalStatus

    def get_num_of_children(self):
        return self._numOfChildren

    def get_gender(self):
        return self._gender

    def get_contact_info(self):
        return self._contactInfo

    def get_type(self):
        return self._typeTime

    def get_status(self):
        return self._status

    def get_department(self):
        return self._department

    def get_starting_time(self):
        return self._startingTime

    def get_basic_salary(self):
        return self._basicSalary

    def get_health_insurance(self):
        return self._healthInsurance

    def get_final_salary(self):
        return self._finalSalary

    def set_id(self, id):
        self._ID = id

    def set_name(self, name):
        self._name = name

    def set_birth_date(self, birthDate):
        self._birthDate = birthDate

    def set_marital_status(self, maritalStatus):
        self._maritalStatus = maritalStatus

    def set_num_of_children(self, numOfChildren):
        self._numOfChildren = numOfChildren

    def set_gender(self, gender):
        self._gender = gender

    def set_contact_info(self, contactInfo):
        self._contactInfo = contactInfo

    def set_type(self, typeTime):
        self._typeTime = typeTime

    def set_status(self, status):
        self._status = status

    def set_department(self, department):
        self._department = department

    def set_starting_time(self, startingTime):
        self._startingTime = startingTime

    def set_basic_salary(self, basicSalary):
        self._basicSalary = basicSalary

    def set_health_insurance(self, healthInsurance):
        self._healthInsurance = healthInsurance

    def set_final_salary(self, finalSalary):
        self._finalSalary = finalSalary