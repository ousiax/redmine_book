# !/usr/bin/env python
# -*- encoding:utf-8 -*-

from redmine_book import book


def main():
    '''The entry point to create a time entry.'''

    url = 'http://redmine.citicsinfo.com/redmine/'
    key = '968aeb29e18dc64df3cd0d14b81c93f3e64ea9ff'

    time_entry = {
        'issue_id': 29417,
        'hours': 8,
        'activity_id': 9,  
        'comments': '场外非标产品系统设计开发',
        }
    book(url, key, **time_entry)

if __name__ == '__main__':
    main()
