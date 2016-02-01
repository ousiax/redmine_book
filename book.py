# !/usr/bin/env python
# -*- encoding:utf-8 -*-

from redmine_book import book


def main():
    '''The entry point to create a time entry.'''

    url = 'http://redmine.citicsinfo.com/redmine/'
    key = '2b548161789460c36b961f62edc2c391ddc15c7c'

    time_entry = {
        'issue_id': 31080,
        'hours': 8,
        'activity_id': 9,  
        'comments': '#31018: 资管MoM管理系统开发',
        }
    book(url, key, **time_entry)

if __name__ == '__main__':
    main()
