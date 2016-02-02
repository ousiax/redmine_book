# redmine_book
A script writed with python to commit time entry on Redmine.

Usages:
    
    $ python book.py

You can also schedule a task on Windows with `schedule_task.bat`: 

    > cd utils
    > schedule_task.bat

(**Deletes** the task with 'schedule_task.bat')

    > cd utils
    > unschedule_task.bat 

**Notes**: Before execute *book.py*, please reset the corresponding arguments in file *book.py* as follows:

    url = 'http://redmine.citicsinfo.com/redmine/'
    key = '968aeb29e18dc64df3cd0d14b81c93f3e64ea9ff' # just for demo, not a valid authentication key.

    time_entry = {
        'issue_id': 29417,
        'hours': 8,
        'activity_id': 9,  
        'comments': '场外非标产品系统设计开发',
        }

Appendix:

1. [Rest api - Redmine](http://www.redmine.org/projects/redmine/wiki/Rest_api_with_python "Using the REST API with Python")
