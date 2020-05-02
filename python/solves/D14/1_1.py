class CustomException(Exception):

    def __init__(self,message):
        self.message = message

num = int(input())

try:
    if num < 10:
        raise CustomException("Input less tha 10")
    elif num > 10:
        raise CustomException('Input Greater than 10')
except CustomException as ce:
    print('The error raised: ' + ce.message)