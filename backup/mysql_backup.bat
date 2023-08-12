rem Save the current working directory (batch file location)
set "backup_path=%~dp0"

rem Check if two command-line arguments are provided
if "%~1"=="" (
    echo Usage: %~nx0 database_name
    exit /b 1
)

rem path to mysql server bin folder
cd /d "C:\Program Files\MySQL\MySQL Server 8.0\bin"

rem credentials to connect to mysql server
set mysql_user=admin
set mysql_password=talmza5678

set "database_name=%~1"

rem backup creation
@REM mysqldump.exe --user=%mysql_user% --password=%mysql_password% --databases %database_name% --result-file="%backup_path%\%database_name%.sql"
mysqldump --defaults-file="%backup_path%\my.cnf" --databases %database_name% --result-file="%backup_path%\%database_name%.sql"

