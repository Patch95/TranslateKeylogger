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
 
 # Fecha 05 de enero del 2018
 
 ### Requerimientos:
  
 - Realizar documento de factibilidad de transformación de los logs de ResearchLogger
 
 ### Informa de Trabajo 
 
 + Se realizó el documento
 + Se acordó generar consultas para ricardo
 + Se asigno la tarea de comenzar a generar una pequeña visualización del log de clicks y de teclas mezclados.
 
 # Fecha 06 de enero del 2018
 
 ### Requerimientos:
  
 - Realizar consultas para Ricardo
 - Realizar pruebas de script de Jose Roberto Arguedas en windows
 - Realizar Chequeo de anteproyecto
 
 ### Informa de Trabajo 
 
 + En conjunto con Jose Roberto Arguedas se testeo el script de manejo de clicks y de toma de imagenes.
    + Se realizó una máquina virtual de windows 10
    + Se instaló el research logger con la ayuda del KitResearchLogger anteriormente creado
    + Se instalaron las bibliotecas necesarias
    + Se cedió el uso de mi computadora a Jose Roberto Arguedas para que este pudieraa realizar los test necesarios.
 + Para que haya un entendimiento más adecuado para Ricardo se instaló microsoft office 2013 para generar las consultas de mejor manera.
 + Se revisaron los documento de anteproyecto necesarios para el Tecnológico de Costa Rica.
 
 # Fecha 07 de enero del 2018
 
 ### Requerimientos:
  
 - Realizar consultas para Ricardo
 - Clonar repositorio de Roxana Lafuente ResearchAnalyser
 - Probar mixed_parse.py de ResearchAnalyser
 
 ### Informa de Trabajo 
 
 + Se realizarón las consultas en el documento de ricardo a manera de comentarios en word.
 + Se clonó el repositorio
 + Se necesito instalar las siguiente dependencias:
    + termcolor [sudo apt-get install python-termcolor]
    + matplotlib
    + colour [pip install colour]
    + Python Image Library (PIL) [sudo apt-get install python-pil]
    + nltk [sudo pip install nltk]
 + Se probó el mixed_parser:
    + No es funcional con los logs de windows, error aún no encontrado.
  
 # Fecha 08 de enero del 2018
 
 ### Requerimientos:
  
 - Chequear error de mixed_parser.py
 - Revisión de logs
 
 ### Informa de Trabajo 
 
 + Se chequeó el error generado por el mixed_parser:
    + Se concluye que, en el log, la falta de X,Y del mouse cuando se presiona una tecla es la causa del fallo, ya que los separadores para comprender la información generar mal los datos si estos datos no estan.
    + Se compararón los log de windows y de ubuntu:
        + Los logs de ubuntu no generan el nombre de las pestañas de los navegadores.
    + Se descargo e instaló windows 7 en una maquina virtual esto para realizar pruebas con el researchlogger y ver si NO genera X,Y coomo en windows 10
        + Se concluye que en windows 10 y 7 no se generan los x,y
        
 # Fecha 09 de enero del 2018
 
 ### Requerimientos:
  
 - Reunión semanal con Aurelio Sanabria y María Estrada
 
 ### Informa de Trabajo 
 
 + La reunión con Aurelio y Maria Estrada no se llevó acábo, por lo cual solo se tuvo una reunión con Paula Estrella
 + En la reunion se acordo lo siguiente:
    + Los logs serán visualizados en un dashboard, se necesita definir que datos pueden generarse y como se puede mostrar la información
    + Se necesita corregir el mixed_parser ya que es necesario trabajar con logs de windows, se sugiere que no se pidan las variables x,y una vez que se carguen los logs.
 + Se intentó NO solicitar las variables x,y pero el script aún falla, realizando más investigación, se concluyó que los logs en windows se generan también con el siguiente error:
    + "key_down" y "key_up" no tiene la raya baja "_" por lo cual aparecen de la siguiente forma "key down" "key up"
 + Debido a todos estos problemas se optará por realizar un script en python que revise la estructura de los logs generados y que haga correciones si es necesario.
 
 # Fecha 11 de Febrero del 2018
 
 ### Requerimientos:
  
 - No aplica
 
 ### Informa de Trabajo 
 
 + No se trabajó por día Feriado.
 
 # Fecha 12 de Febrero del 2018
 
 ### Requerimientos:
  
 - No aplica
 
 ### Informa de Trabajo 
 
 + No se trabajó por día Feriado.
 
 # Fecha 13 de Febrero del 2018
 
 ### Requerimientos:
  
 - Reunión con supervisor de práctica profesional
 
 ### Informa de Trabajo 
 
 + Se realizó una reunión con Aurelio sanabria en la cual se expusieron dudas con respecto al proyecto de invesigación.
 + Revisión de los logs, se propondrá la idea de realizar un Chequeador de scripts el cual verifique si cada uno de los espacios correspondientes al detailedlog son correctos.

 # Fecha 14 de Febrero del 2018
 
 ### Requerimientos:
  
 - Reunión con Paula estrella
 - Consulta de Proyecto de investigación
  
 ### Informa de Trabajo 
 
 + En FAMAF se llevó acabo una reunion en la cual se consulto la viabilidad actual del proyecto de investigación y dudas con respecto a desarrollo:
    + Se acordo continuar con el rumbo actual del proyecto, ya que no afecta al cronograma ni a la extension del mismo
    + Con respecto al desarrollo se simplifico la realización del scriptchecker, se acordo solo modificar los datos que estuvieran erroneos
    + Se necesita chequear si es posible mostrar:
        + Tiempo total de sesión
        + Tiempo por herramienta
        + Tiempo por recurso
        + Combinaciones de teclas
 + Se generó el script adminfile.py para manejo de archivos
 + Se creó la función arranger la cual cambia en el detailedlog "key down" y "keyup" por "key_down" y "key_up" y genera un nuevo archivo con el identificador _new
 + Una vez que se ejecutó el mixed_parser con el log modificado se descubrio que el archivo clickimagelogfile también posee un error simmilar en windows el cual es que "mouse left up" y "left_up" deben ser cambiados por "mouse left down" y "left_down", esto se realizó con exito y se logro ejecutar el mixed_parser
 
 # Fecha 15 de Febrero del 2018
 
 ### Requerimientos:
  
 - Reunión con Paula estrella
  
 ### Informa de Trabajo 
 
 + Se llevó acábo una reunión por hangouts con Paula Estrella en dicha reunión se mencionó el avance actual.
    + Se mencionó que el proyecto ResearchAnalyzer cuenta con una clase llamada LogInfo y que es necesario revisar dicha clase ya que contiene información que podría ser util para la investigación.
    + Se necesita ejecutar main_example1.py y posteriormente ejecutar loginfo sobre los logs que genera windows.
 + Se ejecutó con exito main_example1.py
 + Se intentó ejecutar el script main_example1.py con los logs generados por windows, el resultado fueron diferentes errores que deben ser investigados.
 
 # Fecha 16 de Febrero del 2018
 
 ### Requerimientos:
  
 - Ejecutar loginfo.py con los script de prueba en windows
  
 ### Informa de Trabajo 
 
 - Se necesita averiguar por que el codigo al ejecutarse con los logs de windows falla durante la ejecución
 - A partir de varias pruebas que se ejecutaron con loginfo se concluye lo siguiente:
    - se necesita comprender de mejor manera la estructura de el ResearchAnalyzer, por lo que se realizó la lectura de la tesis de roxana reyes de la página 25 a la página 29
 - Se identifica que el script loginfo.py hace uso de otros scripts entre ellos click_parse.py el script que lanzaba el error, se concluye que la falta de x,y en los logs de detailed_log genera eel problema, se agrega -1 -1 como x,y en el log generado en windows esto para verificar si es posible que el codigo se ejecute.
 - Aun debe depurarse los logs ya que aún no se ejecuta el script.
 
 # Fecha 19 de Febrero del 2018
 
 ### Requerimientos:
  
 - Verificar nuevo error encontrado en click_parser.py
  
 ### Informa de Trabajo
 - Se creo el script windows_logs_test.py para pruebas de desarrollo:
    - Este script intenta inicializar una instancia de loginfo como en ejemplo de main_example1.py de ResearchAnalizer, aun genera un error.
    - En cuestiones de diseño es necesario que solo colocando las diferentes carpetas generadas por el research logger en un directorio se genere un informe por cada carpeta, por lo cual e creó la función load_loginfo, esta funcion realiza lo siguiente:
        - Revisa la carpeta logs_to_treat y con el scrpitchecker genera para cada registro de logs los nuevos archivos de logs para cada carpeta.
        - inicializa la instancia de loginfo para cada registro de log.
 - A partir de varias pruebas que se ejecutaron se concluye lo siguiente:
    - ResearchLogger genera los nombres de las imagenes a partir del nombre de la ventana activa, en windows los nombres que se les dan a las ventanas son la dirección del directorio en el cual se esta ejecutando el programa, dicha dirección puede contener espacios en el nombre como por ejemplo c:\ejemplo uno\programa.exe, esto hace que a la hora de llamarse haya proble con los separadores ya que uno de ellos en un espacio.
    - Se necesita revisar que los nombres de las imagenes en el log no contengan espacio por lo cual se optó por lo siguiente:
        - Contar los | que se encuentran en el log
        - Contar las , que se encuentren en el log
        - cuando se tenga 4 comas se verifica que el valor siguiente no contenga cespacios entre el identificador "," y .png
        - Se inició la implementaacíon de código en la funcióon arranger en scriptchecker.py aun es necesario depurar.
 - Se generó el pdf Validate_manual, el cual se lee envió a Mario, el cual contiene como corregir el problema de la falta de la biblioteca validate.py para ejecutar el ResearchLogger
 
 # Fecha 20 de Febrero del 2018
 
 ### Requerimientos:
  
 - Terminar función arranger para modificación de logs
 - Ejecutar el script windows_logs_test
  
 ### Informa de Trabajo
 
 - Actualmente se cuenta con el script windows_logs_test.py, este hace uso de los script scriptchecker.py y loginfo.py
 - Se generó un algoritmo en la funcion aranger con el cual se corrige el problema de los espacios encontrados en el nombre de las imagenes, esto en los logs de los clicks.
 - Se inicializó con exito la instancia de loginfo una vez que se corrigio el problema.
 - Se intentó obtener el tiempo total de la sesion, este hace uso de el script phaseinfo.py, se genero aun error ya que se descubrio que a logs les hace falta un identifacador "Abrir"
 - Teniendo ya el algoritmo de remplazo en la funcion arranger fue mas facil agregar el identificador "Abrir" a los logs, echo esto se descubrio que no se conoce cual es el archivo finale necesario para poder crear la instancia de phaseinfo.
 - Se forsó crear la instancia de phaseinfo pero se genero un error en la linea 53 del script phaseinfo.py aun se comprende dicho error.
 - Se terminó de simular con exito el main_example1.py con los logs de windows con excepción de los graficos la información si se puede obtener.
 - Se inicio con las pruebas en python para crear un archivo excell.