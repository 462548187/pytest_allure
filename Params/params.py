from Params import tools


def get_params(name):
    data = tools.get_page_list()
    param = data[name]
    return param


class AddEvent():
    param = get_params('AddEvent')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['data'][0])
        headers.append(param[i]['headers'])

class SelectEvent():
    param = get_params('SelectEvent')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['data'][0])
        headers.append(param[i]['headers'])

class DeleteEvent():
    param = get_params('DeleteEvent')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['data'][0])
        headers.append(param[i]['headers'])

if __name__ == '__main__':
    test = DeleteEvent()
    print(test.data)

