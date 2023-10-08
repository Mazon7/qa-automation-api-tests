# constants.py

"""This module defines project-level constants."""

from dotenv import load_dotenv
import os

load_dotenv('.env')

URL = os.getenv('URL')
URL_QA = os.getenv('URL_QA')
QA_EMAIL = os.getenv('QA_EMAIL')
QA_PASSWORD = os.getenv('PASSWORD')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
URL_DEV = os.getenv('URL_DEV')
TEST_PASS = os.getenv('TEST_PASS')