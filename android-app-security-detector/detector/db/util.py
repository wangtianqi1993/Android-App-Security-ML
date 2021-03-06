#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


def get_permissions_from_google():
    """
    Read permissions from google android site
    :return:
    """
    with open('permissions.html') as f:
        html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        permissions = []
        for td in soup.find_all('td', class_="jd-linkcol"):
            permissions.append(td.next_element.contents[0])
        return permissions

if __name__ == '__main__':
    print get_permissions_from_google()
