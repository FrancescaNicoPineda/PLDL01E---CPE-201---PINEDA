import MIDTERMQUIZ1  # Assuming this is your main module

def display_customer_info(customer):
    print(f'''
    ----------------------------------------------------------------------------------------
    {customer.customer_name}
    {customer.cust_address1}
    {customer.cust_address2}
    {customer.cust_address3}
    {customer.cust_address4}
    ----------------------------------------------------------------------------------------
    **************************
    ''')


def display_service_info(assessment):
    print(f'''
    ----------------------------------------------------------------------------------------
                                       Electric Bill
    Summary for Customer Account Number (CAN) {assessment.customer.customer_no}
    Balance from Previous Billing : ₱{assessment.customer.previous_billing}
    {assessment.note}
    ----------------------------------------------------------------------------------------
    **************************
    ''')


def display_billing_info(assessment):
    print(f'''
    ----------------------------------------------------------------------------------------
                                       Current Charges
    Amount Due: ₱{assessment.total_amount}
    Due Date: {assessment.due_date}
    ----------------------------------------------------------------------------------------
    Total Amount Due
    ₱{assessment.total_amount}
    ----------------------------------------------------------------------------------------
                                       Service Info
    Service ID Number: {assessment.service_id_num}
    Rate: {assessment.rate}
    Contact in the Name of {assessment.customer.customer_name}
    Service Address: {assessment.customer.cust_address1}, {assessment.customer.cust_address2}, 
                     {assessment.customer.cust_address3}, {assessment.customer.cust_address4}
    ----------------------------------------------------------------------------------------
                                       Billing Info
    Bill Date: {assessment.bill_date}
    Meter Reading Date: {assessment.meter_read_date}
    Bill Period: {assessment.bill_period}
    Due Date: {assessment.due_date}
    Total kWH: {assessment.total_kwh}
    Total Current Amount: ₱{assessment.total_current_amount}
    Next Meter Reading: {assessment.next_meter_reading}
    ----------------------------------------------------------------------------------------
    ''')


def display_computation_summary(assessment):
    print(f'''
    ----------------------------------------------------------------------------------------
                                       Bill Computation Summary
    Remaining Balance from Previous Bill: ₱{assessment.customer.previous_billing}
    Generation: ₱{assessment.generation}
    Transmission: ₱{assessment.transmission}
    System Loss: ₱{assessment.systemloss}
    Distribution (Meralco): ₱{assessment.distribution}
    Subsidies: ₱{assessment.subsidies}
    Government Taxes: ₱{assessment.government_taxes}
    Universal Charges: ₱{assessment.universal_charges}
    FIT-All (Renewable): ₱{assessment.fitan}
    Applied Credits: ₱{assessment.applied_credits}
    Other Charges: ₱{assessment.other_charges}
    Installment Due: ₱{assessment.installment_due}
    ----------------------------------------------------------------------------------------
    Total Amount Due: ₱{assessment.total_amount}
    ----------------------------------------------------------------------------------------
    ''')



customer = MIDTERMQUIZ1.CustomerInfo()
assessment = MIDTERMQUIZ1.BillingInfo(customer)
assessment.billing_computation()
assessment.previousbilling_note()
display_customer_info(customer)
display_service_info(assessment)
display_billing_info(assessment)
display_computation_summary(assessment)



