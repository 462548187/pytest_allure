import pytest
import allure
import requests

from Common.Request import Request
from Conf.Config import ReadConfig

@pytest.fixture()
def get_cookie():
    config = ReadConfig()
    base_url = config.host
    login_api = '/api/mgr/signin'
    data = {"username":"siuweide", "password":"123456"}
    response = Request().request_post(url=base_url+login_api, data=data)
    cookiejar = response.cookies
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    return cookiedict



