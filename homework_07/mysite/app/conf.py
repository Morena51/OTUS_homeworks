import os

from dotenv import load_dotenv

load_dotenv()

ALLURE = 'https://allure.sbercloud.tech'
ALLURE_PROJECTS_INFO = 'https://allure.sbercloud.tech/api/rs/project/summary?name=&page=0&size=20'
ALLURE_AUTH = "https://allure.sbercloud.tech/api/uaa/oauth/token"
ALLURE_USERNAME = os.getenv("ALLURE_USERNAME")
ALLURE_PASSWORD = os.getenv("ALLURE_PASSWORD")
