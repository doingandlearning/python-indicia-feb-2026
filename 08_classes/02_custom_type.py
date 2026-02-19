# Employee Management System

employee1 = {
  "name": "Alice Johnson",
  "employee_id": "EMP001",
  "department": "Engineering",
  "salary": 70000,
  "start_date": "2023-01-15"
}

print(employee1["name"])
print(type(employee1))

import datetime

class Employee:
  def __init__(self, name, employee_id, department, salary, start_date):
    self.name = name
    self.employee_id = employee_id
    self.department = department
    self.salary = salary
    self.start_date = start_date
    self.skills = []
    self.created_at = datetime.datetime.now() 
  
  def __str__(self):
    return f"{self.name} ({self.employee_id}) - {self.department}"

  def give_raise(self, percent):
    """Give employee raise by given percent (10 rather than 0.1)"""
    self.salary = self.salary * (1 + percent / 100)
  
  def add_skill(self, skill):
    self.skills.append(skill)

employee2 = Employee(
                      name="Alice", 
                      employee_id="EMP001", 
                      department="Engineering", 
                      salary=75000, 
                      start_date="2024-01-01")  # instantiating an object
# Employee -> __init__ -> object's __init__

employee3 = Employee(name="Kevin", employee_id="EMP002", department="L&D", salary=1, start_date="2024-01-01")
employee2.give_raise(5)
# print -> __str__
print(employee2.salary)


# class HouseData:
#   def __init__(self, is_occupied, address, value, monthly_rent, last_occupied):
#     pass

#   def calculate_lost_income(self):
#     pass

# houses = [HouseData(), HouseData()]
# lost_incomes = [h.calculate_lost_income() for h in houses]



# Load file -> extract the data -> make classes from data 

class CrimeLocation:
  pass

  def distance_from(self, lng, lat):
    pass


spreadsheet_rows = [] # loaded the spreadsheet into a list
crime_locations = []

for row in spreadsheet_rows:
  crime_locations.append(CrimeLocation(id=row[3], long=row[6], lat=row[7]))



near_city_centre = [c for c in crime_locations if c.distance_from(56,23) < 100]