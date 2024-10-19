class StudentInfo:
    unit_charge = 1551.00

    def __init__(self):
        # Student info
        self.student_name = ""
        self.course = ""
        self.student_number = ""
        self.acad_year = ""
        self.current_date = ""
        self.downpayment = 0.0

    def get_student_info(self, student_name, course, student_number, acad_year, current_date, downpayment):
        self.student_name = student_name
        self.course = course
        self.student_number = student_number
        self.acad_year = acad_year
        self.current_date = current_date
        self.downpayment = downpayment

    def display_student_data(self):
        print("Student Name:", self.student_name)
        print("Course:", self.course)
        print("Student Number:", self.student_number)
        print("Academic Year:", self.acad_year)
        print("Current Date:", self.current_date)
        print("Downpayment: P", f"{self.downpayment:,.2f}")


class UnitInfo:
    def __init__(self):
        self.subjects = []

    def add_subject(self, section, subject, units):
        self.subjects.append([section, subject, units])

    def display_units(self):
        print("\n=================== Enrolled Units ===================")
        for idx, subject_info in enumerate(self.subjects, start=1):
            print(f"Subject {idx}:")
            print("Section:", subject_info[0])
            print("Subject:", subject_info[1])
            print("Units:", subject_info[2])

    def total_units(self):
        total = 0
        for subject_info in self.subjects:
            total += subject_info[2]
        return total

class Assessment:
    def __init__(self):
        # Static fees input
        self.adu_chronicle = 0.00
        self.athletic = 0.00
        self.av_library = 0.00
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
        self.student_act_fee = 0.00
        self.student_nurture_fee = 0.00
        self.technology_fee = 0.00
        self.test_papers = 0.00

    def compute_tuition_fee(self, total_units):
        return total_units * StudentInfo.unit_charge

    def compute_assessment_amount(self, tuition_fee):
        total_fees = (
                self.adu_chronicle + self.athletic + self.av_library + self.ausg + self.cultural_fee +
                self.energy_cost + self.guidance + self.insurance_fee + self.lms + self.library_fee +
                self.med_den_fee + self.registration + self.rso + self.student_act_fee +
                self.student_nurture_fee + self.technology_fee + self.test_papers
        )
        return tuition_fee + total_fees


class FeeComputation:
    def compute_total_due(self, assessment_amount, downpayment):
        return assessment_amount + downpayment

    def compute_payment_schedule(self, total_due):
        return total_due / 3