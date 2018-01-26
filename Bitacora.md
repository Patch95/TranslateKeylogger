# Bitácora

#### *Proyecto: Procesamiento y visualización de datos de keylogging*

# Fecha: 24 de enero del 2018

### Requerimientos:

 - Configurar ambiente personal de trabajo
 - Clonar repositorio de Roxana 
 - Verificar si es posible ejecutar el researchlogger en windows 10.
 
### Informe de Trabajo
 
 + Se instaló Pycharm (con licencia estudiantil ) como editor de python.
 	- https://www.jetbrains.com/pycharm/download/#section=windows
 + Se intaló git en windows para control de versiones.
 	- https://git-scm.com/download/win
 + Se instaló python 2.7.14
    - https://www.python.org/downloads/release/python-2714/
 + Se clonó el repositorio de Roxana
 + Finalmente se intentó cumplir con las dependencias del researchlogger:
    - validate [sudo pip install validate]
    - Xlib [sudo apt-get install python-xlib]
    - Python Image Library (PIL) [sudo apt-get install python-pil]
    - gtk [sudo apt-get install python-gtk2]
  + Se instaló pip
 
 # Fecha: 25 de enero del 2018

### Requerimientos:

 - Verificar si es posible ejecutar el researchlogger en windows 10.
 
### Informe de Trabajo
 
 + Se necesita instalar el kit keylogger para python7
 + Se instaló pygtk-all-in-one-2.24.0.win32-py2.7:
    - https://github.com/fuzeman/Catalytic/raw/master/dependencies/win32/pygtk-all-in-one-2.24.0.win32-py2.7.msi
 + Se instaló PIL-1.1.7.win32-py2.7:
    - http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe
 + Se instaló pyhook:
    - https://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/pyHook-1.5.1.win32-py2.7.exe/download
 + Se instalo pywin32-219:
    - https://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download
 + se instaló configobj:
    - Navegar por la linea de comandos hasta el directorio de configobj.
    - escribir 
        ```sh
        $ setup.py install
        ```
 + Se instaló el researchlogger
    - Ir a la carpeta de Researchlogger
    - escribir 
        ```sh
        $ setup.py install
        ```
 + se realizo la instación con exito.
 + Finalmente se comenzo generar un archivo .bat el cual realizará la instalación de manera más facil para un usuario no experto.

     