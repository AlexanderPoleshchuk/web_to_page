from django.http import HttpResponse, HttpResponseRedirect

from .check_data import CheckData
from .pdf_generator import PdfGenerator


class DataProcessing:

    @staticmethod
    def processing_request(user_url: str, user_email: str):
        validate_data = CheckData(user_url)

        if user_email:
            if user_url and validate_data.check_url():
                PdfGenerator.convert_url_to_pdf(user_url, user_email)

        return HttpResponseRedirect('')
