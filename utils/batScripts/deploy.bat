@echo off

rem Activate virtual environment
call env\Scripts\activate

setlocal enabledelayedexpansion

set "targetAdress="

for /f "tokens=2,3 delims={,}" %%a in ('"wmic nicconfig where IPEnabled="True" get DefaultIPGateway /value | find "I" "') do set gate_test=%%~a
set gate_test=!gate_test: =!
for /f "tokens=1-3 delims=^." %%i in ("!gate_test!") do set range=%%i.%%j.%%k
for /f "tokens=1,2 delims=:" %%l in ('ipconfig ^| findstr IPv4') do (
   set ip=%%m
   set ip=!ip: =!
   for /f "tokens=1-3 delims=^." %%n in ("!ip!") do set iprange=%%n.%%o.%%p
   if !iprange! == !range! set ipaddress=!ip!
)
set "targetAdress=!ipaddress!"

echo My IP Address is %targetAdress%

rem Run collectstatic
python manage.py collectstatic --noinput

rem Run the server with the dynamic IP
@REM python manage.py runserver %targetAdress%:8000

gunicorn -c gunicorn_config.py Saint_Stephen_School.wsgi:application --bind %targetAdress%:8000


endlocal
