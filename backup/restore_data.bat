@echo off

rem Set the path to the root directory of your project
set "root_dir=%~dp0.."

echo Activating virtual environment...
call "%root_dir%\venv\Scripts\activate"

echo Restoring data from backup...
python "%root_dir%\manage.py" loaddata "%root_dir%\backup\backup.json"

echo Deactivating virtual environment...
deactivate

echo Data restore complete.
pause
