#this class will gather the customer and maynilad informations
class CustomerInfo:
    def __init__(self): #basic info
        self.contract_account_number = input("Contract Account No. : ")
        self.account_name = input("Account Name: ")
        self.service_address =  input("Service Address: ")
        self.statement_of_account_no = input("Statement of Account No. :")
        self.soa_month = input("Statement of Account for the Month of ")
        self.tin = input("TIN :")
        self.rate_class = input("Rate Class: ")
        self.business_area= input("Business Area: ")

    def get_maynilad_info(self): #this is for the maynilad information at the top of the receipt
        self.maynilad_name = ("Maynilad Water Services, Inc.")
        self.maynilad_address = ("8390 DR A SANTOS  AVE BF HOMES")
        self.maynilad_city = ("PARANAQUE CITY")
        self.maynilad_vat = ("VAT Reg TIN 005-393-442-000")
        self.maynilad_spm = ("SPM No.:")
        self.maynilad_machinesn = ("Machine SN:")

class BillingInfo: #computation for billing statemet
    def __init__(self, customer):
        self.billing_period1 = input("Starting Date of Billing Period: ")
        self.payment_duedate = input("Payment Due Date: ")
        self.maintenance_charge = float(input("Maintenance Charge(MSC): "))
        self.cubicm_rate = 23.52
        self.meterno = input("Meter No.: ")
        self.mruno = input("MRU No.: ")
        self.seqno = input("Seq No.: ")
        self.reading_date = input("Reading Date: ")
        self.present_reading = input("Present Reading: ")
        self.previous_reading = input("Previous Reading: ")
        self.consumption = float(input("Consumption (cu.m): "))
    def billing_computation(self): #computation for the bills
        self.basic_charge = self.cubicm_rate * self.consumption
        self.environmental_charge = self.basic_charge * 0.2
        self.total_current_charges_before_tax = self.basic_charge + self.environmental_charge + self.maintenance_charge
        self.government_taxes = self.total_current_charges_before_tax * 0.025
        self.total_amount = self.basic_charge + self.environmental_charge + self.maintenance_charge + self.government_taxes


