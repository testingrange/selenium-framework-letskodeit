"""
@ util package

Util class implementation
All most commonly used utilitites should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""

import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specific amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()
            self.log.error("Waiting for '" + str(sec) + "' seconds not possible to proceed")

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters
        :param length: Length of string, number of characters string should have
        :param type: Type of characters string should have. Default is letters
        Provide lower/upper/digits for different types
        :return:
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids
        :param listSize: Number of email ids. Default is 5 email in a list
        :param itemLength: It should be a list containing number of items equal to the listSize
                           This determines the length of the each item i the list -> [1, 2, 3, 4, 5]
        """
        nameList = []
        for i in range(listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList


    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual text From Application Web UI --> :: " + actualText)
        self.log.info("Expected text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual text From Application Web UI --> :: " + actualText)
        self.log.info("Expected text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCH !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches
        :param expectedList:  Expected list
        :param actualList:  Actual list
        :return:

        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elemetns of expected list
        Parameters:

        :param expectedList: Expected list
        :param actualList: Actual List
        :return:
        """
        length = len(expectedList)
        for i in range(length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True