from Department import*

class Employee:
    """
    a general employee: data + logic
    """
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def increaseStaffPay(self, percent):
        self.employee_count += (1.0 + percent)

    def __str__(self):
        return('<% => %s: %s, %s,>' %
               self.__class__.__name__, self.name, self.job, self.employee_count)

class Manager(Employee):
    """
    a person with custom raise
    inherits general lastname, str
    """

    def __init__(self, name, age, pay):
        Employee.__init__(self, percent + bonus)

if __name__ == '__main__':
    bob = Employee('Bob Smith', 44)
    sue = Employee('Sue JOnes', 47, 40000, 'hardware')
    tom = Manager(name='Tome Doe', age=50, pay=5000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)  # run this obj's giveRaise
        print(obj) # run common __str__method

# tom = Manager('Tom Jones', 50)
# print(tom)
