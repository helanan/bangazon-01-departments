class Departments(object):

    """Parent class for all departments
    Methods:
    --------
    build_departments
    sell_stock
    purchase_stock
    """
    def __init__(self, name, supervisor, employee_count=0, stock=None, salary=0, budget=0):
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.stock = stock
        self.salary = salary
        self.budget = budget

    # method to define the department names
    def departmentName(self):
        return self.name.split()[-1]

    def increaseStaffPay(self, percent):
         self.salary *= (1.0 + percent)

    def getBudget(self, amount):
        self.budget *= (1.0 + amount)

if __name__ == '__main__':
    clothing = Departments('Clothing', 'Ryan Belcher', 30, 'Jeans', 30000, 2000)
    toys = Departments('Toys', 'Helana Nosrat', 40, 'Dolls', 35000, 3000)
    groceries = Departments('Groceries', 'Miriam Rosenbaum', 55, 'Produce', 45000, 4000)
    homegoods = Departments('Home Goods', 'Taylor Perkins', 45, 'Furniture', 20000, 5000)
    # print(clothing.name, toys.supervisor, groceries.employee_count, homegoods.stock)
    # print(clothing.name.split()[-1])
    # toys.employee_count *= 3
    # print(toys.employee_count)
    print("----------Department Names-----------------")
    print("Department Name: " + str(clothing.departmentName()))
    clothing.increaseStaffPay(.2)
    clothing.getBudget(3)
    print("Department Name: " + str(toys.departmentName()))
    toys.increaseStaffPay(.05)
    clothing.getBudget(1)
    print("Department Name: " + str(groceries.departmentName()))
    groceries.increaseStaffPay(.10)
    clothing.getBudget(4)
    print("Department Name: " + str(homegoods.departmentName()))
    homegoods.increaseStaffPay(.02)
    clothing.getBudget(5)

    print("---------------------------")
    print("Surpise! All Department Employees Reached Their Goals, They All Got Raises!")
    print("Increased Department Salaries To:" + str(clothing.salary))
    print("Increased Department Salaries To:" + str(toys.salary))
    print("Increased Department Salaries To:" + str(groceries.salary))
    print("Increased Department Salaries To:" + str(homegoods.salary))

    print("---------------------------")
    print("Surpise! All Department Reached Their Goals, Budgets have been increased!")
    print("Increased Department Budgets To:" + str(clothing.budget))
    print("Increased Department Budgets To:" + str(toys.budget))
    print("Increased Department Budgets To:" + str(groceries.budget))
    print("Increased Department Budgets To:" + str(homegoods.budget))


# built a employee constructor method that fills out the instance with data
# passed in as arguments to the class name

departmentsDB = [clothing, toys, groceries, homegoods] # my "database" list
for departmentDB in departmentsDB:
    print("---------DEPARTMENTS/EMPLOYEE COUNT------------------")
    print(departmentDB.name, departmentDB.employee_count)

general_overview = [(departmentDB.name, departmentDB.employee_count)
                    for departmentDB in departmentsDB]
print("---------General Overview------------------")
print(general_overview)

# if employee count is over or = 45 people
large_staff = ([rec.name for rec in departmentsDB if rec.employee_count >= 45])
print("--------Large Staff Added---------: ")
print(large_staff)

doublestaff = [(rec.employee_count **2 if rec.employee_count >= 45
                else rec.employee_count) for rec in departmentsDB]
print("--------Double Staff Added---------: ")
print(doublestaff)

print("--------PART TWO: METHOD OVERRIDING---------------------------")


@property
def name(self):
    try:
        return self.__name
    except AttributeError:
        return ""

@name.setter
def name(self, val):
    if isinstance(val, str):
        raise TypeError('Please provide a string value for the department name')
        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a department name")
@property
def supervisor(self):
    try:
        return self.__supervisor
    except AttributeError:
        return ""

@supervisor.setter
def supervisor(self, val):
    if not isinstance(val, str):
        raise TypeError('Please provide a string value for the supervisor name')
        if val is not "" and len(val) > 5:
            self.__supervisor = val
        else:
            raise ValueError("Please provide a supervisor name")
