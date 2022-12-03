import os
import time

from fpdf import FPDF
from datetime import date, datetime
from dotenv import load_dotenv
import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
from flask_restful import Resource
from flask_praetorian import auth_required, current_user
from flask import make_response

from Models.user_attr import User_attr
from Models.fitbit_users import Fitbit_users
from Common.api_response import ApiResponse

load_dotenv()

api_response = ApiResponse()


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
            r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication Flow\Extras\Logo heart waves.jpg",
            10, 8, 25)

        self.set_font('Avenir', 'B', 23)

        self.cell(70)

        self.write(5, f'Health Report')

        self.set_font('Avenir', '', 8)

        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        today = date.today().strftime("%m/%d/%Y")

        # Move to the right
        self.cell(38.5)

        self.set_font('Avenir', 'B', 8)

        self.write(5, f"Date : {today}")

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
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    @staticmethod
    def change_sex(sex):
        if sex == 1:
            return "Male"

        return "Female"

    @staticmethod
    def change_ecg(restecg):
        if restecg == 1:
            return "ST"
        elif restecg == 2:
            return "LVH"

        return "Normal"

    @staticmethod
    def change_cp(cp):
        if cp == 1:
            return "Atypical Angina"
        elif cp == 2:
            return "Non-anginal Pain"
        elif cp == 3:
            return "Asymptomatic"

        return "Typical Angina"

    @staticmethod
    def make_report(user, user_attrs):
        pdf = CreatePDF()
        pdf.alias_nb_pages()
        pdf.add_page()

        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")

        pdf.line(10, 25, 200, 25)
        pdf.set_font('Avenir', '', 10)
        pdf.ln(10)
        pdf.cell(0, 20, f'Patient Name: {user.first_name} {user.last_name}')
        pdf.ln(5)

        pdf.cell(0, 20, f'Sex: {CreatePDF.change_sex(user_attrs.sex)}')
        pdf.ln(5)

        pdf.cell(0, 20, f'Age: {user_attrs.age}')
        pdf.ln(5)

        pdf.cell(0, 20, f'Email: {user.email_id}')
        pdf.ln(5)

        pdf.cell(0, 20, f"Report Created at : {timestamp}")
        pdf.line(10, 55, 200, 55)

        pdf.ln(10)
        pdf.set_font('Avenir', 'B', 16)
        pdf.cell(0, 45, 'Test Report ', 0, 2, 'C')
        pdf.set_line_width(0.7)
        pdf.line(30, 80, 180, 80)
        pdf.set_font('Avenir', 'M', 12)
        pdf.cell(0, 0, 'Based on the Inputs received these are your readings ', 0, 1)
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.set_line_width(0.3)

        pdf.set_font('Avenir', 'B', 10)
        pdf.cell(95, 10, f'Blood Cholesterol', 1, 0)
        pdf.set_font('Avenir', 'M', 10)
        pdf.cell(0, 10, f' {user_attrs.chol}', 1, 1)

        pdf.set_font('Avenir', 'B', 10)
        pdf.cell(95, 10, f'Fasting Blood Sugar', 1, 0)
        pdf.set_font('Avenir', 'M', 10)
        pdf.cell(0, 10, f' {user_attrs.fbs}', 1, 1)

        pdf.set_font('Avenir', 'B', 10)
        pdf.cell(95, 10, f'Blood Pressure', 1, 0)
        pdf.set_font('Avenir', 'M', 10)
        pdf.cell(0, 10, f' {user_attrs.trtbps}', 1, 1)

        pdf.set_font('Avenir', 'B', 10)
        pdf.cell(95, 10, f'Maximum Heart Rate Recorded', 1, 0)
        pdf.set_font('Avenir', 'M', 10)
        pdf.cell(0, 10, f' {user_attrs.thalachh}', 1, 1)

        pdf.set_font('Avenir', 'B', 10)
        pdf.cell(95, 10, f'Resting ECG Category', 1, 0)
        pdf.set_font('Avenir', 'M', 10)
        pdf.cell(0, 10, f' {CreatePDF.change_ecg(user_attrs.restecg)}', 1, 1)

        pdf.set_font('Avenir', 'B', 10)
        pdf.cell(95, 10, f'Chest Pain type', 1, 0)
        pdf.set_font('Avenir', 'M', 10)
        pdf.cell(0, 10, f' {CreatePDF.change_cp(user_attrs.cp)}', 1, 1)

        pdf.set_font('Avenir', 'B', 10)
        pdf.cell(95, 10, f'Slope', 1, 0)
        pdf.set_font('Avenir', 'M', 10)
        pdf.cell(0, 10, f' {user_attrs.slp}', 1, 1)

        pdf.set_font('Avenir', 'B', 10)
        if user_attrs.target == 0:
            pdf.cell(95, 10, f'Prediction', 1, 0)
            pdf.set_font('Avenir', 'M', 10)
            pdf.cell(0, 10, f' Not susceptible', 1, 1)

        else:
            pdf.cell(95, 10, f'Prediction', 1, 0)
            pdf.set_font('Avenir', 'M', 10)
            pdf.cell(0, 10, f' Susceptible', 1, 1)

        pdf.set_font('Avenir', 'B', 18)
        pdf.ln(20)
        pdf.cell(70)
        pdf.cell(0, 10, f'FINAL REPORT', 0, 1)
        pdf.ln(10)

        pdf.set_font('Avenir', 'M', 12)
        pdf.set_line_width(1)
        pdf.line(30, 220, 180, 220)
        if user_attrs.target == 0:
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
            fr"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication Flow\Report\{user.first_name}"
            fr"{user.last_name}_report.pdf",
            'F')


class MakeReport(Resource):

    @auth_required
    def get(self):
        try:
            user_attr = User_attr.query.get_or_404(current_user().email_id)
            fitbit_user = Fitbit_users.query.get_or_404(current_user().email_id)
            CreatePDF.make_report(fitbit_user, user_attr)
            time.sleep(4)
            MakeReport.send_report(fitbit_user)
            api_response.success.clear()
            api_response.errors.clear()
            api_response.message = "Report Created and emailed"
            api_response.status = "Success"
            api_response.success.append('Report creating successful')

            return make_response(api_response.to_json(), 200)

        except Exception as e:
            error = e
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = e
            api_response.status = "Fail"
            return make_response(api_response.to_json(), 500)

    @staticmethod
    def send_report(fitbit_user):
        message = Mail(from_email='arko.pal1101@gmail.com',
                       to_emails=f'{fitbit_user.email_id}',
                       subject='Health Report',
                       html_content=f"Dear {fitbit_user.first_name} {fitbit_user.last_name}, <br>"
                                    f"<br>Your heart report is ready and has been attached in this mail. "
                                    f"Please go through it & share it with your doctor in case you are susceptible.<br>"
                                    f"<br> <strong>This report is not a medically holding record and we urge you to "
                                    f"consult with your doctor in case of any discomfort.</strong>")

        with open(
                rf"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication Flow\Report\{fitbit_user.first_name}{fitbit_user.last_name}_report.pdf",
                'rb') as f:
            data = f.read()
            f.close()
        encoded_file = base64.b64encode(data).decode()
        attachedFile = Attachment(
            FileContent(encoded_file),
            FileName('attachment.pdf'),
            FileType('application/pdf'),
            Disposition('attachment')
        )
        message.attachment = attachedFile

        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print("Email Sent")
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
