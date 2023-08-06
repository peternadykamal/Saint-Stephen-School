@echo off

@REM this line for task.json to work correctly
cd .\users\tests

set "CALLING_DIRECTORY=%CD%"
set "TEST_FOLDER=%CALLING_DIRECTORY%\%1"
cd ..\..\

:: Set the environment variables (modify the path as needed)
set PYTHON_ENV= .\env\Scripts\activate

:: Check if the virtual environment exists
if not exist %PYTHON_ENV% (
    echo Virtual environment not found. Please create and activate the virtual environment first.
    exit /b 1
)

echo %TEST_FOLDER%
echo %PYTHON_ENV%

:: Create the test folder and fixtures subfolder if they don't exist
mkdir "%TEST_FOLDER%\fixtures" 2>nul

:: Activate the virtual environment
call %PYTHON_ENV%

:: Run the Django dumpdata commands with the specific fixture folder
python -Xutf8 manage.py dumpdata auth.User --indent 2 > "%TEST_FOLDER%\fixtures\UserData.json"
python -Xutf8 manage.py dumpdata users.Profile --indent 2 > "%TEST_FOLDER%\fixtures\ProfileData.json"
python -Xutf8 manage.py dumpdata users.Address --indent 2 > "%TEST_FOLDER%\fixtures\AddressData.json"
python -Xutf8 manage.py dumpdata users.TalmzaLevel --indent 2 > "%TEST_FOLDER%\fixtures\TalmzaLevelData.json"
python -Xutf8 manage.py dumpdata users.SchoolLevel --indent 2 > "%TEST_FOLDER%\fixtures\SchoolLevelData.json"
python -Xutf8 manage.py dumpdata users.UserPermissionTag --indent 2 > "%TEST_FOLDER%\fixtures\UserPermissionTagData.json"

:: Deactivate the virtual environment
deactivate
