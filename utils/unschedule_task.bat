@rem Forcefully deletes the task 'Redmine Book' and suppresses warnings if the specified task is currently running.
schtasks /delete /tn "Redmine Book" /F