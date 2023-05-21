from Academic import *
from Administrative import *
from datetime import date

# Reading info from general attributes file--------------------------------------------

print("Please enter general attributes file name")
fileName = input()
employees = []

try:
    f = open(fileName, "r")
except IOError:
    print("Error: can\'t find file or read data")
    exit(0)
else:
    lines = []
    for i in f:
        lines.append(i.strip())

    sent = []
    for line in lines:
        sent.append(line.split("; "))

    for s in sent:
        id = int(s[0].strip())
        if id < 0 or id >= 100000:
            print("adding this employee", id, "got skipped, because the id is not valid as 5 digits")
            continue

        name = s[1].split(",")

        birthDate = s[2].strip().split("/")

        maritalStatus = s[3].strip()
        if maritalStatus != "Maried" and maritalStatus != "Single":
            print("adding this employee", id, "got skipped, because the marital status is neither single nor married")
            continue

        numOfChilds = int(s[4].strip())

        gender = s[5].strip()
        if gender != "Male" and gender != "Female":
            print("adding this employee", id, "got skipped, because the gender is neither male nor female")
            continue

        contactInfo = s[6].split(",")

        typeTime = s[7].strip()
        if typeTime != "Administrative" and typeTime != "Academic":
            print("adding this employee", id, "got skipped, because the type is neither Administrative nor Academic")
            continue

        status = s[8].strip()
        if status != "Part-time" and status != "Full-time" and status != "Left-university":
            print("adding this employee", id, "got skipped, because of the wrong status value")
            continue

        department = s[9].strip()

        startingTime = s[10].strip().split("/")

        basicSalary = int(s[11].strip())

        healthInsurance = s[12].strip()
        if healthInsurance != "true" and healthInsurance != "false":
            print("adding this employee", id,
                  "got skipped, because the health insurance status is neither false nor true")
            continue

        if typeTime == "Administrative":
            admin = Administrative(id, name, birthDate, maritalStatus, numOfChilds, gender, contactInfo, typeTime,
                                   status, department, startingTime, basicSalary, healthInsurance)
            employees.append(admin)
        else:
            acadimi = Academic(id, name, birthDate, maritalStatus, numOfChilds, gender, contactInfo, typeTime, status,
                               department, startingTime, basicSalary, healthInsurance)
            employees.append(acadimi)

# Reading administrative file---------------------------------------------------

print("Please enter Administrative attributes file name")
fileName2 = input()

try:
    f = open(fileName2, "r")
except IOError:
    print("Error: can\'t find Administrative.txt file or read data")
    exit(0)
else:
    lines2 = []
    for i in f:
        lines2.append(i.strip())

    sent2 = []
    for line in lines2:
        sent2.append(line.split("; "))

    for word in sent2:
        id = word[0]
        semester = word[1]
        vacationDays = word[2]
        for employee in employees:
            if int(id) == employee.get_id():
                if employee.get_type() == "Administrative":
                    employee.add_vacation_days(semester, vacationDays)
                    break
                else:
                    continue

# Reading academic file----------------------------------------------------

print("Please enter Academic attributes file name")
fileName3 = input()

try:
    f = open(fileName3, "r")
except IOError:
    print("Error: can\'t find Academic.txt file or read data")
    exit(0)
else:
    lines3 = []
    for i in f:
        lines3.append(i.strip())

    sent3 = []
    for line in lines3:
        sent3.append(line.split("; "))

    for word in sent3:
        for employee in employees:
            if int(word[0]) == employee.get_id():
                if employee.get_type() == "Academic":
                    courses = word[3].split(" ")
                    employee.add_expireence(word[2], word[1], courses)
                else:
                    continue

# Functions section-------------------------------------------------------

def add_new_employee():
    flagId = 0
    print("Please enter the employee's id")
    id = int(input())
    while id < 0 or id >= 100000:
        print("Please re-enter the id with 5 digits")
        id = int(input())

    for employee in employees:
        if id == employee.get_id():
            flagId = 1

    if flagId == 1:
        print("This id already exists, couldn't add employee")
        return 0
    else:
        print()
        print("Please enter the employee's name (FirstName MiddleName LastName)")
        name = input().capitalize().split(" ")

        print()
        print("Please enter the employee's birthdate in dd/mm/yyyy order")
        date = input().split("/")

        print()
        print("Please enter the employee's marital status")
        maritalStatus = input().capitalize()
        while maritalStatus != "Maried" and maritalStatus != "Single":
            print("Please re-enter the marital status")
            maritalStatus = input()

        print()
        print("Please enter the employee's number of children")
        numOfChilds = int(input())

        print()
        print("Please enter the employee's gender type")
        gender = input().capitalize()
        while gender != "Female" and gender != "Male":
            print("Please re-enter the gender type")
            gender = input().capitalize()

        print()
        contactInfo = []
        print("Please enter the employee's email address")
        email = input()
        contactInfo.append(email)
        print("Please enter the employee's mobile number")
        mobile = input()
        contactInfo.append(mobile)
        print("Please enter the employee's fax")
        fax = input()
        contactInfo.append(fax)

        print()
        print("Please enter the employee's type (Administrative or Academic)")
        typeTime = input().capitalize()
        while typeTime != "Administrative" and typeTime != "Academic":
            print("Please re-enter the type")
            typeTime = input().capitalize()

        print()
        print("Please enter the employee's status (Part-time, Full-time, Left-university)")
        status = input().capitalize()
        while status != "Part-time" and status != "Full-time" and status != "Left-university":
            print("Please re-enter the status")
            status = input().capitalize()

        print()
        print("Please enter the employee's department")
        department = input().capitalize()

        print()
        print("Please enter the employee's starting time in mm/yyyy order")
        startingTime = input().split("/")

        print()
        print("Please enter the employee's basic salary")
        basicSalary = int(input())

        print()
        print("Please enter the employee's health insurance status (true, false)")
        healthInsurance = input()
        while healthInsurance != "true" and healthInsurance != "false":
            print("Please re-enter the health insurance status")
            healthInsurance = input()

        if typeTime == "Administrative":
            admin = Administrative(id, name, date, maritalStatus, numOfChilds, gender, contactInfo, typeTime, status,
                                   department, startingTime, basicSalary, healthInsurance)
            employees.append(admin)
        else:
            acadimi = Academic(id, name, date, maritalStatus, numOfChilds, gender, contactInfo, typeTime, status,
                               department, startingTime, basicSalary, healthInsurance)
            employees.append(acadimi)

        return 1


def update_general_attributes():
    flagId = 0
    print("Please enter the employee's id")
    id = int(input())

    for employee in employees:
        if id == employee.get_id():
            flagId = 1
            print()
            print("Do you want to change employee's name? (yes, no)")
            idChoice = input()
            if idChoice == "yes":
                print("Please enter the new name (FirstName MiddleName LastName)")
                name = input().capitalize().split(" ")
                employee.set_name(name)

            print()
            print("Do you want to change employee's birthdate? (yes, no)")
            birthChoice = input()
            if birthChoice == "yes":
                print("Please enter the new employee's birthdate in dd/mm/yyyy order")
                date = input().split("/")
                employee.set_birth_date(date)

            print()
            print("Do you want to change employee's marital status? (yes, no)")
            maritalChoice = input()
            if maritalChoice == "yes":
                print("Please enter the new employee's marital status")
                maritalStatus = input().capitalize()
                while maritalStatus != "Maried" and maritalStatus != "Single":
                    print("Please re-enter the marital status")
                    maritalStatus = input()
                employee.set_marital_status(maritalStatus)

            print()
            print("Do you want to change employee's number of children? (yes, no)")
            childrenChoice = input()
            if childrenChoice == "yes":
                print("Please enter the new employee's number of children")
                numOfChilds = int(input())
                employee.set_num_of_children(numOfChilds)

            print()
            print("Do you want to change employee's gender type? (yes, no)")
            genderChoice = input()
            if genderChoice == "yes":
                print("Please enter the new employee's gender type")
                gender = input().capitalize()
                while gender != "Female" and gender != "Male":
                    print("Please re-enter the gender type")
                    gender = input().capitalize()
                employee.set_gender(gender)

            print()
            print("Do you want to change employee's contact info? (yes, no)")
            contactChoice = input()
            if contactChoice == "yes":
                contactInfo = []
                print("Please enter new the employee's email address")
                email = input()
                contactInfo.append(email)
                print("Please enter new the employee's mobile number")
                mobile = input()
                contactInfo.append(mobile)
                print("Please enter new the employee's fax")
                fax = input()
                contactInfo.append(fax)
                employee.set_contact_info(contactInfo)

            print()
            print("Do you want to change employee's type? (yes, no)")
            typeChoice = input()
            if typeChoice == "yes":
                print("Please enter the new employee's type (Administrative or Academic)")
                typeTime = input().capitalize()
                while typeTime != "Administrative" and typeTime != "Academic":
                    print("Please re-enter the type")
                    typeTime = input().capitalize()
                employee.set_type(typeTime)

            print()
            print("Do you want to change employee's status? (yes, no)")
            statusChoice = input()
            if statusChoice == "yes":
                print("Please enter the new employee's status (Part-time, Full-time, Left-university)")
                status = input().capitalize()
                while status != "Part-time" and status != "Full-time" and status != "Left-university":
                    print("Please re-enter the status")
                    status = input().capitalize()
                employee.set_status(status)

            print()
            print("Do you want to change employee's department? (yes, no)")
            depChoice = input()
            if depChoice == "yes":
                print("Please enter the new employee's department")
                department = input().capitalize()
                employee.set_department(department)

            print()
            print("Do you want to change employee's starting time? (yes, no)")
            startChoice = input()
            if startChoice == "yes":
                print("Please enter the new employee's starting time in mm/yyyy order")
                startingTime = input().split("/")
                employee.set_starting_time(startingTime)

            print()
            print("Do you want to change employee's basic salary? (yes, no)")
            salaryChoice = input()
            if salaryChoice == "yes":
                print("Please enter the new employee's basic salary")
                basicSalary = int(input())
                employee.set_basic_salary(basicSalary)

            print()
            print("Do you want to change employee's basic health insurance statusy? (yes, no)")
            healthChoice = input()
            if healthChoice == "yes":
                print("Please enter the new employee's health insurance status (true, false)")
                healthInsurance = input()
                while healthInsurance != "true" and healthInsurance != "false":
                    print("Please re-enter the health insurance status")
                    healthInsurance = input()
                employee.set_health_insurance(healthInsurance)
            break

    if flagId == 0:
        print("There is no employee with this ID!")


def add_update_administrative():
    flagId = 0
    print("Please enter the employee's id")
    id = int(input())

    for employee in employees:
        if id == employee.get_id():
            flagId = 1
            if employee.get_type() != "Administrative" and employee.get_status() == "Left-university":
                print("Couldn't add/update, the employee is academic or left university")
                break
            else:
                print("Please enter the number of vacation days")
                vacationdays = int(input())
                print("Please enter the year of the vacation days")
                year = int(input())
                employee.add_vacation_days(year, vacationdays)
                break
    if flagId == 0:
        print("Couldn't find employee with this ID")


def add_update_academic():
    flagId = 0
    print("Please enter the employee's id")
    id = int(input())

    for employee in employees:
        if id == employee.get_id():
            flagId = 1
            if employee.get_type() != "Academic" and employee.get_status() == "Left-university":
                print("Couldn't add/update, the employee is Administrative or left university")
                break
            else:
                print("Please enter the list of courses of experience (course1, course2, ...)")
                experience = input().split(",")
                print("Please enter the year of the experience courses")
                year = int(input())
                print("Please enter the semester of experience courses")
                semester = int(input())
                employee.add_expireence(year, semester, experience)
                break
    if flagId == 0:
        print("Couldn't find employee with this ID")


def display_employee_stat():
    print("The number of all employees is =", General.numOfAll)
    print("The number of Male employees is =", General.numOfMale)
    print("The number of Female employees is =", General.numOfFemale)
    print("The number of Administrative employees is =", General.numOfAdmin)
    print("The number of Academic employees is =", General.numOfAcademic)
    print("The number of Full time employees is =", General.numOfFullTime)
    numOffULL = General.numOfFullTime
    numOfAll = General.numOfAll
    percent = (numOffULL / numOfAll) * 100
    print('The percent of full-time employees is %.2f' % percent)


def salary_stat():
    for employee in employees:

        basicSalary = employee.get_basic_salary()
        numOfChilds = employee.get_num_of_children()
        sumAcademic = 0
        sumAdmin = 0

        if employee.get_marital_status() == "Maried":
            if employee.get_health_insurance() == "true":
                finalSalary = basicSalary + 20 + (15 * numOfChilds) - 12 * (1 + (1 + numOfChilds))
                employee.set_final_salary(finalSalary)
            else:
                finalSalary = basicSalary + 20 + (15 * numOfChilds) - 12
                employee.set_final_salary(finalSalary)
        else:
            finalSalary = basicSalary + (15 * numOfChilds) - 12
            employee.set_final_salary(finalSalary)
    # -------------------------------------------------------------------

    for employee in employees:
        if employee.get_type() == "Administrative":
            sumAdmin = sumAdmin + employee.get_final_salary()
        else:
            sumAcademic = sumAcademic + employee.get_final_salary()

    avgAdmin = (sumAdmin / General.numOfAdmin)
    avgAcademic = (sumAcademic / General.numOfAcademic)
    print('Average academic employees’ salary is %.2f' % avgAcademic)
    print('Average Administrative employees’ salary is %.2f' % avgAdmin)
    # --------------------------------------------------------------------

    print()
    print("Please enter a salary to check which employees have greater than the salary defined")
    salaryDefined = int(input())
    for employee in employees:
        if employee.get_final_salary() > salaryDefined:
            name = employee.get_name()
            print("The employee with this name " + name[0] + name[1] + name[1] + " has salary more than " + str(salaryDefined)  + " which is " + str(employee.get_final_salary()))


def admin_employees_stat():
    for employee in employees:
        if employee.get_type() == "Administrative":
            sum = 0
            count = 0
            dict = employee.get_vacation()
            for i in dict.values():
                count = count + 1
                sum = sum + int(i)
            print("Employee with ID " + str(employee.get_id()) + " took " + str(
                sum) + " vacation days since working here")
            if count == 0:
                avg = 0
            else:
                avg = sum / count
            print('Average number of vacations per year is %.2f' % avg)
            print()
        else:
            print("The employee with id " + str(employee.get_id()) + " is not Admin")
            print()

def academic_employees_stat():
    for employee in employees:
        if employee.get_type() == "Academic":
            dict = employee.get_experience()
            count = 0
            countSemester = 0
            for list in dict.values():
                countSemester = countSemester + 1
                for i in list:
                    count = count + 1
            print("The number of courses employee with ID " + str(employee.get_id()) + " taught is " + str(count))
            if countSemester == 0:
                avg = 0
            else:
                avg = count / countSemester
            print('Average number of courses per semester is %.2f' % avg)
            print()
        else:
            print("The employee with id " + str(employee.get_id()) + " is not Academic")
            print()


def RetirementInfo():

    print("Please enter n number to compare Retirement with")
    n = int(input())

    today = date.today()
    currentY = today.year

    for employee in employees:
       birthdate = employee.get_birth_date()
       birthYear = int(birthdate[2])
       age = currentY - birthYear
       startdate = employee.get_starting_time()
       startYear = int(startdate[1])
       workingY = today.year - startYear
       if age <= 65 and workingY <= 35:
           numOfYearsLeft = 65 - age - workingY
           name = employee.get_name()
           if numOfYearsLeft < n:
               print("Name : " + name[0] + name[1] + name[2])


def Courses_stat():
    dict = {}
    dictE = {}
    for employee in employees:
        if employee.get_type() == "Academic":
            temp = employee.get_experience()
            for x in temp.values():
                list = x
                for i in list:
                    dict[i]=0
    for employee in employees:
        if employee.get_type() == "Academic":
            temp = employee.get_experience()
            for x in temp.values():
                list = x
                for i in list:
                    dict[i]+=1

    print("Number of times the course is offered:")
    for i in dict:
      print(i, ' : ', dict[i])

    print()
    # -------------------------------------------

    for employee in employees:
        if employee.get_type() == "Academic":
            temp = employee.get_experience()
            for x in temp.values():
                list = x
                for i in list:
                    dictE[i]=0

    listAll = []
    for employee in employees:
        listEmp = []
        if employee.get_type() == "Academic":
            temp = employee.get_experience()
            for x in temp.values():
                for n in x:
                    listEmp.append(n)
            listAll.append(listEmp)

    for n in dictE.keys():
        for list in listAll:
            for i in list:
                if i == n:
                    dictE[i] += 1
                    break
        continue

    print("Number of academic employees who taught this course:")
    for i in dictE.keys():
      print(i, ' : ', dictE[i])

# menu section------------------------------------------------------

def menu():
    print('1. Add new Employee Record')
    print('2. Update general attribute')
    print('3. Add/Update Administrative employee attribute')
    print('4. Add/Update academic employee attribute')
    print('5. Employee’s statistics')
    print('6. Salary statistics')
    print('7. Retirement information')
    print('8. Courses statistics')
    print('9. Administrative employees’ statistics')
    print('10. Academic employees’ statistics')
    print('11. Exit')

print()
while True:
    try:
        menu()
        print('')
        option = input('Enter option: ')
        if option == "1":
            state = add_new_employee()
            if state == 1:
                print("Added successfully!")
            print("-----------------------------------------------------------")
        elif option == "2":
            update_general_attributes()
            print("-----------------------------------------------------------")
        elif option == "3":
            add_update_administrative()
            print("-----------------------------------------------------------")
        elif option == "4":
            add_update_academic()
            print("-----------------------------------------------------------")
        elif option == "5":
            display_employee_stat()
            print("-----------------------------------------------------------")
        elif option == "6":
            salary_stat()
            print("-----------------------------------------------------------")
        elif option == "7":
            RetirementInfo()
            print("-----------------------------------------------------------")
        elif option == "8":
            Courses_stat()
            print("-----------------------------------------------------------")
        elif option == "9":
            admin_employees_stat()
            print("-----------------------------------------------------------")
        elif option == "10":
            academic_employees_stat()
            print("-----------------------------------------------------------")
        elif option == "11":
            break
        else:
            print("Please enter number between 1-10 is stated in the instruction above")
    except Exception:
        print('error occurred try again later')
