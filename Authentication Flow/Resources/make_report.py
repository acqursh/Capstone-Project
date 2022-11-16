import joblib
from fpdf import FPDF
from datetime import date
import requests
from a import create_model

r = requests.get("http://127.0.0.1:7000/users_attr").json()[0]
r1 = requests.get("http://127.0.0.1:7000/users").json()[0]

print(r)

create_model()


# for i in r.json():
#     print(i)

class PDF(FPDF):
    def header(self):
        # Logo
        # self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Helvetica', 'B', 20)
        # Title

        self.cell(70)

        self.write(5, f'Health Report')

        self.set_font('Helvetica', 'B', 8)

        # self.ln(1)
        # Move to the right
        self.cell(40)

        self.write(5, f"Date : {date.today()}")
        # Line break
        self.ln(10)

        self.set_font('Helvetica', 'B', 10)

        self.write(5, f'Patient Name: {r1["first_name"]}')
        # Line break
        self.ln(5)

        self.set_font('Helvetica', 'B', 10)

        if r["sex"] == 1:
            sex = "Male"
        else:
            sex = "Female"

        self.write(5, f'Sex: {sex}')

        self.ln(5)

        self.set_font('Helvetica', 'B', 10)

        self.write(5, f'Age: {r1["age"]}')

        self.ln(5)

        self.set_font('Helvetica', 'B', 10)

        self.write(5, f'Email: {r["email"]}')
        # Line break
        self.ln(10)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def predict(x):
    # print(attrs)
    # print(ecg)
    create_model()

    m_jlib = joblib.load(
        r'C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication Flow\model1.pkl')

    return m_jlib.predict([x])


# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 16)
# pdf.cell(0, 10, 'Based on the Inputs received these are your readings ', 0, 1)
pdf.cell(0, 10, 'Based on the Inputs received these are your readings ', 0, 2, 'C')
pdf.cell(90, 10, " ", 0, 2, 'C')

if r["fbs"] == 0:
    fbs = "< 120"
else:
    fbs = "> 120"

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

pdf.set_font('Helvetica', '', 10)
pdf.cell(0, 10, f'Blood Cholesterol : {r["chol"]}', 0, 1)
pdf.cell(0, 10, f'Fasting Blood Sugar : {fbs}', 0, 1)
pdf.cell(0, 10, f'Blood Pressure : {r["trtbps"]}', 0, 1)
pdf.cell(0, 10, f'Maximum Heart Rate Recorded : {r["thalachh"]}', 0, 1)
pdf.cell(0, 10, f'Resting ECG Category : {restecg}', 0, 1)
pdf.cell(0, 10, f'Chest Pain type : {cp}', 0, 1)
pdf.cell(0, 10, f'Slope : {r["slp"]}', 0, 1)

output = predict([r["age"], r["sex"], r["cp"], r["trtbps"], r["chol"], r["fbs"], r["restecg"], r["thalachh"], r["slp"]])

if int(output[0]) == 0:
    pdf.cell(0, 10, f'Prediction : Not susceptible ', 0, 1)

else:
    pdf.cell(0, 10, f'Prediction : Susceptible', 0, 1)

pdf.set_font('Helvetica', 'B', 14)

pdf.ln(30)

pdf.cell(70)
pdf.cell(0, 10, f'FINAL REPORT', 0, 1)

pdf.ln(10)


pdf.set_font('Helvetica', '', 10)

if int(output[0]) == 0:

    pdf.cell(0, 10, 'After Analysing the vitals we predict that you are not susceptible to a Heart related disease', 0,
             2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')

else:

    pdf.cell(0, 10,
             'After Analysing the vitals we predict that you are susceptible to a Heart related disease ', 0, 2)
    pdf.cell(0, 10,
             'We recommend you to consult your doctor ASAP',
             0, 2)

    pdf.cell(90, 10, " ", 0, 2, 'C')

# predict([r["age"], r["sex"], r["cp"], r["trtbps"], r["chol"], r["fbs"], r["restecg"], r["thalachh"], r["slp"]])
# predict([32, 1, 1, 120, 225, 0, 0, 184, 0])
pdf.output('report.pdf', 'F')
