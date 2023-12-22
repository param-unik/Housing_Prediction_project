import sys


class HousingException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_error_message(error_message, error_detail)

    @staticmethod
    def get_error_message(error_message: Exception, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        lineno = exc_tb.tb_frame.f_lineno
        error_msg = "Error occurred while executing the script -> [{0}] at line number : [{1}] with error message as - [{2}].".format(
            filename, lineno, str(error_message))
        return error_msg

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return HousingException.__name__.str()
