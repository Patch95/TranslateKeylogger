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
 + Se instaló git en windows para control de versiones.
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
 + Se instaló pywin32-219:
    - https://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download
 + se instaló configobj:
    - Navegar por la línea de comandos hasta el directorio de configobj.
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
 + se realizó la instalación con éxito.
 + Finalmente se comenzo generar un archivo .bat el cual realizará la instalación de manera más fácil para un usuario no experto.

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
 
 - Solucionar el problema de las variables de ambiente.
 
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
    1. ResearchLoggerInstaller: éste se encarga de llamar a los diferentes instaladores que son necesarios para que el researchlogger funcione correctamente.
    2. EnvironmentVariables: este se encarga de escribir las variables de entorno necesarias para que python sea accesible desde terminal y para que se pueda hacer uso del comando pip que se necesita para el último script.
    3. validate: Este script se encarga de instalar la biblioteca validate de python.
 + Se realizó el README de instalación, se especifica que script deben ser ejecutados y de que forma.
 + Se asignó la lectura ApuntesPaula para investigación, se comenzó a leer y a comprender durante el día.
 
 
 # Fecha 30 de enero del 2018
 
 ### Requerimientos:
  
 - Pruebas de instalador
 - Lectura de folleto ApuntesPaula
 - Lectura de Tesis de Keylogging para el estudio de los procesos cognitivos del traductor, Rozana Anabel Lafuente
 -
 
 ### Informa de Trabajo 
 
 + Se utilizaron dos sujetos de prueba para testear el script de instalación, Jose Roerto Argueddas y Randall Araya Campos.
    - El primer sujeto de prueba completo el tutorial de instalación con éxito, como retroalimentación sugirió realizar dos instaladores 1 con detalles técnicos (el que actualmente existe) y otro que tenga screenshots y más detalles de la instalación.
    - El segundo sujeto de prueba seleccionó la opción de reinicio por error, en caso de que esto suceda el script puede correrse nuevamente solo que la instalación de python debe cancelarse la segunda vez que se ejecuta ya que este ya estaría instalado.
 + Se leyó el folleto ApuntesPaula y se generaron dudas que deben ser consultadas con paula
 + Se leyó la Tesis de Keylogging para el estudio de los procesos cognitivos del traductor, Roxana Anabel Lafuente, se hizo apuntes de la lectura y también se generaron dudas.
 
# Fecha 31 de enero del 2018
 
 ### Requerimientos:
  
 - Reunión con usuario no experto para instalación de researchlogger
 
 ### Informa de Trabajo 
 
 + Se tuvo una reunión con una señorita que se encuentra en España, reunión virtual, en la cual se testeó el script de instalación para windows.
 + Durante la instalación hubo un error con las variables de entorno, que se solucionó por medio de teamviewer.
 + Finalmente se asignó la revisión del folleto ApuntesPaula contra la estructura de los logs.
 
 # Fecha 01 de enero del 2018
 
 ### Requerimientos:
  
 - No aplica
 
 ### Informa de Trabajo 
 
 + No se trabajó por motivos de enfermedad.
 
 # Fecha 02 de enero del 2018
 
 ### Requerimientos:
  
 - Reunión en FaMAF
 
 ### Informa de Trabajo 
 
 + Se llevó a cabo la primera reunión en conjunto con Paula Estrella, Aurelio Sanabria y María Estrada.
 
 # Fecha 05 de enero del 2018
 
 ### Requerimientos:
  
 - Realizar documento de factibilidad de transformación de los logs de ResearchLogger
 
 ### Informa de Trabajo 
 
 + Se realizó el documento
 + Se acordó generar consultas para ricardo
 + Se asignó la tarea de comenzar a generar una pequeña visualización del log de clicks y de teclas mezclados.
 
 # Fecha 06 de enero del 2018
 
 ### Requerimientos:
  
 - Realizar consultas para Ricardo
 - Realizar pruebas de script de Jose Roberto Arguedas en windows
 - Realizar Chequeo de anteproyecto
 
 ### Informa de Trabajo 
 
 + En conjunto con Jose Roberto Arguedas se testeo el script de manejo de clicks y de toma de imágenes.
    + Se realizó una máquina virtual de windows 10
    + Se instaló el research logger con la ayuda del KitResearchLogger anteriormente creado
    + Se instalaron las bibliotecas necesarias
    + Se cedió el uso de mi computadora a Jose Roberto Arguedas para que este pudiera realizar los test necesarios.
 + Para que haya un entendimiento más adecuado para Ricardo se instaló microsoft office 2013 para generar las consultas de mejor manera.
 + Se revisaron los documento de anteproyecto necesarios para el Tecnológico de Costa Rica.
 
 # Fecha 07 de enero del 2018
 
 ### Requerimientos:
  
 - Realizar consultas para Ricardo
 - Clonar repositorio de Roxana Lafuente ResearchAnalyser
 - Probar mixed_parse.py de ResearchAnalyser
 
 ### Informa de Trabajo 
 
 + Se realizaron las consultas en el documento de ricardo a manera de comentarios en word.
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
    + Se concluye que, en el log, la falta de X,Y del mouse cuando se presiona una tecla es la causa del fallo, ya que los separadores para comprender la información generar mal los datos si estos datos no están.
    + Se compararon los log de windows y de ubuntu:
        + Los logs de ubuntu no generan el nombre de las pestañas de los navegadores.
    + Se descargo e instaló windows 7 en una máquina virtual esto para realizar pruebas con el researchlogger y ver si NO genera X,Y como en windows 10
        + Se concluye que en windows 10 y 7 no se generan los x,y
        
 # Fecha 09 de enero del 2018
 
 ### Requerimientos:
  
 - Reunión semanal con Aurelio Sanabria y María Estrada
 
 ### Informa de Trabajo 
 
 + La reunión con Aurelio y Maria Estrada no se llevó a cabo, por lo cual solo se tuvo una reunión con Paula Estrella
 + En la reunión se acordó lo siguiente:
    + Los logs serán visualizados en un dashboard, se necesita definir qué datos pueden generarse y como se puede mostrar la información
    + Se necesita corregir el mixed_parser ya que es necesario trabajar con logs de windows, se sugiere que no se pidan las variables x,y una vez que se carguen los logs.
 + Se intentó NO solicitar las variables x,y pero el script aún falla, realizando más investigación, se concluyó que los logs en windows se generan también con el siguiente error:
    + "key_down" y "key_up" no tiene la raya baja "_" por lo cual aparecen de la siguiente forma "key down" "key up"
 + Debido a todos estos problemas se optará por realizar un script en python que revise la estructura de los logs generados y que haga correcciones si es necesario.
 
 # Fecha 12 de Febrero del 2018
 
 ### Requerimientos:
  
 - No aplica
 
 ### Informa de Trabajo 
 
 + No se trabajó por día Feriado.
 
 # Fecha 13 de Febrero del 2018
 
 ### Requerimientos:
  
 - No aplica
 
 ### Informa de Trabajo 
 
 + No se trabajó por día Feriado.
 
 # Fecha 14 de Febrero del 2018
 
 ### Requerimientos:
  
 - Reunión con supervisor de práctica profesional
 
 ### Informa de Trabajo 
 
 + Se realizó una reunión con Aurelio sanabria en la cual se expusieron dudas con respecto al proyecto de investigación.
 + Revisión de los logs, se propondrá la idea de realizar un Chequeador de scripts el cual verifique si cada uno de los espacios correspondientes al detailedlog son correctos.

 # Fecha 15 de Febrero del 2018
 
 ### Requerimientos:
  
 - Reunión con Paula estrella
 - Consulta de Proyecto de investigación
  
 ### Informa de Trabajo 
 
 + En FAMAF se llevó a cabo una reunión en la cual se consultó la viabilidad actual del proyecto de investigación y dudas con respecto a desarrollo:
    + Se acordó continuar con el rumbo actual del proyecto, ya que no afecta al cronograma ni a la extensión del mismo
    + Con respecto al desarrollo se simplificó la realización del scriptchecker, se acordó solo modificar los datos que estuvieran erróneos
    + Se necesita chequear si es posible mostrar:
        + Tiempo total de sesión
        + Tiempo por herramienta
        + Tiempo por recurso
        + Combinaciones de teclas
 + Se generó el script adminfile.py para manejo de archivos
 + Se creó la función arranger la cual cambia en el detailedlog "key down" y "keyup" por "key_down" y "key_up" y genera un nuevo archivo con el identificador _new
 + Una vez que se ejecutó el mixed_parser con el log modificado se descubrió que el archivo clickimagelogfile también posee un error similar en windows el cual es que "mouse left up" y "left_up" deben ser cambiados por "mouse left down" y "left_down", esto se realizó con éxito y se logro ejecutar el mixed_parser
 
 # Fecha 16 de Febrero del 2018
 
 ### Requerimientos:
  
 - Reunión con Paula estrella
  
 ### Informa de Trabajo 
 
 + Se llevó a cabo una reunión por hangouts con Paula Estrella en dicha reunión se mencionó el avance actual.
    + Se mencionó que el proyecto ResearchAnalyzer cuenta con una clase llamada LogInfo y que es necesario revisar dicha clase ya que contiene información que podría ser útil para la investigación.
    + Se necesita ejecutar main_example1.py y posteriormente ejecutar loginfo sobre los logs que genera windows.
 + Se ejecutó con exito main_example1.py
 + Se intentó ejecutar el script main_example1.py con los logs generados por windows, el resultado fueron diferentes errores que deben ser investigados.
  
 # Fecha 19 de Febrero del 2018
 
 ### Requerimientos:
 - Ejecutar loginfo.py con los script de prueba en windows
 - Verificar nuevo error encontrado en click_parser.py
  
 ### Informa de Trabajo
 - Se necesita averiguar por que el código al ejecutarse con los logs de windows falla durante la ejecución
 - A partir de varias pruebas que se ejecutaron con loginfo se concluye lo siguiente:
    - se necesita comprender de mejor manera la estructura de el ResearchAnalyzer, por lo que se realizó la lectura de la tesis de roxana reyes de la página 25 a la página 29
 - Se identifica que el script loginfo.py hace uso de otros scripts entre ellos click_parse.py el script que lanzaba el error, se concluye que la falta de x,y en los logs de detailed_log genera el problema, se agrega -1 -1 como x,y en el log generado en windows esto para verificar si es posible que el código se ejecute.
 - Aún debe depurarse los logs ya que aún no se ejecuta el script.
 - Se creo el script windows_logs_test.py para pruebas de desarrollo:
    - Este script intenta inicializar una instancia de loginfo como en ejemplo de main_example1.py de ResearchAnalizer, aun genera un error.
    - En cuestiones de diseño es necesario que solo colocando las diferentes carpetas generadas por el research logger en un directorio se genere un informe por cada carpeta, por lo cual se creó la función load_loginfo, esta funcion realiza lo siguiente:
        - Revisa la carpeta logs_to_treat y con el scrpitchecker genera para cada registro de logs los nuevos archivos de logs para cada carpeta.
        - inicializa la instancia de loginfo para cada registro de log.
 - A partir de varias pruebas que se ejecutaron se concluye lo siguiente:
    - ResearchLogger genera los nombres de las imagenes a partir del nombre de la ventana activa, en windows los nombres que se les dan a las ventanas son la dirección del directorio en el cual se esta ejecutando el programa, dicha dirección puede contener espacios en el nombre como por ejemplo c:\ejemplo uno\programa.exe, esto hace que a la hora de llamarse haya problemas con los separadores ya que uno de ellos en un espacio.
    - Se necesita revisar que los nombres de las imágenes en el log no contengan espacio por lo cual se optó por lo siguiente:
        - Contar los | que se encuentran en el log
        - Contar las , que se encuentren en el log
        - cuando se tenga 4 comas se verifica que el valor siguiente no contenga espacios entre el identificador "," y .png
        - Se inició la implementacíon de código en la funcióon arranger en scriptchecker.py aun es necesario depurar.
 - Se generó el pdf Validate_manual, el cual se lee envió a Mario, el cual contiene como corregir el problema de la falta de la biblioteca validate.py para ejecutar el ResearchLogger
 
 # Fecha 20 de Febrero del 2018
 
 ### Requerimientos:
  
 - Terminar función arranger para modificación de logs
 - Ejecutar el script windows_logs_test
  
 ### Informa de Trabajo
 
 - Actualmente se cuenta con el script windows_logs_test.py, este hace uso de los script scriptchecker.py y loginfo.py
 - Se generó un algoritmo en la función aranger con el cual se corrige el problema de los espacios encontrados en el nombre de las imágenes, esto en los logs de los clicks.
 - Se inicializó con éxito la instancia de loginfo una vez que se corrigió el problema.
 - Se intentó obtener el tiempo total de la sesión, éste hace uso del script phaseinfo.py, se genero aún error ya que se descubrió que a logs les hace falta un identificador "Abrir"
 - Teniendo ya el algoritmo de remplazo en la función arranger fue mas facil agregar el identificador "Abrir" a los logs, echo esto se descubrió que no se conoce cual es el archivo finale necesario para poder crear la instancia de phaseinfo.
 - Se forzó crear la instancia de phaseinfo pero se genero un error en la linea 53 del script phaseinfo.py aun se comprende dicho error.
 - Se terminó de simular con exito el main_example1.py con los logs de windows con excepción de los gráficos la información si se puede obtener.
 - Se inició con las pruebas en python para crear un archivo excell.
 
 
 # Fecha 21 de Febrero del 2018
 
 ### Requerimientos:
  
 - Reunión con el coordinador
 - Reunión con Paula
  
 ### Informa de Trabajo
 
 - Reunión semanal con el coordinador de práctica profesional,Aurelio Sanabria.
 - Se llevo acabo una reunión con Paula Estrella, en dicha reunión se trataron temas como:
    - Posibles ideas para paper
    - Estado actual de avance
 - Se acuerda realizar las siguientes tareas:
    - Lectura de paper Psycholinguistic Foundations of the Writing Process
    - Depurar código para obtener aún más información necesaria a partir de los logs
    - Investigar cómo realizar un piloto en procesos de programación
    - Introducción con evidencia de autores
    - Investigar que son los procesos de escritura
    - Investigar términos técnicos de lo que se tiene como ideas
  
 # Fecha 22 de Febrero del 2018
 
 ### Requerimientos:
  
 - Video llamada con Mariona
 - Verificación de Tags

  
 ### Informa de Trabajo
 
 - Se realizó una video llamada con Mariona Sabate y  con el técnico en computación, en dicha reunión se solucionaron los problemas de instalación que se tenía con el ResearchLogger.
    - El primer problema se debía a que la biblioteca validate no se instalo correctamente, ya que las computadoras cuentan con dos usuarios, uno administrador, por lo que el script que genera las variables de ambiente en el momento de la solicitud de permisos de superusuario no funcionó correctamente.
    - El segundo problema que se encontró fue que en el momento de mover la carpeta ResearchLogger a la dirección C:\ResearchLogger se solicitan permisos de superusuario y la carpeta se mueve con estos permisos por lo cual la carpeta no era visible para todos los usuarios solo para el usuario administrador, se resolvió volver a descomprimir el kitResearchLogger y mover la carpeta manualmente.
 - Con ayuda de Jose Roberto Arguedas, se verificó el nombre de la ciertas teclas especiales como enter o delete, cual es el nombre que se genera para ellas en ubuntu y cual en windows, se agregaron a la función arranger de scriptchecker.py
 
 
 # Fecha 23 de Febrero del 2018
 
 ### Requerimientos:
  
 - Lectura paper Psycholinguistic Foundations of the Writing Process
  
 ### Informa de Trabajo
 
 - Se inició con la lectura del paper se tomaron apuntes escritos y apuntes en documento de texto, la lectura posee muchos términos técnicos y se encuentra escrita en inglés, también contiene explicaciones de estructuras gramaticales en inglés por lo que requiere de más tiempo de comprensión e investigación.
 - También se realizó la lectura del la tesis de Roxana La Fuente no enfocado en código y diseño de código
 - Se obtuvo el tiempo total de la sesión mediante la resta del último tiempo obtenido, ya sea de click o de tecla presionada, menos el primer tiempo obtenido.
 
 # Fecha 26 de Febrero del 2018
 
 ### Requerimientos:
  
 - Lectura paper Psycholinguistic Foundations of the Writing Process
 - Generar boceto de Excel
  
 ### Informa de Trabajo
 
 - Se terminó con la lectura del paper.
 - Se realizó una comparación entre el tiempo total obtenido mediante la resta y el tiempo total que se genera a partir del uso de la función get_time_by_active_window().
    - Los tiempos no coinciden, se decidió trabajar con el tiempo total que se genera mediante la función.
 - Se inició con la generación del archivo excel a partir de la información previamente obtenida con el research logger.
    - Se utilizó la biblioteca xlxswrite:
        - https://pypi.python.org/pypi/XlsxWriter/
    - Se creó la función generate data
    - Para cada carpeta se generó un archivo de excel:
        - El nombre de este archivo tiene el siguiente formato Analysis_Usuario_id.xlsx
        - Cada archivo cuenta con 1 worksheet (hoja de trabajo) GeneralInfo

 
 
 # Fecha 27 de Febrero del 2018
 
 ### Requerimientos:
  
 - Generar boceto de Excel
 - Realizar manual de uso de ResearchLogger
  
 ### Informa de Trabajo
 
 - Se continuó con la generación del excel, se agregaron 2 worsheets (hojas de trabajo) al archivo excel, ClicksInfo, KeysInfo
 - Durante el día se recibieron varios correos de Mariona sabate los cuales se adjunta a continuación:
```
Hola Walter,

El lunes de la semana que viene vamos a hacer la primera actividad con los
alumnos con el keylogger. Para ello, me gustaría hacer un par de pruebas,
una en mi ordenador (donde ya está instalado el keylogger) y una desde un
ordenador de la sala 3.48 (donde ya está instalado en todos los
ordenadores el keylogger).

¿Puedes darme instrucciones de cómo activar el keylogger? Una vez haya
hecho la prueba en mi ordenador, podemos hacer un teamviewer y puedes
comprobar dónde están los documentos generados por la traducción.

Después, podemos hacer una prueba desde la 3.48 utilizando también
teamviewer.

Por favor, indícame tu disponibilidad de días y horas, para calcular la
hora española teniendo en cuenta la diferencia horaria de 4 horas.

Gracias por todo,
ona
```
```
 Hola Walter,

Te envio el documento con las instrucciones (instrucciones.doc) que pasaré
a los alumnos para la sesión de la semana que viene.

¿Podrías aclararme los fragmentos que he resaltado en color rojo? Gracias
ona
```
```
Hola Walter,

Otra vez yo. He hablado con los informáticos (Roger y Pascal) y me han
dicho que podríamos tener la sesión mañana miércoles a las 13:30 en España
(9:30 en Argentina). Qué tal?
ona
```
- Dados los anteriores correos se le contestó a Mariona Sabata:
    - Se accede a tener la reunión el día y la hora indicadas por ella.
    - Se realizó un manual el cual indica como activar el ResearchLogger y como verificar que este funciona correctamente.
    
 # Fecha 28 de Febrero del 2018
 
 ### Requerimientos:
 
 - Reunión con Mariona Sabate
 - Reunión con el coordinador de practica profesional Costa Rica
  
  
 ### Informa de Trabajo
 
 - Se llevó acabo la reunión con Mariona Sabate:
    - Se le explicó como ejecutar paso a paso el researchlogger, con o sin interfaz.
    - Se explicó como verificar si el researchlogger funciona correctamen.
    - Se hizo uso de skype para llevar a cabo la reunión y de teamviwer para mejor comprensión de los pasos a seguir
 - Se llevó a cabo la reunión semanal con Aurelio Sanabria, se trataron temas como:
    - Estado actual de la investigación
    - Situación actual en Argentina
    - Se me solicitó comenzar a redactar documentos formales que requiere el Tecnológico de Costa Rica durante la práctica profesional:
        - Informes semanales de trabajo con un formato particular.
        - Primer Informe general con un formato particular.
 - Se continuó pensando en como generar un boceto de información en excell. 
 
 # Fecha 01 de Marzo del 2018
 
 ### Requerimientos:
  
 - Generación de archivo excell
 - Lectura de "An Online System for Monitoring and Assessing the Programming Process"
 
  
 ### Informa de Trabajo
 
 - Actualmente el script windows_logs_test.py cuentaa con las siguiente funciones:
    - load_loginfo(): Función que revisa la carpeta logs_to_treat y con el scrpitchecker genera para cada registro de logs los nuevos archivos de logs para cada carpeta, también inicializa la instancia de loginfo para cada registro de log.
    - total_session_time(): Función que obtiene el tiempo total de la sesión mediante la resta del ultimo tiempo registrado menos el primer tiempo registrado, actualmente no se hace uso de esta función.
    - generate_click_info(li, workbook, addname): Función que imprime información extraida con loginfo con respectto a los clicks, se filtraron por evento down.
    - generate_key_info(li, workbook, addname): Función que imprime información extraida con loginfo con respectto a los eventos de teclado, se filtraron por evento down.
    - generate_separate_data(): Función que se encarga de generar un archivo excel por cada carpeta en logs_to_treat
 - Actualmente se genera un archivo excel por cada carpeta,
    - Se modificaron las fuciones print_click_summary() y print_key_summary() para que no solo imprimieran los datos sino que los retornaran, esto para trabajar con los datos y no realizar modificaciones mayores en loginfo.py
    - El nombre del archivo se construye de la siguiente forma, Analysis_Usuario_ID.xlsx, ejemplo:
        - Analysis_walter_1518136283.xlsx
    - Cada archivo tiene una hoja con información y datos generales
    - Una hoja con la información de los click obtenida a partir de loginfo.py
    - Una hoja con la información de las  teclas obtenida a partir de loginfo.py
    - Se procederá a generar un archivo excel, "United_Analysis.xlsx", que contenga los datos generales de cada carpeta en una solo hoja para asi realizar graficos basados en el excel "Análisis Traducción Técnica"
    - Se realizó la lectura del paper "An Online System for Monitoring and Assessing the Programming Process"
 
 # Fecha 02 de Marzo del 2018
 
 ### Requerimientos:
  
 - Generar archivo United_Analysis.xlsx
 - Investigación procesos de escritura
 - Investigación procesos de programación
 
 ### Informa de Trabajo
 
 -  United_Analysis.xlsx, se agregó al script windows_logs_test.py las funciones:
    - generate_full_data(): Función que se encarga de crear el archivo excel, escribe la información general de cada carpeta en una sola hoja
    - generate_total_plot(workbook, worksheet, usersamount): Genera un gráfico que compara los usuarios por tiempo total de sesión.
 - Procesos de escritura se investigó hasta encontrar el siguiente link:
    - https://cmsw.mit.edu/writing-and-communication-center/resources/writers/writing-process/
 - Procesos de programación se investigó y por recomendación de Msc.Kevin Moraga se sugiere leer.
    - La catedral y el bazar
    
# Fecha 05 de Marzo del 2018
 
 ### Requerimientos:
  
 - No aplica
 
 ### Informa de Trabajo
 
 - No se trabajó por problemas con la conexión a internet y problemas con la electricidad.
 
 # Fecha 06 de Marzo del 2018
 
 ### Requerimientos:
  
 - Lectura del documento la catedral y el bazar
 - Añadir funcionalidades al archivo United_Analysis.xlsx
 
 ### Informa de Trabajo
 - Se comenzó con la lectura la catedral y el bazar, actualmente falta leer la mitad del document
 - United_Analysis.xlsx, se agregó al script windows_logs_test.py las funciones:
    - generate_resources_plot(workbook, worksheet, users, resourcesamount): Genera un gráfico que compara los usuarios por tiempo en recurso.
    - Se agregaron modificaciones a la función generate_full_data(), esto para lograr acomodar los datos que utilizará la función generate_resources_plot.
    - Actualmente se generan errores de impresion de datos.
  
 
 # Fecha 07 de Marzo del 2018
 
 ### Requerimientos:
  
 - Terminar lectura la catedral y el bazar
 - Lectura An Online System for Monitoring and Assessing the Programming Process
 - Analisis y depuración de codigo actual
 - Realizar los Informes Semalanes
 
 ### Informa de Trabajo
 
 - Se terminó con la lectura la catedral y el bazar, se concluye que tiene un minimo de relevancia para el proyecto.
 - Se realizó la lectura An Online System for Monitoring and Assessing the Programming Process, se concluye que es de gran relevancia para el proyecto
 - Se corrigieron los errores de impresión se primera etapa de representación de información generada por ResearchLogger.
 - Se hizo de mi conocimiento que se necesita entregar informes de avances semanales, por lo que se debe realizar los primeros 6 informes de las semanas anteriores, actualmentes se han realizado estos informes y se encuentran en un documento compartido.
 
 # Fecha 08 de Marzo del 2018
 
 ### Requerimientos:
 
 - Reunión con Mariona Sabaté
 - Reunión con tutora de proyecto Argentina
 - Continuar el borrador del Primer Informe
 
 ### Informa de Trabajo
 
 - Mariona Sabaté solicitó una reunión por video llamada para verificar que la prueba que ella realizó con sus alumnos fue exitosa, ella no ejecuto el script researchlogger.py por lo cual la sesión de traducción no se grabo, solo obtuvo un volcado del archivo generado por los traductores.
 - Se llevó a cabo una reunión en FAMAF con Paula estrella:
    - Se habló del estado actual de los script, se necesita agregar una reconstruccion de palabras por herramienta al archivo excel.
    - Se hablo de las bibliografias encontradas y leidas, se acordó se buscarian mas bibliografias con relación a visualización de la información.
    - Se aclaró que realizar un piloto es testear el software ResearchLogger con estudiantes de ingeniería en computación y posteriormente analizar los datos con el script windows_logs_test.py.
    - Se necesita cambiar el nombre del script windows_logs_test.py.
 - Se hizo de mi conocimiento que se necesita entregar un informe general que describa aspectos de la practica profesional, actualmentes se ha realizado este informe y se encuentra en un documento compartido.
 
 # Fecha 09 de Marzo del 2018
 
 ### Requerimientos:
  
 - Reunión con el coordinador de proyecto
 
 ### Informa de Trabajo
 
 - Se llevó a cabbo una reunión con Aurelio Sanabria:
    - Se consulto acerca del "norte" del proyecto, se corrigió y se analizó el mismo.
    - Se revisó el primer informe el cual se acuerda realizar correcciones.
    - Se solicitó entregar los informes semanales por separado en formato pdf.
    - Se solicitó redactar minuta de la reunión de la semana pasada y de esta reunión, tambien se acordó realizar minutas de las reuniones con Aurelio Sannabria apartir de la presente fecha.
    
  # Fecha 12 de Marzo del 2018
 
 ### Requerimientos:
  
 - Redactar minuta de la reunión de las semanas 6 y 7.
 - Realizar Correcciones al Primer Informe para el Tecnológico de Costa Rica.

 
 ### Informa de Trabajo
 
 - Se realizaron las correcciones al Primer informe:
    - Se agregó un índice
    - Se agregó todo lo relacionado con el "norte" de la investigación
    - Se le agrregó al contexto del proyectto una sección acerca del convenio TEC - (FAMaF- UNC)
    - Se agrego la metodología y los modelos conceptuales
 - Se realizarón la minutas de las semanas 6 y 7, se espera aprovación de las mismas.
    
 
 # Fecha 13 de Marzo del 2018
 
 ### Requerimientos:
  
 - Agregar una reconstrucción de palabras por herramienta al archivo excel.
 
 ### Informa de Trabajo
 
 - Se agrego un worksheet al excel:
    - Nombre se asigna de la siguiente forma Textinfo_{USER}_{id}
    - Por cada recurso que exista, no importa si es de la misma ventana, se imprimira en un cuadro los keys sin filtrar de algún modo.
    - Posteriormente en un cuadro diferente se mostrara una reconstruccion parcial de texto.
 - Se creó el archivo constants_analysis_value.py en el se ecuentra un hash el cual se utilizara para la reconstrucción parcial, cambia las teclas speciles por su equivalente.
    - return se cambia por \\n
 - Se creó la función generate_words_reconstruction:
    - Se encarga de imprimir generar y imprimir en el excel los keys iniciales y el texto reconxtruido.
    - Se realizó la impresión del los keys sin modificar.
     
   
 
 
 # Fecha 14 de Marzo del 2018
 
 ### Requerimientos:
  
 - Continuar la reconstrucción de palabras por herramienta al archivo excel.
 
 ### Informa de Trabajo
- Se resuelve que filtrar por down en la funcion generate_key_info no es viable, ya que se necesita tener key_up para realizar las combinaciones de las teclas
- Se modificó la función generate_key_info para que ya no filtre los keys
- Se creó la funcion get_combos:
    - Se encarga de encontrar todas las combinaciones de teclas que haya en el log
    - Algortimo:
        - Se inicialmete toma cada key excepto letras
        - Se coleccionan todos los key a continuación encontrados hasta que se encuentre el up del key inicial
        - De los keys coleccionados se ignora el up ya que no hace falta tomarlo en cuenta, esto asegura que se guarden todas las combinaciones especiales de dos o más teclas.
 - Se imprime con exito la reconstrucción parcial de texto.
 
 # Fecha 15 de Marzo del 2018
 
 ### Requerimientos:
  
 - Relizar simulacro de piloto de software
 
 ### Informa de Trabajo
 
 - Se creó una maquina virtual de windows 7.
 - Se instaló todo lo necesario para realizar el piloto de software.
 - Se quiere realizar el siguiente piloto:
    - Generar un lista de 10 elementos que contenga numeros generados aleatoriamente.
 - Supuestos del piloto:
    - En caso de querer realizar una consulta en web SE PUEDE UTILIZAR SOLO google chrome.
    - Se tiene que utilizar el idle de python.
    - Antes de inicializar el researchlogger se debe haber guardado el archivo con el nombre del estudiante walter.py en este caso.
 - Se realizó el piloto con exito
 - Se tomó la carpeta generada y se intento realizar el excel con dicha información
 - Se generó el siguiente erro
    ```
    Ha ocurrido un error fatal. El log no tiene el formato deseado.
    ```
    - Error generado por la clase loginfo.py
 
 # Fecha 16 de Marzo del 2018
 
 ### Requerimientos:
  
- Reunión con tutora de proyecto Argentina
 
 ### Informa de Trabajo
 
 - Se mostró la reconstrucción parcial del texto, que está separado por recurso utilizado.
 - Se expuso el error encontrado con la realización del log, el cual debe ser visto en una reunión presencial.
 - También se concluye realizar el mismo piloto en un live cd de ubuntu y en una maquina que tenga como sistema operativo windows 7.

    