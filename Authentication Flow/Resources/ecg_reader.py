from Models.user_attr import User_attr
from Common.api_response import ApiResponse
from Common.init_database import db
from Resources.user_attr import FitbitUserAttrSchema

from PyPDF2 import PdfFileReader

from flask_restful import Resource
from flask_praetorian import auth_required, current_user
from flask import make_response, request

schema = FitbitUserAttrSchema()
api_response = ApiResponse()


class ReadECG(Resource):

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

            db.session.commit()

            api_response.success.clear()
            api_response.errors.clear()
            api_response.message = "ECG Value uploaded to the Database"
            api_response.status = "Success"
            api_response.success.append('Data appended in the database')

            return make_response(api_response.to_json(), 200)

        except Exception as e:
            db.session.rollback()
            error = "Something went wrong please check the data again"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = e
            api_response.status = "Fail"

            return make_response(api_response.to_json(), 500)
