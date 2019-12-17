# Programming components
def logger(func):
    def wrapper():
        print('Logging Execution')
        func()
        print('Done Logging')
    return wrapper


@logger
def sample():
    print('--Inside Sample Function')
    
sample()