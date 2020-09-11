# -*- coding: utf-8 -*-
import yaml
import os
import os.path

def parse():
    param_paths = ['/login',  '/customer']
    pages = {}
    for param_path in param_paths:
        file_path = os.path.dirname(__file__) + param_path
        for root, dirs, files in os.walk(file_path):
            for name in files:
                watch_file_path = os.path.join(root, name)
                with open(watch_file_path, encoding='utf-8') as f:
                    page = yaml.safe_load(f)
                    pages.update(page)
    return pages

def get_page_list():
    page_list = {}
    pages = parse()
    for page, value in pages.items():
        parameters = value['parameters']
        data_list = []

        for parameter in parameters:
            data_list.append(parameter)
        page_list[page] = data_list
    return page_list

if __name__ == '__main__':
    list = get_page_list()
    print(list)
