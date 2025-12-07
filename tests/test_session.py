import sys
import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_PATH)
from src.quizsession.session import QuizSession, pickQuestions, loadAllQuestions, loadUsers, selectUser
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta

class TestQuizSession(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_questions = [
            {"qid": "q1", "qtext": "this is q1", "qtitle": "mcq", "qtype": "MC", "qoptions": ["2"], "qanswer": "2"}, 
            {"qid": "q2", "qtext": "this is q2?", "qtitle": "tfq", "qtype": "TF", "qanswer": "T"}, 
            {"qid": "q3", "qtext": "this is q3", "qtitle": "saq", "qtype": "SA", "qanswer": "answer"}
        ]
        print("Set up Class")

    @classmethod
    def tearDownClass(cls):
        cls.mock_questions = None
        print("Tear down Class")

    def setUp(self):
        self.session = QuizSession(
            user_id="u1",
            user_name="name1",
            num_questions=[1, 1, 1],
            question_ids=["q1", "q2", "q3"]
        )
        self.all_questions = TestQuizSession.mock_questions
        print("Set up")

    def tearDown(self):
        self.session = None
        self.all_questions = None
        print("Tear down")


if __name__ == "__main__":
    unittest.main()
