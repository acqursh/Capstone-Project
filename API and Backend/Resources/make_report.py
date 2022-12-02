from fpdf import FPDF
from datetime import date, datetime
import requests

r = requests.get("http://127.0.0.1:7000/users_attr").json()[0]
r1 = requests.get("http://127.0.0.1:7000/users").json()[0]


class CreatePDF(FPDF):
    def header(self):

        self.add_font(
            family='Avenir',
            style='',
            fname=r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication F"
                  r"low\Fonts\Avenir Book\avenir_lt_std_45_book.ttf",
            uni=True
        )

        self.add_font(
            family='Avenir',
            style='M',
            fname=r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication F"
                  r"low\Fonts\Avenir Medium\avenir_lt_std_65_medium.ttf",
            uni=True
        )

        self.add_font(
            family='Avenir',
            style='B',
            fname=r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication"
                  r" Flow\Fonts\Avenir Black\avenir_lt_std_95_black.ttf",
            uni=True
        )

        self.image(
            r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication Flow\Report\Logo heart waves.jpg",
            10, 8, 25)

        self.set_font('Avenir', 'B', 23)

        self.cell(70)

        self.write(5, f'Health Report')

        self.set_font('Avenir', '', 8)

        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")

        # Move to the right
        self.cell(38.5)

        self.set_font('Avenir', 'B', 8)

        self.write(5, f"Date : {date.today()}")
        # Line break
        self.ln(10)

        self.line(10, 25, 200, 25)

        self.set_font('Avenir', '', 10)

        self.write(25, f'Patient Name: {r1["first_name"]} {r1["last_name"]}')
        # Line break
        self.ln(5)

        if r["sex"] == 1:
            sex = "Male"
        else:
            sex = "Female"

        self.write(25, f'Sex: {sex}')

        self.ln(5)

        self.write(25, f'Age: {r1["age"]}')

        self.ln(5)

        self.write(25, f'Email: {r["email"]}')

        self.ln(5)

        self.write(25, f"Report Created at : {timestamp}")

        self.line(10, 60, 200, 60)

        self.ln(10)

    # Page footer
    def footer(self):

        self.set_line_width(0.3)

        self.line(10, 265, 200, 265)

        self.set_y(-25)

        self.set_font('Avenir', '', 8)

        self.cell(190, 10,
                  'Note: This is report not meant for actual diagnosis and is part of the capstone project, '
                  'we recommend you to visit the doctor in case of any discomfort',
                  0, 2, 'C')
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def make_report():
    pdf = CreatePDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.ln(10)
    pdf.set_font('Avenir', 'B', 16)
    pdf.cell(0, 25, 'Test Report ', 0, 2, 'C')
    pdf.set_line_width(0.7)
    pdf.line(30, 80, 180, 80)
    pdf.set_font('Avenir', 'M', 12)
    pdf.cell(0, 10, 'Based on the Inputs received these are your readings ', 0, 1)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.set_line_width(0.3)

    if r["restecg"] == '1':
        restecg = "ST"
    elif r["restecg"] == 2:
        restecg = "LVH"
    else:
        restecg = "Normal"

    if r["cp"] == 1:
        cp = "Atypical Angina"
    elif r["cp"] == 2:
        cp = "Non-anginal Pain"
    elif r["cp"] == 3:
        cp = "Asymptomatic"
    else:
        cp = "Typical Angina"

    pdf.set_font('Avenir', 'B', 10)
    pdf.cell(95, 10, f'Blood Cholesterol', 1, 0)
    pdf.set_font('Avenir', 'M', 10)
    pdf.cell(0, 10, f' {r["chol"]}', 1, 1)
    pdf.set_font('Avenir', 'B', 10)
    pdf.cell(95, 10, f'Fasting Blood Sugar', 1, 0)
    pdf.set_font('Avenir', 'M', 10)
    pdf.cell(0, 10, f' {r["fbs"]}', 1, 1)
    pdf.set_font('Avenir', 'B', 10)
    pdf.cell(95, 10, f'Blood Pressure', 1, 0)
    pdf.set_font('Avenir', 'M', 10)
    pdf.cell(0, 10, f' {r["trtbps"]}', 1, 1)
    pdf.set_font('Avenir', 'B', 10)
    pdf.cell(95, 10, f'Maximum Heart Rate Recorded', 1, 0)
    pdf.set_font('Avenir', 'M', 10)
    pdf.cell(0, 10, f' {r["thalachh"]}', 1, 1)
    pdf.set_font('Avenir', 'B', 10)
    pdf.cell(95, 10, f'Resting ECG Category', 1, 0)
    pdf.set_font('Avenir', 'M', 10)
    pdf.cell(0, 10, f' {restecg}', 1, 1)
    pdf.set_font('Avenir', 'B', 10)
    pdf.cell(95, 10, f'Chest Pain type', 1, 0)
    pdf.set_font('Avenir', 'M', 10)
    pdf.cell(0, 10, f' {cp}', 1, 1)
    pdf.set_font('Avenir', 'B', 10)
    pdf.cell(95, 10, f'Slope', 1, 0)
    pdf.set_font('Avenir', 'M', 10)
    pdf.cell(0, 10, f' {r["slp"]}', 1, 1)
    pdf.set_font('Avenir', 'B', 10)

    if r["target"] == 0:
        pdf.cell(95, 10, f'Prediction', 1, 0)
        pdf.set_font('Avenir', '', 10)
        pdf.cell(0, 10, f' Not susceptible', 1, 1)

    else:
        pdf.cell(95, 10, f'Prediction', 1, 0)
        pdf.set_font('Avenir', '', 10)
        pdf.cell(0, 10, f' Susceptible', 1, 1)

    pdf.set_font('Avenir', 'B', 18)

    pdf.ln(20)

    pdf.cell(70)
    pdf.cell(0, 10, f'FINAL REPORT', 0, 1)

    pdf.ln(10)

    pdf.set_font('Avenir', 'M', 12)
    pdf.set_line_width(1)
    pdf.line(30, 220, 180, 220)

    if r['target'] == 0:

        pdf.cell(0, 10,
                 'After Analysing your vitals we predict, that you are not susceptible to a Heart related disease.',
                 0,
                 2, 'C')
        pdf.cell(90, 10, " ", 0, 2, 'C')

    else:

        pdf.cell(0, 10,
                 'After Analysing the vitals we predict that you are susceptible to a Heart related disease ', 0, 2)
        pdf.cell(0, 10,
                 'We recommend you to consult your doctor ASAP',
                 0, 2)

        pdf.cell(90, 10, " ", 0, 2, 'C')

    pdf.output(
        rf'C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication Flow\Report\{r1["first_name"]}{r1["last_name"]}_report.pdf',
        'F')


make_report()
