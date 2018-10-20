'''
Created on Oct 19, 2018

@author: peris
'''

import StringIO
import sys
import unittest
from logger import Logger

class TestLogger(unittest.TestCase):


    def testLoggerTrace(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        logger = Logger.getInstance('TestLogger', 'testLoggerTrace')
        logger.setLogLevel('trace')
        logger.trace('Hello World!')
        sys.stdout = sys.__stdout__
        print '\r--> ' + capturedOutput.getvalue() + '\r'

    def testLoggerDebug(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        logger = Logger.getInstance('TestLogger', 'testLoggerDebug')
        logger.setLogLevel('trace')
        logger.debug('Hello World!')
        sys.stdout = sys.__stdout__
        print '\r--> ' + capturedOutput.getvalue() + '\r'
    
    def testLoggerInfo(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        logger = Logger.getInstance('TestLogger', 'testLoggerInfo')
        logger.setLogLevel('trace')
        logger.info('Hello World!')
        sys.stdout = sys.__stdout__
        print '\r--> ' + capturedOutput.getvalue() + '\r'
    
    def testLoggerWarn(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        logger = Logger.getInstance('TestLogger', 'testLoggerWarn')
        logger.setLogLevel('trace')
        logger.warn('Hello World!')
        sys.stdout = sys.__stdout__
        print '\r--> ' + capturedOutput.getvalue() + '\r'

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogger']
    unittest.main()