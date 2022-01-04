import requests

from .conf import ALLURE_USERNAME, ALLURE_PASSWORD, ALLURE_AUTH, ALLURE_PROJECTS_INFO
from .handlers import AllureAccessToken, AllureContent
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_allure_token():
    payload = {
        "username":ALLURE_USERNAME,
        "password":ALLURE_PASSWORD,
        "grant_type":"password",
        "scope":"openid"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", ALLURE_AUTH, headers=headers, data=payload, verify=False)

    return AllureAccessToken(**response.json()).access_token


def get_coverage_count(automated_count: int, manual_count: int) -> float:
    coverage_count = automated_count / (manual_count + automated_count) * 100
    return round(coverage_count, 2)


def get_allure_project_info(token: str):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request("GET", ALLURE_PROJECTS_INFO, headers=headers, data={}, verify=False)
    raw_data = response.text
    projects = AllureContent.parse_raw(raw_data).content
    return projects
