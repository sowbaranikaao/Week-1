from dataclasses import dataclass
@dataclass
class InvoiceData:
    invoice_id:int
    customer_name:str
    amount:float
    status:str

class InvoiceController:
    TAX_RATE=0.18
    def __init__(self,invoice:InvoiceData):
        self.invoice=invoice
    def validate(self):
        """
        Validate the invoice data.
        """
        if self.invoice.invoice_id <=0:
            print("Invalid invoice ID")
            return False
        if self.invoice.customer_name.strip() == "":
            print("Customer name cannot be empty")
            return False
        if self.invoice.amount <=0:
            print("Amount must be greater than zero")
            return False
        print("Invoice data is valid")
        return True
    def calculate_tax(self):
        """"Calculate the tax for the invoice amount."""
        tax=self.invoice.amount*self.TAX_RATE
        return tax
    def print_invoice(self):
        """"
        Display invoice details"""
        tax=self.calculate_tax()
        total=self.invoice.amount+tax
        print("\n----------- Invoice -----------")
        print(f"Invoice ID : {self.invoice.invoice_id}")
        print(f"Customer   : {self.invoice.customer_name}")
        print(f"Amount     : ₹{self.invoice.amount:.2f}")
        print(f"GST (18%)  : ₹{tax:.2f}")
        print(f"Total      : ₹{total:.2f}")
        print(f"Status     : {self.invoice.status}")
        print("-------------------------------")
class Main:
    invoice=InvoiceData(
        invoice_id=101,
        customer_name="John",
        amount=1500.00,
        status="Pending"
    )
    controller=InvoiceController(invoice)
    if controller.validate():
        controller.print_invoice()