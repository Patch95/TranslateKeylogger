@echo off
@echo off
set "py=C:\Python27"

setx -m PYTHON_HOME %py%

set "scripts=\Scripts\"
set "pathScripts=%py%%scripts%"

setx -m Path %path%;%py%;%pathScripts%

pause
exit
