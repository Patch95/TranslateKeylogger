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

# Fecha: 26 de enero del 2018

### Requerimientos:

 - Terminar el instalador de ResearchLogger para windows.
 
### Informe de Trabajo
 
 + Se genero el script ResearchLoggerInstaler.bat
 + En el primer segmento de el script se birnda ayuda para instalar los programas que se ocupan para que se ejecute el research logger
 + En la parte final del script se copian los archivos necesarios para que funcione el research logger
 + Finalmente se ubica la carpeta ResearchLogger en el directorio raíz:
    - C:\
 + Links de apoyo:
    - https://github.com/Southpaw-TACTIC/Team/tree/master/src/python/Lib/site-packages/pywin32_system32
    - https://es.osdn.net/projects/sfnet_ascend-sim/downloads/thirdparty/py2cairo-1.10.0.win-amd64-py2.7.exe/
    - http://www.pythonware.com/products/pil/
    - https://github.com/fuzeman/Catalytic/blob/master/dependencies/win32/pygtk-all-in-one-2.24.0.win32-py2.7.msi
    - https://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/
    - https://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/
    
 
 # Fecha 28 de enero del 2018
 
 ### Requerimientos:
 
 - Solucuionar el problema de las variables de ambiente.
 
 ### Informa de Trabajo 
 + Ingresar las variables de ambiente "C:\Python27" y "C:\Python27\Scripts\" requiere permisos de administrador, pero si se inicia el script con dichos permisos el directorio de ejecución cambia a C:\windows\system32,por lo que no es posible ubicar los ejecutables a llamar.
 + Se optó por realizar dos scripts, esto para que ambos puedan ser ejecutados sin permisos de administrador
 + Links de apoyo:
    - https://stackoverflow.com/questions/1894967/how-to-request-administrator-access-inside-a-batch-file
    - https://www.windows-commandline.com/set-path-command-line/
    - https://stackoverflow.com/questions/3803581/setting-a-system-environment-variable-from-a-windows-batch-file
    - https://www.dostips.com/DtTipsStringManipulation.php
    
 # Fecha 29 de enero del 2018
 
 ### Requerimientos:
  
 - Depuración de instalador
 - Pruebas de instalador
 
 ### Informa de Trabajo 
 
 + Finalmente se optó por realizar 3 scripts:
    1. ResearchLoggerInstaller: este se encarga de llamar a los diferentes intaladores que son necesarios para que el researchlogger funcione correctamente.
    2. EnvironmentVariables: este se encarga de escribir las variables de entorno necesarias para qur python sea accesible desde terminal y para que se pueda hacer uso del comando pip que se necesita para el ultimo script.
    3. validate: Este script se encarga de instalar la biblioteca validate de python.
 + Se realizó el README de instalación, se especifica que script deben ser ejecutados y de que forma.
 + Se asigno la lecura ApuntesPaula para investigación, se comenzó a leer y a comprender durante el día.
 
 
 # Fecha 30 de enero del 2018
 
 ### Requerimientos:
  
 - Pruebas de instalador
 - Lectura de folleto ApuntesPaula
 - Lectura de Tesis de Keylogging para el estudio de los procesos cognitivos del traductor, Rozana Anabel Lafuente
 -
 
 ### Informa de Trabajo 
 
 + Se utilizaron dos sujetos de prueba para testear el script de instalación, Jose Roerto Argueddas y Randall Araya Campos.
    - El primer sujeto de prueba completo el tutorial de instalación con exito, como retroalimentación sugerió realizar dos instaladores 1 con detalles tecnicos (el que actualmente existe) y otro que tenga screenshots y mas detalles de la instalación.
    - El segundo sujeto de prueba selecciono la opción de reinicio por error, en caso de que esto suceda el script puede correrse nuevamente solo que la instalación de python debe cancelarse la segunda vez que se ejecuta ya que este ya estaria instalado.
 + Se leyó el folleto ApuntesPaula y se generaron dudas que deben ser consultadas con paula
 + Se leyó la Tesis de Keylogging para el estudio de los procesos cognitivos del traductor, Rozana Anabel Lafuente, se hizo apuntes de la lectura y también se generaron dudas.
 
# Fecha 31 de enero del 2018
 
 ### Requerimientos:
  
 - Reunión con usuario no experto para instalación de researchlogger
 
 ### Informa de Trabajo 
 
 + Se tuvo una reunión con una señorita que se encuentra en España, reunión virtual, en la cual se testeo el script de instalación para windows.
 + Durante la instalación hubo un error con las variables de entorno, que se solucionó por medio de teamviewer.
 + Finalmente se asigno la revision del folleto ApuntesPaula contra la estructura de los logs.
 
 # Fecha 01 de enero del 2018
 
 ### Requerimientos:
  
 - No aplica
 
 ### Informa de Trabajo 
 
 + No se trabajó por motivos de enfermedad.
 
 # Fecha 02 de enero del 2018
 
 ### Requerimientos:
  
 - Reunión en FaMAF
 
 ### Informa de Trabajo 
 
 + Se llevó a cabo la priera reunion en conjunto con Paula Estrella, Aurelio Sanabria y María Estrada.
 
 # Fecha 03 de enero del 2018
 
 ### Requerimientos:
  
 - Realizar documento de factibilidad de transformación de los logs de ResearchLogger
 
 ### Informa de Trabajo 
 
 + Se realizó el documento
 + Se acordó generar consultas para ricardo
 + Se asigno la tarea de comenzar a generar una pequeña visualización del log de clicks y de teclas mezclados.
 