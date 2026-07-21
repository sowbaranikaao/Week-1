import frappe
@frappe.whitelist()
def create_employee(name, age, salary):
    employee = frappe.get_doc({
        "doctype": "Employee",
        "employee_name": name,
        "age": age,
        "salary": salary
    })
    employee.insert()
    return "Employee Created"