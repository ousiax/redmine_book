# !/usr/bin/env python
# -*- encoding:utf-8 -*-

from datetime import date
from redmine import Redmine
from . import settings


def is_exist_today_entry(redmine, issue_id):
    time_entries = redmine.time_entry.filter(
        issue_id=issue_id, spent_on=date.today())
    return len(time_entries) >= 1


def is_weekday():
    return date.today().isoweekday() <= 5


def book(url, key, **kwargs):
    '''
    The entry point method that book a new time entry on Redmine.
    url:
        The redmine rest api url.
        e.g. http://redmine.citicsinfo.com/redmine/

    key:
        The API key requires authentication.

    **kargs: A hash of the time entry attributes represnts a time_entry, including:
        issue_id :
            the issue id or project id to log time on
        spent_on (not used):
            the date the time was spent (default to the current date)
        hours (required):
            the number of spent hours
        activity_id:
            the id of the time activity.
        comments:
            short description for the entry (255 characters max)
    '''
    url = url.rstrip('/')
    issue_id = kwargs.get('issue_id')

    if not is_weekday():
        print('today is not weekday, do you want to continue. Y/N ?')
        for i in range(4):
            if i == 3:
                print('more than 3 times, failure.')
                return
            p = raw_input().lower()
            if p == 'y':
                break
            elif p == 'n':
                return
            else:
                print('Y/N ?')

    redmine = Redmine(url, key=key)

    if not is_exist_today_entry(redmine, issue_id):
        time_entry = create_today_time_entry(redmine, **kwargs)
        if time_entry.save():
            print('done, created today time entry sucessfully.')
    else:
        print('noop, time entry at today has been created')


def create_today_time_entry(redmine, **kwargs):
    time_entry = redmine.time_entry.new()
    time_entry.issue_id = kwargs.get('issue_id')
    time_entry.hours = kwargs.get('hours')
    time_entry.activity_id = kwargs.get('activity_id')
    time_entry.comments = kwargs.get('comments', None)
    return time_entry

def main():
    print('hello book')

if __name__ == '__main__':
    main()
