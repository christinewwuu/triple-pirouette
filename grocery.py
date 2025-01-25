from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()  # load API key value from .env file

def get_value(param=""):
    request_url = f""