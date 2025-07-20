import sys


def custom_message(error_message,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line = exc_tb.tb_lineno
    custom_error_msg = f"Error in file [{file_name}, line number [{line}], error is [{error_message}]]"

    return custom_error_msg




class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = custom_message(error_message,error_detail)

    def __str__(self):
        return self.error_message


