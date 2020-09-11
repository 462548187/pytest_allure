from Params import tools


def get_params(name):
    data = tools.get_page_list()
    param = data[name]
    return param


class LoginSucess():
    param = get_params('LoginSucess')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['data'][0])
        headers.append(param[i]['headers'])

class LoginPasswordError():
    param = get_params('LoginPasswordError')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['data'][0])
        headers.append(param[i]['headers'])

class LoginPasswordNull():
    param = get_params('LoginPasswordNull')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['data'][0])
        headers.append(param[i]['headers'])

class LoginPasswordMiss():
    param = get_params('LoginPasswordMiss')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['data'][0])
        headers.append(param[i]['headers'])

if __name__ == '__main__':
    test = LoginSucess()
    print(test.data)

