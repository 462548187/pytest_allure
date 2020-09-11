from Params import tools


def get_params(name):
    data = tools.get_page_list()
    param = data[name]
    return param


class SelectCustomerLostCookie():
    param = get_params('SelectCustomerLostCookie')
    print(param)
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['params'][0])
        headers.append(param[i]['headers'])

if __name__ == '__main__':
    test = SelectCustomerLostCookie()
    print(test.data)

