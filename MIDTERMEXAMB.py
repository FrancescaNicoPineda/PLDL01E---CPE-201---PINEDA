import MIDTERMEXAMA

def display_all_info(customer, assessment): #this will display all inputs
    print(f'''
    ------------------------------------------------------------
      Advisory: Check payment WILL NOT BE ACCEPTED without the
      Statement of Acount effective October 01, 2019          
    ------------------------------------------------------------
                                {customer.maynilad_name}
                                {customer.maynilad_address}
                                {customer.maynilad_city}
                                {customer.maynilad_vat}
                                {customer.maynilad_spm}
                                {customer.maynilad_machinesn}
    SOA # {customer.statement_of_account_no}
                      STATEMENT OF ACCOUNT 
                 For the month of: {customer.soa_month}
                      
                      SERVICE INFORMATION 
    Contract Account No: {customer.contract_account_number}
    Account Name       : {customer.account_name}
    Service Address    : {customer.service_address}
    TIN                : {customer.tin}
    Rate Class         : {customer.rate_class}
    Business Area      : {customer.business_area}
    ------------------------------------------------------------
                      METERING INFORMATION
         Meter No.             MRU No:               Seq No.                  
       {assessment.meterno}      {assessment.mruno}             {assessment.seqno}
    Reading Date      :{assessment.reading_date}
    Present Reading   :{assessment.present_reading}
    Previous Reading  :{assessment.previous_reading}
    Consumption (cu.m):{assessment.consumption}
    
    Previous 3 Months
       Consumption 
    ------------------------------------------------------------
                     BILL & PAYMENT HISTORY
    Desc      Total Amount            OR#              Date
    
    Description: WB-Water Bill, GD-Guarantee Deposit, MISC-
    Reopening Fee, Connection Fee, Metering Charge
    ____________________________________________________________
                        BILLING SUMMARY 
    BILLING PERIOD :{assessment.billing_period1} TO {assessment.reading_date}
    Current Charges                                  {(round(assessment.total_amount, 2))}
      Basic Charge                                   {(round(assessment.basic_charge, 2))}
      Environmental Charge (20% of Basic Charge)     {(round(assessment.environmental_charge, 2))}
      Maintenance Service Charge (MSC)               {(round(assessment.maintenance_charge, 2))}
      Total Current Charges Before Taxes             {(round(assessment.total_current_charges_before_tax, 2))}
      Government Taxes                               {(round(assessment.government_taxes, 2))}
      
      
    ------------------------------------------------------------
    TOTAL AMOUNT DUE                          PHP{(round(assessment.total_amount, 2))}
    PAYMENT DUE DATE                          {assessment.payment_duedate}
    ------------------------------------------------------------                  
''')

customer = MIDTERMEXAMA.CustomerInfo()
customer.get_maynilad_info()
assessment = MIDTERMEXAMA.BillingInfo(customer)
assessment.billing_computation()
display_all_info(customer, assessment)
