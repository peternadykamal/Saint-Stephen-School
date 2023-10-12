@echo off

echo Batch Script: Starting...

:: Activate virtual environment
echo Activating virtual environment...
call env\Scripts\activate

:: Run collectstatic
echo Running collectstatic...
python manage.py collectstatic --noinput

:: Get the parent directory of the virtual environment folder
for %%I in ("%VIRTUAL_ENV%") do set "workspace_dir=%%~dpI"

:: Get the directory where the script is located
set "script_dir=%~dp0"
set "nginx_config=%script_dir%nginx.conf"

set "nginx_folder=%script_dir%nginx-windows"
set "nginx_exe=%nginx_folder%\nginx.exe"

:: Change to the nginx folder and execute nginx
echo Starting nginx...
pushd "%nginx_folder%"
pushd "%nginx_folder%\conf"
:: replace every \ with /
set "workspace_dir=%workspace_dir:\=/%"
:: Remove the trailing slash if present
if "%workspace_dir:~-1%"=="/" set "workspace_dir=%workspace_dir:~0,-1%"
echo %workspace_dir%
call format_conf.bat "%workspace_dir%"
popd
start /B "" "%nginx_exe%"
popd

:: create these folder if they don't exsit
mkdir "%nginx_folder%\temp\uwsgi_temp" 2>nul
mkdir "%nginx_folder%\temp\scgi_temp" 2>nul
mkdir "%nginx_folder%\temp\proxy_temp" 2>nul
mkdir "%nginx_folder%\temp\fastcgi_temp" 2>nul
mkdir "%nginx_folder%\temp\client_body_temp" 2>nul

:: run waitress
echo Starting waitress...
start /B "" python .\utils\batScripts\waitress_config.py

:: Get the PID of the Python process
for /F "TOKENS=1,2,*" %%a in ('tasklist /FI "IMAGENAME eq python.exe"') do (set waitressPID=%%b)

echo Batch Script: Press any key to exit...
pause > nul

:: Execute cleanup commands before exiting
echo Batch Script: Cleaning up...

:: Terminate nginx
echo Terminating nginx...
taskkill /f /im nginx.exe

:: Terminate waitress
echo Terminating waitress...
taskkill /PID %waitressPID% /F

echo Batch Script: Exiting...
exit