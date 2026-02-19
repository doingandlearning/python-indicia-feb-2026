class Employee:
  def __init__(self, name, employee_id, department, salary, start_date):
    self.name = name
    self.employee_id = employee_id
    self.department = department
    self.salary = salary
    self.start_date = start_date
    self.skills = []
  
  def __str__(self):
    return f"{self.name} ({self.employee_id}) - {self.department}"

  def give_raise(self, percent):
    """Give employee raise by given percent (10 rather than 0.1)"""
    self.salary = self.salary * (1 + percent / 100)
  
  def add_skill(self, skill):
    self.skills.append(skill)

  def __len__(self):
    return len(self.name)

  def has_skill(self, skill):
    return skill in self.skills

  def __contains__(self, skill):
    return skill in self.skills

  def __iter__(self):
    return iter(self.skills)

  def __lt__(self, other):
    return self.salary < other.salary

  def __eq__(self, other):
    return self.salary == other.salary

  def __repr__(self):
    return f'Employee("{self.name}", "{self.employee_id}", "{self.department}", {self.salary}, "{self.start_date}")'

employee1 = Employee("Alice", "EMP001", "Engineering", 75000, "2024-01-01")
employee2 = Employee("Bob", "EMP001", "Engineering", 75000, "2024-01-01")

print(employee1 > employee2)
print(employee1 == employee2)
print(employee1)  # __str__ -> human/user readable
print([employee1, employee2])  # __repr__ => machine/developer readable