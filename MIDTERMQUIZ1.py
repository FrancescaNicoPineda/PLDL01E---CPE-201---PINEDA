# This program assesses the classes for each category

class CustomerInfo:
    def __init__(self):
        self.customer_name = input("Customer Name: ")
        self.cust_address1 = input("Home Address: ")
        self.cust_address2 = input("Barangay: ")
        self.cust_address3 = input("City: ")
        self.cust_address4 = input("Province: ")
        self.customer_no = input("Customer Account Number: ")
        self.previous_billing = float(input("Balance from Previous Billing: "))

class BillingInfo:
    def __init__(self, customer):
        self.rate_per_kwh = self.get_float_input("Rate per kWH: ")
        self.actual_consumption = self.get_float_input("Actual Consumption: ")
        self.remaining_balance = self.get_float_input("Remaining Balance from Previous Billing: ")
        self.transmission = self.get_float_input("Transmission: ")
        self.systemloss = self.get_float_input("System Loss: ")
        self.distribution = self.get_float_input("Distribution (Meralco): ")
        self.subsidies = self.get_float_input("Subsidies: ")
        self.government_taxes = self.get_float_input("Government Taxes: ")
        self.universal_charges = self.get_float_input("Universal Charges: ")
        self.fitan = self.get_float_input("Fit-AN (Renewable): ")
        self.applied_credits = self.get_float_input("Applied Credits: ")
        self.other_charges = self.get_float_input("Other Credits: ")
        self.installment_due = self.get_float_input("Installment Due: ")

        self.service_id_num = input("Service ID Number: ")
        self.rate = input("Rate (Residential/Commercial): ")

        self.bill_date = input("Bill Date: ")
        self.meter_read_date = input("Meter Reading Date: ")
        self.bill_period = input("Bill Period: ")
        self.due_date = input("Due Date: ")

        self.total_kwh = self.get_float_input("Total kWH: ")
        self.total_current_amount = self.get_float_input("Total Current Amount: ")

        self.next_meter_reading = input("Next Meter Reading: ")

        self.customer = customer

    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def billing_computation(self):
        self.generation = self.rate_per_kwh * self.actual_consumption
        self.total_amount = self.remaining_balance + self.generation + self.transmission + self.systemloss + self.distribution + self.subsidies + self.government_taxes + self.universal_charges + self.fitan + self.applied_credits + self.other_charges + self.installment_due

    def previousbilling_note(self):
        if self.customer.previous_billing == 0:
            self.note = "Thank You"
        else:
            self.note = "Balance Carrying Over"





