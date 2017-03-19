'''

'''

import requests
import re
import lxml
from grab import Grab
import sys


def main():
    '''

    '''

    code = 'a=1'

    g = Grab()
    results = []
    for i in range(1):
        g.go('http://127.0.0.1:5000/', method='GET')
        # g.go('http://127.0.0.1:5000/check_pep8', method='POST', post={'code':code})
    # print(g.doc.body)


if __name__ == '__main__':
    main()
