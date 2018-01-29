@echo off
echo Welcome to ResearchLogger Instalation

echo Installing dependencies

echo Installing python
START /WAIT python-2.7.14.msi
echo Python installed

echo Installing pygtk
start /WAIT pygtk-all-in-one-2.24.0.win32-py2.7.msi
echo pygtk installed

echo Installing PIL
start /WAIT PIL-1.1.7.win32-py2.7.exe
echo PIL installed

echo Installing pyHook
start /WAIT pyHook-1.5.1.win32-py2.7.exe
echo pyHook installed

echo Installing pywin32
start /WAIT pywin32-219.win32-py2.7.exe
echo pywing installed

echo Installing configobjg
start /WAIT configobj-4.7.2\setup.py
echo configobj installed

echo Dependencies installed

echo Copying files ...
set actualPath=%cd%
set HeadPath=%actualPath:~0,3%

move ResearchLogger %HeadPath%

echo ReasearchLogger located in:
echo.%HeadPath%

pause

set "python=Python27\"
set "pythonPath=%HeadPath%%python%"

set "libOrigin=Lib\site-packages\pywin32_system32\pywintypes27.dll"
set "libDestination=Lib\site-packages\win32\"

set "pathOrigin=%pythonPath%%libOrigin%"
set "pathDestination=%pythonPath%%libDestination%"

copy  %pathOrigin% %pathDestination%

echo Files copied

start environmentVariables.bat

Echo Instalation finished!!!
exit