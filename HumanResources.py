from Department import*

class HumanResources(Department):
  """Class for representing Human Resources department

  Methods: __init__, add_policy, get_policy, etc.
  """
if __name__ == '__main__':
    tom = Manager(fullName='Tom Doe', age=50, pay=50000, name=None)
    tom.departmentName('homegoods')
    print(tom.name)

  # def __init__(self, name, supervisor, employee_count):
  #   super().__init__(name, supervisor, employee_count)
  #   self.policies = set()
  #
  # def add_policy(self, policy_name, policy_text):
  #   """Adds a policy, as a tuple, to the set of policies
  #
  #   Arguments:
  #     policy_name (string)
  #     policy_text (string)
  #   """
  #
  #   self.policies.add((policy_name, policy_text))

######
# hr_department = HumanResources(...)
# print(hr_department.name)
