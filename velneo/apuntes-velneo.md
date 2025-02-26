# OBJETOS
Un objeto es un elemento definible dentro de un proyecto que realiza las tareas de un programa. Estos objetos son creados de forma visual y únicamente tendremos que definir sus propiedades.
Una característica de estos objetos es la **refactorización automática** que se encarga de refrescar el cambio de identificador de cualquier objeto allí donde se use.

## Tabla
Sirve para almacenar la información de manera organizada.
Una tabla organiza la información en fichas o registros que contienen los mismos campos o datos individuales.

## Actualización
Una actualización es un subobjeto de tabla que permite actualizar el valor de los campos de un registro de una tabla a la que apunta cada vez que se produce un alta, una modificación o una baja

## Campo
Un campo es un subobjeto de una tabla que define la mínima unidad de información dentro de un registro a la que podemos acceder.

## Enlace
Nos permite establecer una relación entre dos registros de distintas tablas por medio de un campo y un índice de clave única de la tabla enlazada.

## Índice
Se trata de una estructura de datos que mejora la velocidad de las operaciones, permitiendo un rápido acceso a los registros de una tabla.

## Plural
Un enlace plural relaciona los registros de la tabla maestra con sus registros en la tabla plural.
Los enlaces plurales se crean de forma automática y no es posible crearlos, modificarlos o borrarlos de forma manual.

## Trigger
Un trigger es un proceso definido por el programador que es ejecutado automáticamente al producirse el evento al que hace referencia.

## Acción
Una acción es el objeto de proyecto de aplicación que permite disparar un comando.
La acción puede ser usada en opciones de menú, toolbars, botones en formularios, etc. 

## Alternador de lista
Se trata de un objeto al que se le pueden declarar múltiples objeto de salida (rejilla, informe, casillero, etc.) entre los que el usuario final podrá alternar en tiempo de ejecución. 

## Búsqueda
Es el objeto que sirve para realizar consultas en las tablas de datos.

## Dibujo
Se trata de un objeto que contendrá un dibujo estático (puede ser una foto).

## Esquema de tablas
Este objeto permite tanto crear como mostrar de forma gráfica la estructura de tablas de nuestros proyectos, así como crear enlaces entre las mismas.
Dentro de un mismo proyecto podremos crear tantos esquemas como consideremos necesario

## Formulario
Un formulario es el objeto de proyecto de aplicación que permite introducir, modificar y ver los distintos campos de una ficha o registro de una tabla por medio de controles. Para ello debe tener una tabla asociada de la que podrá presentar los registros.
Como entrada y salida el formulario tiene Ficha de la tabla asociada.

## Función
La función es un objeto contenedor de instrucciones definible por el programador. Las instrucciones se ejecutarán de forma secuencial y harán uso de comandos de instrucción de proceso que pueden acceder a otros objetos de los proyectos incluyendo otros procesos.

## Informe
Los informes se utilizan habitualmente para enviar información de tablas de datos a una impresora o a un documento de disco.

## Localizador
Un localizador es el objeto de proyecto de aplicación que permite localizar registros haciendo uso de los índices existentes en la tabla

## Marco
Nos permite definir cómo será la interfaz del usuario cuando ejecuta el proyecto de aplicación. 
En un proyecto de aplicación podemos definir más de un marco y es obligatorio que al menos haya uno llamado autoexec

## Menú
Un menú es el objeto de proyecto de aplicación que permite agrupar acciones y otros menús y presentarlos como un menú desplegable. El menú puede ser usado en el marco de la aplicación, en otros menús, como menú de contexto de objetos o en botones de formulario.

## Rejilla
La rejilla es un objeto que sirve para presentar listas de registros de las tablas.
La rejilla siempre va asociada a una tabla. El flujo es Lista de la tabla asociada tanto para la entrada como para la salida.
La rejilla está compuesta por una serie de celdas distribuidas en forma de filas y columnas. Una fila se corresponde con un registro de una tabla y una columna con un campo de la tabla.

## Toolbar
Una toolbar o barra de herramientas es un objeto de interfaz gráfica que contiene botones que al ser presionados activan ciertas funciones de una aplicación.
Cada botón de la toolbar disparará un objeto (acción o menú) declarado en el proyecto en curso o en los proyectos heredados o un menú en stock.
