@rem Create a daily task on windows task scheduler.

@rem Add path to Python Binaries
@set "PythonPath="
@if exist "C:\Python27\" set "PythonPath=C:\Python27\"
@if exist "%ProgramFiles%\Python27\" set "PythonPath=%ProgramFiles%\Python27\"
@if exist "%ProgramFiles(x86)%\Python27\" set "PythonPath=%ProgramFiles(x86)%\Python27\"

@schtasks /create /tr "'%PythonPath%Python.exe' \"%CD%\book.py\"" /sc daily /tn "Redmine Book"  /st 15:00 /ru system /rl highest /f