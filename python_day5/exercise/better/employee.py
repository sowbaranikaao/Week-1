import logging
import frappe
logger=logging.getLogger(__name__)
@frappe.whitelist()
def create_employee(
    name:str,
    age:int,
    salary:float
)->str:
    """
    Create a new Employee document
    """
    if not name.strip():
        raise ValueError("Employee name cant be empty")
    if age<=0:
        raise ValueError("Age must be greater than zero")
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
    if not frappe.has_permission("Employee","create"):
        frappe.throw("Permission denied")
    try:
        employee=frappe.get_doc({
            "doctype":"Employee",
            "employee_name":name,
            "age":age,
            "salary":salary
        })
        employee.insert()
        return "Employee created successfully"
    except Exception as error:
        logger.error(error)
        raise
