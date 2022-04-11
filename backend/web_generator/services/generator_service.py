import os
import logging
import uuid

import pdfkit

from django.db import DatabaseError, transaction
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

from ..models import UrlResource, ApplicationProcessing


class GeneratorService:

    @staticmethod
    def create_new_task(user_email: str, user_url: str) -> int:
        try:
            with transaction.atomic():
                receiver, _ = User.objects.get_or_create(username=user_email, email=user_email)

                if user_url:
                    user_url, _ = UrlResource.objects.get_or_create(url=user_url)

                task_id = str(uuid.uuid4())

                new_request = ApplicationProcessing(user=receiver, user_url=user_url, task_id=task_id, status='Data loading')
                new_request.save()
                return task_id

        except DatabaseError as error:
            logging.error(error)
        except Exception as error:
            logging.error(error)
        return str(uuid.uuid4())

    @staticmethod
    def convert_user_url(task_id: int, finished_file_name: str) -> None:

        receiver = ApplicationProcessing.objects.get(task_id=task_id)
        receiver.status = 'In progress'

        # with open(f'{finished_file_name}', 'w+b') as temp_pdf:
        #     pass

        pdfkit.from_url(receiver.user_url.url, f'{finished_file_name}')

        with open(f'{finished_file_name}', 'rb') as temp_pdf:
            receiver.finished_file = ContentFile(temp_pdf.read(), f'{finished_file_name}')

        receiver.save()
        os.remove(f'{finished_file_name}')
