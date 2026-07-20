from dataclasses import dataclass
#dataclass
@dataclass
class InvoiceData:
    invoice_id: int
    customer_name: str
    amount: float
    status: str

#controller class
class InvoiceController:
    def __init__(self,invoice):
        self.invoice=invoice
    def validate(self):
        if self.invoice.amount<=0:
            print("Invalid amount. Amount must be greater than zero.")
            return False
        if self.invoice.customer_name.strip()=="":
            print("Invalid customer name. Customer name cannot be empty.")
            return False
        print("Invoice is valid.")
        return True
    def calculate_tax(self):
        return self.invoice.amount*0.18
    def print_invoice(self):
        tax=self.calculate_tax()
        print("\n------ Invoice ------")
        print("Invoice ID :", self.invoice.invoice_id)
        print("Customer   :", self.invoice.customer_name)
        print("Amount     :", self.invoice.amount)
        print("GST        :", tax)
        print("Status     :", self.invoice.status)
class Main:
    invoice=InvoiceData("INV001","John Doe",1000.0,"Pending")
    controller=InvoiceController(invoice)
    if controller.validate():
        controller.print_invoice()

