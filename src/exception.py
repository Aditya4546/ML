import os
import sys
import logging

# Your code using os and sys functions here
def error_message_details(error: str, error_detail) :
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in script: {file_name}  line number: {exc_tb.tb_lineno}  error message: {error} "
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail=sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message

