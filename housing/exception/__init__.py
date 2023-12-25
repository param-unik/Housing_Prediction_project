import sys


class HousingException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_error_message(error_message, error_detail)

    @staticmethod
    def get_error_message(error_message: Exception, error_detail: sys) -> str:
        _, _, exec_tb = error_detail.exc_info()
        filename = exec_tb.tb_frame.f_code.co_filename
        try_block_line_number = exec_tb.tb_lineno
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        error_msg = f"""
                    Error occurred while executing the script -> 
                    [{filename}] at 
                    try block line number  -> [{try_block_line_number}] and exception block line number  -> [{exception_block_line_number}]
                    with error message as >>>>  [{error_message}] 
                    """
        return error_msg

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return HousingException.__name__.str()
