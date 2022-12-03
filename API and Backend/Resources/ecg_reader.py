import joblib
from Models.user_attr import User_attr
from Common.api_response import ApiResponse
from Common.init_database import db
from Common.model import create_model
from Resources.user_attr import FitbitUserAttrSchema

from PyPDF2 import PdfFileReader

from flask_restful import Resource
from flask_praetorian import auth_required, current_user
from flask import make_response, request

schema = FitbitUserAttrSchema()
api_response = ApiResponse()


class ReadECG(Resource):

    @staticmethod
    def predict_output(attrs):

        create_model()
        m_jlib = joblib.load(
            r'C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication '
            r'Flow\Monitoring and alerting\model1.pkl')

        return m_jlib.predict([attrs])

    @auth_required
    def patch(self):

        try:
            user_attr = User_attr.query.get_or_404(current_user().email_id)

            if 'file' not in request.files:
                return "No file attached"

            pdf_file = request.files['file']
            pdf_name = pdf_file.filename

            if pdf_name == '':
                return 'No selected file'

            if pdf_file:
                pdf = PdfFileReader(pdf_file)
                text = None
                for page in pdf.pages:
                    text = page.extract_text().split("\n")

                if text[2] == "Normal Sinus Rhythm":
                    user_attr.restecg = 0

                else:
                    user_attr.restecg = 1

            if user_attr.fbs < 120:
                fbs = 0
            else:
                fbs = 1

            user_attr.target = int(ReadECG.predict_output(
                [user_attr.age, user_attr.sex, user_attr.cp, user_attr.trtbps, user_attr.chol, fbs,
                 user_attr.restecg, user_attr.thalachh, user_attr.slp]
            )[0])

            db.session.commit()

            api_response.success.clear()
            api_response.errors.clear()
            api_response.message = "ECG Value uploaded to the Database"
            api_response.status = "Success"
            api_response.success.append('Data appended in the database')

            return make_response(api_response.to_json(), 200)

        except Exception as e:
            print(e)
            db.session.rollback()
            error = "Something went wrong please check the data again"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = e
            api_response.status = "Fail"

            return make_response(api_response.to_json(), 500)
