import requests
import logging


class CheckData:

    def __init__(self, user_url: str) -> None:
        self.user_url = user_url

    def check_url(self) -> bool:
        try:
            requests.get(self.user_url)
            return True
        except requests.exceptions.ConnectionError as error:
            logging.error(error)
            return False
