@echo off

set pri=%cd%

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

echo Creating Environment Variables

set actualPath=%cd%
set HeadPath=%actualPath:~0,3%

set "python=Python27\"
set "pythonPath=%HeadPath%%python%"

setx -m PYTHON_HOME %pythonPath%

set "scripts=Scripts\"
set "pathScripts=%pythonPath%%scripts%"

setx -m Path %path%;%pythonPath%;%pathScripts%

start validate.bat
exit