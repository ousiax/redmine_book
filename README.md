# Redmine book
A script writed with python to commit time entry on Redmine.

**Run with terminal**
    
    $ python book.py

**Schedule a task**

You can also schedule a task on Windows with `schedule_task.bat`: 

    > cd utils
    > schedule_task.bat

**Unschedule task**

Deletes the task with 'schedule_task.bat'

    > cd utils
    > unschedule_task.bat 

**Attention**

Before execute *book.py*, please reset the corresponding arguments in file *book.py* as follows:

    url = 'http://redmine.citicsinfo.com/redmine/'  # API URL
    key = '968aeb29e18dc64df3cd0d14b81c93f3e64ea9ff' # API访问键 (just for demo, not a valid authentication key.)

    time_entry = {
        'issue_id': 31080,
        'hours': 8,
        'activity_id': 9,
        'comments': random.choice([ # Choice a comment randomly to create the time entry.
            'FOO 产品系统设计开发',
            'BAR 产品系统设计开发',
            'BUZZ 产品系统设计开发',
        ]),
    }

**Appendix**

1. [Rest api - Redmine](http://www.redmine.org/projects/redmine/wiki/Rest_api_with_python "Using the REST API with Python")
