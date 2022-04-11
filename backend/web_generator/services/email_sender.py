import logging

from django.db import DatabaseError, transaction
from django.core.mail import EmailMessage
from ..models import ApplicationProcessing


class EmailSender:

    @staticmethod
    def send_pdf(task_id: int) -> None:
        try:
            with transaction.atomic():
                new_task = ApplicationProcessing.objects.get(task_id=task_id)

                user = new_task.user.email
                url = new_task.finished_file.url

                mail = EmailMessage(subject='W2P generator', body=f'Dear, {user}\n\nIt is your file:\n{url}', to=[user])
                mail.send()

                new_task.status = 'Finish'
                new_task.save()

        except DatabaseError as error:
            logging.error(error)
        except Exception as error:
            logging.error(error)
