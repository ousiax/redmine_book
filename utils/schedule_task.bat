@rem Create a daily task on windows task scheduler.

@rem Set pythonexe variable of python executable file full path.
@python -c "import sys; print sys.executable" > pythonexe.tmp
@set /p pythonexe= < pythonexe.tmp
@del pythonexe.tmp

@rem Install Pip
@rem @python "get-pip.py"

@rem Install Python-Redmine
@rem @pip install python-redmine --index-url="https://pypi.mirrors.ustc.edu.cn/simple"

@rem Create a task to windows task scheduler
@for %%i in ("%~dp0..") do @set "book_py=%%~fi\book.py"
@schtasks /create /tr "'%pythonexe%' \"%book_py%" /sc daily /tn "Redmine Book"  /st 15:00 /ru system /rl highest /f