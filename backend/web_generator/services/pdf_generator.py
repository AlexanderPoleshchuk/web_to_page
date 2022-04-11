import logging
import uuid


from .generator_service import GeneratorService
from .tasks import celery_task_convert_url_to_pdf


class PdfGenerator:

    @staticmethod
    def convert_url_to_pdf(user_url: str, user_email: str) -> None:
        try:
            task_id = GeneratorService.create_new_task(user_email=user_email, user_url=user_url)
            finished_file_name = f'{user_email}_{str(uuid.uuid4())}.pdf'

        except Exception as error:
            logging.log(error)

        celery_task_convert_url_to_pdf.delay(task_id, finished_file_name)
