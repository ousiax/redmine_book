# !/usr/bin/env python
# -*- encoding:utf-8 -*-

import random
from redmine_book import book


def main():
    '''The entry point to create a time entry.'''

    url = 'http://redmine.citicsinfo.com/redmine/'  # API URL
    key = '1a1a1a1a1a1a1a1aa1a1a1a1a1a1'  # API访问键

    time_entry = {
        'issue_id': 31080,
        'hours': 8,
        'activity_id': 9,
        'comments': random.choice([
            'foo',
            'bar',
            'buzz',
        ]),
    }
    try:
        book(url, key, **time_entry)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
