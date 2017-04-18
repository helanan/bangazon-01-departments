from Department import Department


class Departments:
  """Contains methods for maintaining a Department

  Methods:
  --------
  build_departments
  sell_stock
  purchase_stock
  """
  def __init__(self, name, supervisor, employee_count=0, stock=None):
      self.name = name
      self.supervisor = supervisor
      self.employee_count = employee_count
      self.stock = stock
  def departmentName(self):
      return self.name.split()[-1]
  def increaseStaff(self, percent):
      self.employee_count *= (1.0 + percent)

if __name__ == '__main__':
    clothing = Departments('Clothing', 'Ryan Belcher', 30, 'Jeans')
    toys = Departments('Toys', 'Helana Nosrat', 40, 'Dolls')
    groceries = Departments('Groceries', 'Miriam Rosenbaum', 55, 'Produce')
    homegoods = Departments('Home Goods', 'Taylor Perkins', 45, 'Furniture')
    # print(clothing.name, toys.supervisor, groceries.employee_count, homegoods.stock)
    # print(clothing.name.split()[-1])
    # toys.employee_count *= 3
    # print(toys.employee_count)
    print("Department Name: " + str(clothing.departmentName()))
    groceries.increaseStaff(.10)
    print("Increased staff to:" + str(groceries.employee_count))


# built a employee constructor method that fills out the instance with data
# passed in as arguments to the class name

departments = [clothing, toys, groceries, homegoods] # my "database" list
for department in departments:
    print(department.name, department.employee_count)

general_overview = [(department.name, department.employee_count) for department in departments]
print(general_overview)

# if employee count is over or = 45 people
large_staff = ([rec.name for rec in departments if rec.employee_count >= 45])
print(large_staff)

doublestaff = [(rec.employee_count **2 if rec.employee_count >= 45
       else rec.employee_count) for rec in departments]
print(doublestaff)


  # def build_habitat(self, habitat):
  # """Adds a habitats to the zoo
  #
  # Method arguments:
  # -----------------
  # habitat(object) -- A habitat instance
  # """
  #
  # self.habitats.add(habitat)
  #
  # def sell_family_ticket(self, family):
  # """Adds an entire family to the list of visitors
  #
  # Method argument:
  # -----------------
  # family(list) -- A list of people in a family of visitors
  # """
  #
  # self.visitors.extend(family)
  #
  # def purchase_animal(self, animal):
  # """Add an animal to the zoo
  #
  # Method arguments:
  # -----------------
  # animal(object) -- An animal instance
  # """
  #
  # self.animals.add(animal)
  #
  # def animal_report(self):
  #
  # for habitat in self.habitats:
  # print("\n\nHabitat:"+habitat.marketing_name)
  # print("-------------------------")
  # for animal in self.animals:
  # if animal.habitat is habitat:
  # print(animal.name)
  #
  # def list_animals(self):
  # """Lists all animals in the zoo
  #
  # Method arguments:
  # n/a
  # """
  #
[print("{} the {}".format(department.name, department.stock)) for departments in self.departments]
