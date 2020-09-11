import requests


class Request():

    def request_get(self, url, params=None, headers=None, cookies=None):
        res = requests.get(url=url, params=params, headers=headers, cookies=cookies)
        return res

    def request_post(self, url, data=None, headers=None, cookies=None):
        res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
        return res

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/api/get_event_list/'
    client = Request()
    res = client.request_get(url)
    print(res)