import requests

from Common.Session import Session


class Request():

    def __init__(self):
        self.session = Session()
        self.get_session = self.session.get_session()

    def request_get(self,url, params=None, headers=None):
        res = requests.get(url=url, params=params, headers=headers, cookies=self.get_session)
        return res

    def request_post(self, url, data, headers):
        res = requests.post(url=url, data=data, headers=headers, cookies=self.get_session)
        return res

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/api/get_event_list/'
    client = Request()
    res = client.request_get(url)
    print(res)