import unittest
import sys
import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_PATH)

from test_session import TestQuizSession
from test_result import TestQuizResult
from test_question import TestQuestion
from test_question_manager import TestQuestionManager
from test_user import TestUserClasses
from test_user_manager import TestUserManager

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestQuizSession))
    suite.addTests(loader.loadTestsFromTestCase(TestQuizResult))
    suite.addTests(loader.loadTestsFromTestCase(TestQuestion))
    suite.addTests(loader.loadTestsFromTestCase(TestQuestionManager))
    suite.addTests(loader.loadTestsFromTestCase(TestUserClasses))
    suite.addTests(loader.loadTestsFromTestCase(TestUserManager))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())