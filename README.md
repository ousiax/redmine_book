# redmine_book
A util writed with python to book time entry on redmine.

Usages:
    
    $ python book.py

You can also create a task on Windows with `schedule_task.bat`: 

    > schedule_task

Notes: Before execute *book.py*, please reset the corresponding setting item in the *settings.py*.

+ REDMINE_URL
+ REDMINE_KEY
+ ISSUE_ID
+ HOURS
+ ACTIVITY_ID
+ COMMENTS

Remark:
The file *get-pip.py* is download from [get-pip.py](https://bootstrap.pypa.io/get-pip.py get-pip)

Reference: 

1. [pip](https://pip.pypa.io/en/stable/ pip)
1. [Rest api - Redmine](http://www.redmine.org/projects/redmine/wiki/Rest_api_with_python "Using the REST API with Python")
