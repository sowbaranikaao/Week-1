import unittest
from employee import create_employee
class TestEmployee(unittest.TestCase):
    def test_invalid_age(self):
        with self.assertRaise(ValueError):
            create_employee(
                "Alice",
                -5,
                5000
            )
if __name__=="__main__":
    unittest.main()