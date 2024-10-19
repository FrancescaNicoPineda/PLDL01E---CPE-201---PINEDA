class studentinfo:
      unit_charge = 1551.00
      def __init__(self):
          #student info
          self.student_name = ""
          self.course = ""
          self.student_number = ""
          self.acad_year = ""
          self.current_date = ""
          self.downpayment = ""

      def get_student_info(self, student_name, course, student_number, acad_year, current_date, downpayment):
          self.student_name = student_name
          self.course = course
          self.student_number = student_number
          self.acad_year = acad_year
          self.current_date = current_date
          self.downpayment = downpayment

      def display_student_data(self):
          print("Student Name:",   self.student_name )
          print("Course: ", self.course )
          print("Student Number: ", self.student_number)
          print("Academic Year: ",  self.acad_year)
          print("Current Date: ", self.current_date)
          print("Downpayment: ", self.downpayment)

class units:
      def unitsinfo(self):
          self.section = ""
          self.subject = ""
          self.no_units = ""

      def get_unit_info(self, section, subject, no_units):
          self.section = section
          self.subject = subject
          self.no_units = no_units

      def display_unit(self):
          print("Section: ", self.section)
          print("Subject: ", self.subject)
          print("Units: ", self.no_units)
class assessment:

      def assessmentinfo(self):
          self.charge_per_unit = 1551.00
          self.total_no_units = float(input("Total Number of Units: "))
          self.adu_chronicle = 0.00
          self.athletic = 0.00
          self.av_library = 00.00
          self.ausg = 0.00
          self.cultural_fee = 0.00
          self.energy_cost = 0.00
          self.guidance = 0.00
          self.insurance_fee = 0.00
          self.lms = 0.00
          self.library_fee = 0.00
          self.med_den_fee = 0.00
          self.registration = 0.00
          self.rso = 0.00
          self.stud_act_fee = 0.00
          self.stud_nurtur_fee = 0.00
          self.technology_fee = 0.00
          self.test_papers = 0.00

class feecomputation:
      def fee_computation(self):
          self.tuition_fee = self.total_no_units * self.charge_per_unit
          self.assessment_fee = self.tuition_fee + self.adu_chronicle + self.athletic + self.av_library + self.ausg + self.cultural_fee + self.energy_cost + self.guidance + self.insurance_fee + self.lms + self.library_fee + self.med_den_fee + self.registration + self.rso + self. stud_act_fee + self.stud_nurtur_fee + self.technology_fee + self.test_papers
          self.total_due =  self.assessment_fee + self.downpayment
          self.sched_payment = self.total_due/3

