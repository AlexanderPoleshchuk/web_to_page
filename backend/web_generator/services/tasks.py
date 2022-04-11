from .generator_service import GeneratorService
from .email_sender import EmailSender
# from celery.decorators import task
from celery import shared_task

@shared_task
def celery_task_convert_url_to_pdf(task_id: int, finished_file_name: str) -> None:
    GeneratorService.convert_user_url(task_id, finished_file_name)
    EmailSender.send_pdf(task_id)
