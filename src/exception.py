import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb:
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = (
            f"Error occurred in Python script: [{file_name}] "
            f"line number: [{exc_tb.tb_lineno}] "
            f"Error message: [{str(error)}]"
        )
    else:
        error_message = f"Error message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)
        
    def __str__(self):
        return self.error_message
