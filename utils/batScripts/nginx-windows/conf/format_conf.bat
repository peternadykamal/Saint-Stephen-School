@echo off
setlocal enabledelayedexpansion
REM Check if an argument was provided
if "%~1" == "" (
    echo Usage: %0 "replacement_text"
    exit /b 1
)

REM Input and output file paths
set "inputFile=nginx_template.conf"
set "outputFile=nginx.conf"

REM Read the input file, replace placeholder, and write to the output file
(for /f "delims=" %%a in ('type "%inputFile%"') do (
    set "line=%%a"
    set "line=!line:{workspace}=%~1!"
    echo !line!
)) > "%outputFile%"

echo File generated: %outputFile%