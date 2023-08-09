@echo off

rem Set the path to the root directory of your project
set "root_dir=%~dp0.."

echo Activating virtual environment...
call "%root_dir%\env\Scripts\activate"

echo Dumping data to backup.json...
python -Xutf8 "%root_dir%\manage.py" dumpdata --output="%root_dir%\backup\backup.json"

echo Deactivating virtual environment...
deactivate

echo Data dumped successfully.
pause

