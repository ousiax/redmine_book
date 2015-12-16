# -*- encoding:utf-8 -*-
from datetime import date

from redmine import Redmine

import settings


def is_exist_today_entry(redmine):
    time_entries = redmine.time_entry.filter(
        issue_id=settings.ISSUE_ID, spent_on=date.today())
    return len(time_entries) >= 1


def is_weekday():
    return date.today().isoweekday() <= 5


def book():
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

    redmine = Redmine(settings.REDMINE_URL, key=settings.REDMINE_KEY)

    if not is_exist_today_entry(redmine):
        time_entry = create_today_time_entry(redmine)
        if time_entry.save():
            print('done, created today time entry sucessfully.')
    else:
        print('noop, time entry at today has been created')


def create_today_time_entry(redmine):
    time_entry = redmine.time_entry.new()
    time_entry.issue_id = settings.ISSUE_ID
    time_entry.hours = settings.HOURS
    time_entry.activity_id = settings.ACTIVITY_ID
    time_entry.comments = settings.COMMENTS
    return time_entry


def main():
    book()

if __name__ == '__main__':
    main()
