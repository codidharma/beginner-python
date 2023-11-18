import traceback


class BaseCustomError(Exception):
    def __init__(self, errorCode, errorMessage):
        self.args = (errorCode, errorMessage)
        self.error_code = errorCode
        self.error_message = errorMessage

    def to_String(self):
        return f"Exception with code {self.error_code} and message {self.error_message}"

class SpecializedCustomError(BaseCustomError):
    def __init__(self, errorCode, errorMessage):
        self.args = (errorCode, errorMessage)
        self.error_code = errorCode
        self.error_message = errorMessage

    def to_String(self):
        return "I have overridden the exception message"

try:
    i = int(input("Enter any number"))

    if i == 1 :
        raise BaseCustomError(101, "I raised custom error")

    if i == 2:
        raise SpecializedCustomError(101, "I raised custom error1")

except ValueError as e:
    print(traceback.format_exception(e, e, e.__traceback__))
    print(e)

except BaseCustomError as e:
    print(e.to_String())

