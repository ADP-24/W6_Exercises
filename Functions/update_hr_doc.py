hr_list = [
    ('0123', 'HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahna Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000')
]

hr_list = [
    (emp[0], emp[1], 'Mark Blick-Hawley' if emp[2] == 'Mark Blick' else emp[2], emp[3])
    if emp[2] != 'Jim Smith' else (emp[0], 'CS', emp[2], '6000')
    for emp in hr_list
]

def display_employees(employee_list):
    print("Employee# | DeptCode | Name | Salary")
    for emp in employee_list:
        emp_id, department, name, salary = emp
        formatted_salary = f"{int(salary):,}"
        print(f"{emp_id} | {department} | {name} | {formatted_salary}")

display_employees(hr_list)