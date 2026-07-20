from enum import Enum
class Status(Enum):

    ACTIVE = "Active"

    INACTIVE = "Inactive"

    PENDING = "Pending"
employee = Status.ACTIVE
print(employee)
print(employee.value)
print(employee.name)