'''
Python weekend
'''

import requests
import re
import lxml
from grab import Grab
import sys

def ver_pep8(code):
    '''
    Verify pep8
    '''
    g = Grab()
    results = []
    g.go('http://pep8online.com/checkresult', method='POST', post={'code':code})
    # print(g.doc.body)
    for idx, tr in enumerate(g.doc.tree.cssselect('#result_table > tbody > tr')):
        col = tr.cssselect('td')
        results.append({
            'code': str.strip(col[0].cssselect('span')[0].text),
            'line': str.strip(col[1].text),
            'col': str.strip(col[2].text),
            'text': str.strip(col[3].text)})

    return results

def main(code):

    results = ver_pep8(code)

    print('Code\tLine\tColumn\tText')
    for result in results:
        print('{:}\t{:}\t{:}\t{:}'.format(result['code'], result['line'], result['col'], result['text']))


if __name__ == '__main__':
    main(sys.argv[1])
