# In file: employee_utils.py
def give_raise(employee_dict, percent):
    """Give employee a raise."""
    employee_dict["salary"] = employee_dict["salary"] * (1 + percent / 100)

def transfer_department(employee_dict, new_dept):
    """Transfer employee to new department."""
    employee_dict["department"] = new_dept

# In file: payroll.py
def process_payroll(employee_dict):
    """Process payroll for employee."""
    # Need to know the shape: {"name": ..., "salary": ..., "employee_id": ...}
    salary = employee_dict["salary"]
    # ...

# In file: reporting.py
def generate_report(employee_dict):
    """Generate employee report."""
    # Need to know the shape AGAIN: {"name": ..., "department": ..., ...}
    name = employee_dict["name"]
    dept = employee_dict["department"]
    # ...