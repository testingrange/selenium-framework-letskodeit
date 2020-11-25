import inspect
import logging

def customLogger(logLevel=logging.DEBUG, fileName="automationTest"):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(str(fileName)+".log", mode='a') ###"{0}.log".format(loggerName)
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s- %(name)s- %(levelname)s - %(message)s', datefmt='=%a=%B=%W=\'%Z\' %m/%d/%Y %H:%M:%S')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger