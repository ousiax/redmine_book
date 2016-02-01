@rem Create a daily task on windows task scheduler.

@rem Set pythonexe variable of python executable file full path.
@python -c "import sys; print sys.executable" > pythonexe.tmp
@if %errorlevel% neq 0 goto :error_no_Python
@set /p pythonexe= < pythonexe.tmp
@del pythonexe.tmp

@rem Create a task to windows task scheduler
@for %%i in ("%~dp0..") do @set "book_py=%%~fi\book.py"
@schtasks /create /tr "'%pythonexe%' \"%book_py%" /sc daily /tn "Redmine Book"  /st 15:00 /ru system /rl highest /f
@goto :end

@rem -----------------------------------------------------------------------------------
:error_no_Python
@echo ERROR: Cannot determine the location of the Python installation.
@goto :end

:end