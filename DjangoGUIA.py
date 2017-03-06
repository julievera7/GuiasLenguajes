# Guía Django by dM

**********TEORIA**********

#-Framework de desarrollo web de codigo abierto escrito en Python
#(todo lo que se haga dentro de Django sera en Python)

#-Permite construir aplicaciones web mas rapido y con menos codigo.

#-El un proyecto en Django se divide en varias partes llamadas aplicaciones, el conjunto
#esas aplicaciones genera un proyecto general en Django.

#-Django se basa en la reutilizacion de el codigo que ya hemos hecho,
#en tratar de no repetir y volver a escribir ese codigo. No duplcaremos
#el codigo.

#-Cuenta con su propia ORM (Object relational maping)  
#Quiere decir que nuestra base de datos relacional que ya conocemos
#la va a transformar a una base de datos orientada a objetos
#Las tablas que soliamos tener vamos a verlas en formas de clases
#y las consultas en SQL seran a nivel de Python.

#-Django trae su propio administrador por defecto:
#Podemos gestionar todos los datos de nuestro proyecto
#con el administrador.

**********PATRON DE DESARROLLO MVT**********

#***Modelo-vista-controlador:
#-Modelo: Se encarga de manipular toda la informacion
#de nuestro proyecto que este en nuestras bases de datos.
#Vista: Es la que decide como es que vamos a mostrar toda
#esta informacion almacenada.
#-Controlador: Es el que se encarga de hacer
#la comunicacion entre el modelo y las vista

#***Modelo-vista-template:
#(Ahora Django hara el papel de el controlador, que se encargaba
#de la comunicacion de los modelos y las vistas)
#-Modelo: Se encarga de manipular toda la informacion
#de nuestro proyecto que este en nuestras bases de datos.
#-Vista: Es la que se encarga de decir que informacion vamos
#a mostrar y en que template.
#-Template: Es el que se encarga de coger toda la informacion, organizarla
#y ver como se va a mostrar.

**********Instalar Django*********

#-Django está escrito completamente en Python
#por lo que el primer paso en la instalación de Django 
#es el asegurarse de que Python esta instalado.

#-Bajar Django de: http://www.python.org/download/
#Ejemplo: Django-1.5.12.tar.gz

#-Descomprimir el archivo: Nos dejara una carpeta
#Ejemplo: Django-1.5.12

#-Dentro de (Django-1.5.12) esta el archivo setup.py

#-Ejecutar: sudo python setup.py install #Estando en el directorio del archivo

#Tambien podemos realizar la instalación desde PIP que es un repositorio
#de paquetes python facil de manejar

########################
##### Paquetes PIP #####
########################

Para desarrollar software con rapidez y calidad, es imprescindible utilizar paquetes externos que ayuden
con parte de la funcionalidad que se desea implementar. En el ambiente Python esto no es la excepción.

// Para solventar ésta necesidad, la comunidad Python ha puesto convenientemente a disposición de los desarrolladores
un repositorio de paquetes de fácil acceso llamado PyPi. Solo es necesario ejecutar un comando en la terminal
para poder instalar el paquete Python que necesitemos. Incluso es posible instalar paquetes que no se encuentren
en el mencionado repositorio.

// Para descargar paquetes del repositorio PyPi se pueden utilizar varias herramientas, pero en este caso se
va a usar pip. Es necesario instalar esta herramienta en el sistema en caso de no estar disponible, antes
de poder instalar un paquete Python.

// El comando pip equivale al apt-get de Debian pero para paquetes Python.

$ aptitude install python−pip python−dev python-setuptools // Instalamos PIP y otros necesarios

// Una vez instalado ya podremos instalar paquetes de Python a traves de pip ejemplo:

$ pip install django // Nos instalara la ultima version de Django disponible en los paquetes pi

// Tambien es posible crear ficheros que contengan rutinas para automatizar la instalacion
de varios paquetes ejemplo:

Creamos un requirements.txt y dentro escribimos como ejemplo:
django==1.5.12
pillow==2.4.0
Geraldo==0.4.17

// Luego podemos ejecutar un pip install sobre el fichero e instalará lo que contenga:

pip install −r requirements.txt

// Dentro de los .virtualenvs, dentro de nuestro entorno virtual en
lib/python2.7/site-packages podemos ver que se instalaron los paquetes de requirements.txt
de no ser así hay que revisar el fichero o el nombre de los paquetes a instalar, etc.

$ pip search nombre_paquete // Buscar un paquete.

**********VERIFICACION DE INSTALACION**********

-Dentro de Python ejecutamos:
>>> import django
>>> django.VERSION #Nos mostrara la version de Django instalada
(1, 5, 12, 'final', 0)

-Otra forma:
>>> import django #Si el Comando se ejecuta sin errores es que Django esta instalado
>>> print(django.get_version()) #Nos mostrar la version de Django Instalada
1.5.12

**********Compatibilidad / Base de Datos**********

Django es compatible con cuatro motores de base de datos:

-PostgreSQL (http://www.postgresql.org/)
-SQLite 3 (http://www.sqlite.org/)
-MySQL (http://www.mysql.com/) #Django requiere MySQL 4.0 o superior
-Oracle (http://www.oracle.com/)

**********CREANDO UN PROYECTO**********

-Un proyecto es una colección de ajustes de una instancia de Django
incluyendo la configuración de la base de datos, las opciones
específicas de Django, y la configuración de la aplicación.

-Para crear un proyecto hay que abrir unaconsola
situarse donde se quiere crear el proyecto y Ejecutar:

$ django-admin.py startproject NombreDelProyecto #Se creará un directorio NombreDelProyecto 

-El comando startproject crea un directorio (NombreDelProyecto)
que contiene cuatro archivos:

1) __init__.py
-Es un fichero vacío, y normalmente no se le añade nada
-Le dice a Python que este directorio debería ser considerado
un paquete Python (un grupo de módulos)

2) manage.py
-Permite interactuar con el proyecto Django, administrar el proyecto.

3) settings.py
-Opciones/configuraciones para este proyecto de Django
-Muestra las características de configuración
de este proyecto Django: Administradores, conexion y acceso
a la base de datos, aplicaciones instaladas, sesiones etc.
-Es un módulo Python normal con variables a nivel de
módulo que representan configuraciones de Django

4) urls.py
-La declaración de las URL para este proyecto de Django;
-Es como una tabla de contenidos de tu sitio hecho con Django.
-Las URLs(Localizador uniforme de recursos: Sirve para nombrar recursos
en Internet o en servidores locales. Tiene como proposito asignar una 
direccion unica a cada uno de los recursos disponibles ejemplo:
textos, imagenes, vdeos, etc...) para este proyecto Django
-Contiene las direcciones URL de este proyecto Django.
-Al principio no contiene ninguna.

(Estos archivos ya constituyen una aplicación Django de trabajo)

**********El servidor de desarrollo**********

-Entrar al directorio (NombreDelProyecto)
y ejecuta el comando:

$ python manage.py runserver #Verás la siguiente salida en la línea de comandos:

$ python manage.py check #Validar los modelos en busca de errores sin necesidad de correr el servidor.

Validating models...

0 errors found
February 22, 2015 - 13:35:04
Django version 1.5.12, using settings 'NombreDelProyecto.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

(Arranca el servidor de desarrollo de Django
un servidor web liviano escrito completamente en Python.
Se incluye en Django para que puedas desarrollar de manera rápida
sin tener que vértelas con la configuración de un servidor de producción
como Apache, hasta que estés listo para producción)

-Cuando el servidor está inicializado, visita http://127.0.0.1:8000/
usando un navegador web. Se observara una página "Welcome to Django"

-Por defecto, el comando runserver arranca el servidor de desarrollo
en el puerto 8000

python manage.py runserver 8080 #Arranca el servido en el puerto 8080

python manage.py runserver 0.0.0.0:8000 #Cambiando la direccion IP

**********Configuración de la base de datos**********

En settings.py se pueden configurar los privilegios, nombre, etc a la base de datos. 

ENGINE -- Ya sea 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql'
o 'django.db.backends.sqlite3'. Otros backends también están disponibles.

NAME -- El nombre de tu base de datos. Si estás usando SQLite la base de datos
será un archivo en tu ordenador; en tal caso, NAME debería ser la ruta absoluta
incluyendo nombre de archivo, de dicho archivo. Si el archivo
no existe se creará automáticamente cuando sincronices la base
de datos por primera vez.

USER -- El usuario de la base de datos (no usado en SQLite).

PASSWORD -- La contraseña de la base de datos (no usado en SQLite).

HOST -- La máquina donde está ubicada la base de datos.
Déjalo como una cadena vacía si la base de datos está en la misma
máquina física (no usado en SQLite).

(Si las bases de datos son algo nuevo para ti te recomendamos usar
simplemente SQLite (poniendo en ENGINE 'django.db.backends.sqlite3'). 
SQLite viene incluido como parte de Python 2.5 y superior
así que no tendrás que instalar nada.)

(Si se esta usando PostgreSQL o MySQL, se debe haber creado una base de datos.
Lo puedes hacer con el comando "CREATE DATABASE nombre_basededatos;"
en el intérprete interactivo de tu base de datos)

-En settings.py, la variable INSTALLED_APPS contiene el nombre de todas
las aplicaciones Django que están activadas en esta instancia de Django.
Las aplicaciones pueden ser empacadas y distribuidas para ser usadas por otros proyectos.

Por defecto, INSTALLED_APPS contiene las siguientes aplicaciones, todas ellas vienen con Django:

-django.contrib.auth -- Un sistema de autenticación.
-django.contrib.contenttypes -- Un framework para tipos de contenidos.
-django.contrib.sessions -- Un framework para manejar sesiones.
-django.contrib.sites -- Un framework para manejar múltiples sitios con una única instalación Django.

**********Creando APLICACIONES**********

-La aplicacion se creara en el directorio (NombreDelProyecto) con:

python manage.py startapp NombreAplicacion

-Esto creará un directorio NombreAplicacion, que contiene los siguiente archivos:

- __init__.py

- models.py: En este archivo es donde vamos a crear nuestras tablas de las bases de datos.
Un modelo de Django es una descripción de los datos en la base de datos, esta es tu capa de datos

- tests.py

- views.py: En este archivo es donde pondremos todas las funciones que necesitemos
ejecutar en nuestro proyecto

--- Las variables las llamo en mi template así: {{ variable }}

--- render()
-Es un idioma muy común para cargar una template llenar un contexto
y retornar un objeto HttpResponse con el resultado de una template
renderizada.
-La función render toma como primer argumento la solicitud (objeto
request), el nombre de una template como segundo argumento y un
diccionario como tercer argumento. Este devuelve un objeto
HttpResponse de la template solicitada renderizada con el contexto
dado.

--- render_to_response()

-El primer argumento de render_to_response() debe ser el nombre de la plantilla a utilizar.
-El segundo argumento, si es pasado, debe ser un diccionario para usar en la creación de un
Context para esa plantilla.
-Si no se le pasa un segundo argumento, render_to_response() utilizará un diccionario vacío.

///////////////Creando proyectos:

*****Crear el proyecto
django-admin startproject NombreDelProyecto

*****Configura el settings
Configurar zona horaria, lenguaje
--> Using Language Identifiers: http://www.i18nguy.com/unicode/language-identifiers.html

*****Configurar la base de datos
Elegir el motor y el nombre de la db, si se usa postgres esta debe estar creada y tner un usuario, si se
usa sqlite3 no hace falta crearla, solo agregando el nombre Django la crea

*****Habilitar el administrador (apps,urls)
Descomentar las lineas correspondientes en el settings/apps y en el urls

*****Sincronisar la db
python manage.py syncdb

*****Crear el super usuario
Escribir el user, pass y email del superuser

*****Correr el servidor, validar los modelos y probar el admin
Probar el admin /admin 

python manage.py runserver

*****Crear aplicacion y registrarla en el settings
python manage.py startapp NombreAplicacion

*****Crear carpeta templates y declararla en el settings
Declarar la carpeta de nuestras plantillas en el settings en 
TEMPLATE_DIRS con la ruta completa '/home/osorio/Escritorio/inscripcion/templates'

*****Abrir el views.py y declarar la funcion con el render y la template que corresponda
En la vista iran nuestras funciones y clases y decimos que plantillas
vamos a usar 

*****Crear el Index de la funcion y guardarlo en templates
Crear el html y guardarlo en nuestra carpeta de plantillas 

*****Declarar la funcion de la vista en las urls
Las vistas deben ser declaradas en las urls
url(r'^$', 'aplicacion.views.funcion', name='funcion'),

*****Probar el index con el servidor andando
python manage.py runserver

*****Creamos los modelos 
En el models.py crearemos las clases que al final
seran nuestras tablas con sus campos en nuestra base de datos 

python manage.py sqlall books / books es el nombre de la aplicación, podremos
observar nuestros modelos de datos antes de crear las tablas con la sincronizacion de la db

*****Sincronizamos la db 
Al sincronizar, las clases que creamos en los modelos
se generaran en tablas de nuestra base de datos 

python manage.py syncdb

*****Corremos el servidor y entramos al admin para ver nuestras tablas
En principio no veremos nuestras tablas en el admin, tenemos que crear el archivo admin.py
en el directorio de la aplicacion y declaramos

from django.contrib import admin 
from .models import NombreClase

admin.site.register(NombreClase) 

volvemos a correr el servidor, entramos al admin y ya podemos ver nuestra tabla creada
y podemos llenarla de datos

*****Creamos un template donde mostraremos nuestro formulario
basado en los modelos de la base de datos, podemos usar el modelo como base para los 
forms, creamos el template con el formulario, el metodo etc

<FORM method="POST"> {% csrf_token %} #Este token lo agregamos por segridad, Django lo exige
		{{ form }}
		<input type="submit" value="Enviar">
</FORM>

*****En la vista creamos una clase que contendra nuestro modelo

class RegistrarAlumno(CreateView):
	template_name = "registrar.html"
	model = Alumno

Con esto mandamos a la plantilla declarada un form el cual recibe el form en el template
asignado

*****Declaramos nuestra clase en la URLS para que la lea como vista 
url(r'^registrar/$', RegistrarAlumno.as_view(), name='RegistrarAlumno'),
####Debemos revisar siempre los import, son muy importantes

*****Declarando los CSS

Creamos la carpeta static que contendra nuetros css, imagenes y demas
archvos estaticos, se debe guardar a nivel de las plantillas
 (aplicacion/static/css/estilo.css)
 (aplicacion/templates/index.html)

 Con esto llamamos nuestro CSS en la plantilla:

 <head>
	<title>PAGOS</title> 
	<meta http-equiv="content-type" content="text/html;charset=utf-8" /> 
	<meta charset="UTF-8" /> 
	{% load staticfiles %}	
	<link rel="stylesheet" type="text/css" href="{% static 'css/estilo.css' %}" />
</head>

*****Agregando imagenes a la plantilla

Los archivos de media seran llamados de la carpeta Img
que por lo general acompaña al css, se hace referencia a la 
carpeta static con {{STATIC_URL}} y luego la ruta de la imagen:
Ejemplo:

<img src="Imagen.jpg" width="200px" heigth="200px"></img>

<img src="{{STATIC_URL}}css/Img/gris.JPG"></img> Agregando una imagen local 

#Estructura de un proyecto, algunos directorios
#debemos crearlos nosotros por ejemplo: templates, static, admin.py

project
  manage.py
  database.db  
  project/
    settings.py
    urls.py
    wsgi.py

  app/
    templates/
      app/
        base.html
        index.html      
    admin.py
    tests.py
    models.py
    forms.py
    views.py  
    
    static/
      css/
        styles.css

    img/ 
      a.jpg
      b.png

    js/
      jquery.js
-----

Recommended Django Project Layout

myproject/
    manage.py
    myproject/
        __init__.py
        urls.py
        wsgi.py
        settings/
            __init__.py
            base.py
            dev.py
            prod.py
    blog/
        __init__.py
        models.py
        managers.py
        views.py
        urls.py
        templates/
            blog/
                base.html
                list.html
                detail.html
        static/
           …
        tests/
            __init__.py
            test_models.py
            test_managers.py
            test_views.py
    users/
        __init__.py
        models.py
        views.py
        urls.py
        templates/
            users/
                base.html
                list.html
                detail.html
        static/
            …
        tests/
            __init__.py
            test_models.py
            test_views.py
     static/
         css/
             …
         js/
             …
     templates/
         base.html
         index.html
     requirements/
         base.txt
         dev.txt
         test.txt
         prod.txt

##############################
##### Modelos en Django  #####
##############################

¿Qué es un modelo?

- En Django los modelos son como django tratara los datos, contendrá los campos de los objetos que queremos guardar.
Generalmente django creara por cada modelo una tabla en la base de datos.

- Cada modelo es una clase python que hereda de django.db.models.Model

- Cada atributo del modelo representa un campo de la tabla de la base de datos.

##### Los campos #####

Los campos son el tipo de objeto del atributo que guardara, hay varios tipos:

AutoField: Es un IntegerField que se incrementa cuando creas un nuevo objeto, casi que no es necesario ya que django lo crea solo si no especificas otro campo como id.

BigIntegerField: Representa un Entero de 64 bit, es como el IntegerField, solo que permite números desde el -9223372036854775808 hasta el 9223372036854775807. El campo por defecto de los formularios es el TextField.

BooleanField: El campo de true/false. El campo por defecto de los formularios es un CheckboxInput. El vlaor por defecto es None si no defines el default.

CharField: Para string pequeños, frases o palabras. El campo por defecto en los formularios es el TextInput.
    max_length=20: Establece el tamaño máximo del string, es requerido.

CommaSeparateIntegerField: Guarda una lista de enteros separados por coma. 
    Max_length=20: Establece el valor máximo de los enteros, es requerido.

DateField: Guarda una instancia de la fecha a partir de la clase datetime.date de python.
    auto_now=True: Actualiza la fecha cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la fecha de cuando se creo.

DateTimeField: Como el DateField solo que guarda también la hora
    auto_now=True: Actualiza la fecha cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la fecha de cuando se creo.

DecimalField: Guarda números decimales.
    max_digits=5: Establece el numero de dígitos máximo, la suma de la parte entera y la decimal
    decimal_places=2: Establece el número de dígitos de la parte decimal.

EmailField: Es un CharField que comprueba lo introducido para verificar que sea un email.
    max_length=75: Establece el tamaño máximo del email, es requerido.

FileField: Sirve para guardar archivos en el servidor. En el formulario saldría el campo de escoger un fichero del ordenador. Tiene que estar definido el MEDIA_ROOT en el settings para que guarde los archivos. Guardara el archivo en la ruta especificada por el MEDIA_ROOT.
    upload_to='/videos': Subirá el archivo a la carpeta vídeos alojada en la carpeta definida por MEDIA_ROOT. (Requerido)
    FileField(upload_to='/video'[, max_length=100, **options]): si se quiere poner los atributos opcionales tendrán que añadirse así.

FilePathField: Sirve para mostrar los archivos accesible de una carpeta siguiendo una restricción si se quiera, para hacer alguna operación sobre ellos.
    FilePathField(path=None[, match=None,recursive=False, max_length=100, **options])
        path (requerido): directorio del que sacara FilePathField las opciones.
        match: filtro por el que pasaran los archivos, se usaran expresiones regulares.
        recursive: False por defecto, especifica si entran las subcarpetas de la ruta indicada por path.
        max_length: Indica el tamaño máximo del nombre del archivo.

FloatField: Campo que guarda una instancia del modelo Float de python.

ImageField: Como el FileField pero solo acepta formatos de imágenes. Tiene dos campos opcionales mas que el FielField
    height_field: Representa el alto máximo de la imagen.
    width_field: Representa el ancho máximo de la imagen.

IntegerField: Guarda un entero.

IPAddressField: Guarda un string que coincida con el formato ip (192.168.0.1).

GenericIPAddressField: Guarda una ip, ya sea ipv4 o ipv6. Para saber como las guarda Doc Django.

NullBooleanField: Como el BooleanField pero permite null.

PositiveIntegerField: Guarda un entero mayor o igual que cero.

SlugField:  Campo que guarda una pequeña etiqueta (letras, números, guiones) suele usarse en las url.

TextField: Campo que guarda texto.

TimeField: Guarda una hora, comparte los campos con DateField
    auto_now=True: Actualiza la hora cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la hora de cuando se creo.
URLField: Guarda una dirección html, comprueba que lo introducido sea una dirección html.

##### Campos de relación #####

ForeignKey:  Para referir objetos a un objeto, un modelo puede referirse a un modelo, pero un modelo puede estar referido a mas de uno, es lo que se llama un many-to-one referencia.

ManyToManyField: Para guardar una referencia a varios objetos de la misma clase. Hay que definir la clase con la que se relaciona. Va guardando las referencias a esos objetos en una lista con las primary keys referncia.

OneToOneField: Es como el ForeignKey pero tiene unique=True, por lo que solo puede haber una referencia a ese objeto.

##### Opciones que tiene todos los campos #####

null=True: Permite que los valores puedan ser null.

blank=True: Permite que el campo se pueda quedar en blanco.

choices=meses: Permite asignar un diccionario de elementos a un objetos para que los valores solo sean los contenidos en el diccionario. La clave del diccionario sera lo que se guarda en la base de datos, el valor asociado sera lo que se mostrar en el formulario que lo use.

db_column: El nombre de la columna donde django guardara el campo, si no se especifica guarda el nombre del campo.

db_index=True: Sirve para indexar el campo en las búsqueda de django. Por defecto django busca entre las PK de la base de datos, si añades esto también buscara entre esos datos y no tendrás que acceder directamente al objeto para comprobar el campo en las búsquedas.

db_tablespace: El nombre al que se referencia para buscar si ha sido indicado como index.

default: El valor por defecto que tiene el modelo, si se va a guardar un valor distinto a vació se guardara con el valor por defecto.

editable=False: Indica si el valor se puede modificar, si es falso no aparecerá en el admin ni similares.

error_messages={null:"Hay que darle un valor",blank:"No se puede dejar en blanco",invalid="El valor introducido es erróneo", invalid_choice:"Has escogido un valor inadecuado", unique="Este valor ya existe"}: Como se ve en el ejemplo hacer referencia a los mensajes que se mostraran si se produce ese error. No hace falta crear todos los mensajes. Si no los creas saldrá el que tiene por defecto.

help_text="Inserta un nombre": Un texto que aparecerá en forma de ayuda en el campo del formulario.

primary_key=True: Para asignar que el campos es la clave primaria del modelo.

unique=True: Indica que el valor es único, solo podrá haber uno en la base de datos.

unique_for_date='pub_date': El valor de esta propiedad tendrá que existir como campo del modelo y tendrá que ser del tipo DateField o DateTimeField. Lo que hace es no dejar que haya un elemento con el mismo valor del campo y el mismo día.

unique_for_month='pub_date': El valor de esta propiedad tendrá que existir como campo del modelo y tendrá que ser del tipo DateField o DateTimeField. Lo que hace es no dejar que haya un elemento con el mismo valor del campo y el mismo mes.

unique_for_year='pub_date': El valor de esta propiedad tendrá que existir como campo del modelo y tendrá que ser del tipo DateField o DateTimeField. Lo que hace es no dejar que haya un elemento con el mismo valor del campo y el mismo año.

verbose_name="Nombre de usuario": Nombre del campo comprensible por humanos, si no se crea django lo generar automáticamente, convirtiendo los guiones en espacios.

validators=[]: Una lista de validaciones para el campo referencia.

##### Declarando la clase Articulo y Comentarios para una publicacion, y estableciendo
#la relacion entre los comentarios y un articulo #####
from django.db import models

class Articulo(models.Model):
   autor = models.CharField(max_length = 30)
   titulo = models.CharField(max_length = 100)
   texto = models.TextField()
   fecha = models.DateTimeField()

class Comentario(models.Model):
   nombre = models.CharField(max_length = 200)
   cuerpo = models.TextField()
   fecha_pub = models.DateTimeField('fecha publicacion')
   articulo = models.ForeignKey(Articulo)

#Modelos para un blog, con un método para la fecha de publicación.
#Más en --> https://tutorial.djangogirls.org/es/

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

##############################################################################
##### Ejemplo de admin.py para mostrar los modelos en el admin de django #####
##############################################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

admin.site.register(Post)

##### Pasando un diccionario en el render #####

xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
chartdata = {'x': xdata, 'y': ydata}
charttype = "pieChart"
chartcontainer = 'piechart_container'
data = {
    'charttype': charttype,
    'chartdata': chartdata,
    'chartcontainer': chartcontainer,
    'extra': {
        'x_is_date': False,
        'x_axis_format': '',
        'tag_script_js': True,
        'jquery_on_ready': False,
    }
}
return render_to_response('piechart.html', data)

##################################
##### Creating an admin user #####
##################################

First we’ll need to create a user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser

Enter your desired username and press enter.

Username: admin

You will then be prompted for your desired email address:

Email address: admin@example.com

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.

##################################################
##### Permisos de contenido según el usuario #####
##################################################

{% if user.is_staff %}
<h1>Soy Admin </h1>
{% else %}
<h1>No soy Admin </h1>
{% endif %}

#######################################################
##### Ruta de instalación convencional de Django ######
#######################################################

$ python
>>> import django
>>> django.__file__
'/usr/local/lib/python2.7/dist-packages/django/__init__.pyc'

####################################################################
##### Ruta de instalación de Django dentro de entorno virtual ######
####################################################################

/home/user/Entornos_virtuales/Django_1.10.1/local/lib/python2.7/site-packages/django

####################################
##### Recolectar los estáticos #####
####################################

Cuando el:

$ python manage.py collectstatic

falla, se pueden recolectar manualmente los estáticos, solo hay que buscar la ruta adecuada dentro del core de django, en
un entorno virtual sería en:

/home/user/Entornos_virtuales/Django_1.10.1/local/lib/python2.7/site-packages/django/contrib/admin/static/

Dentro está la carpeta admin/ con todos los estáticos que necesita el servidor, sobre todo los estáticos del admin de django, por lo tanto
podemos copiar esa carpeta admin/ a la carpeta static de nuestro proyecto.

###################################################################
##### Desplegar aplicación web en Django - pythonanywhere.com #####
###################################################################

Tutorial en Español en --> ttps://stories.devacademy.la/django-y-como-desplegar-tu-peque%C3%B1a-aplicaci%C3%B3n-web-y-no-morir-en-el-intento-e18551c0c8b6#.z8mol0onp

Otro Tutorial en Español en --> https://tutorial.djangogirls.org/es/deploy/

Pythonanywhere que cuenta con un sin fin de paquetes de Python y soporta Python desde la ultima versión estable de la 2.7.x y
las ultimas versiones estables de la 3.x.

1) Creamos una cuenta en Pythonanywhere como principiante ( Beginner), lo que nos da un plan gratuito (obviamente con algunas
limitaciones, como solo poder crear o desplegar un proyecto por cuenta).

Al ingresar vamos a dar click en Dashboard para acceder a nuestro panel principal en donde tendremos 5 pestañas especiales de las cuales
en esta vez solo usaremos 4: Consoles, Files, Web y Databases. En la pestaña de consola podremos elegir abrir una consola bash que nos 
situará en el directorio de nuestro usuario: /home/dm/ desde la consola podemos clonar repositorios y para nuestro caso podemos clonar el proyecto
que queremos desplegar. También podemos entornos virtuales por si necesitamos paquetes python adicionales, por defecto nuestra sesion en bash ya
tiene instalado django 1.10 y python 2.7.x.

Cuando te hayas registrado en PythonAnywhere serás redirigida a tu panel de control o página "Consoles". Elije la opción para iniciar una consola "Bash", que
es la versión PythonAnywhere de una consola, como la que tienes en tu PC.

Descarguemos nuestro código desde GitHub a PythonAnywhere mediante la creación de un "clon" del repositorio. Escribe lo siguiente en la consola de PythonAnywhere:

$ git clone https://github.com/<tu-usuario-github>/my-first-blog.git

Ahora toca configurar el fichero WSGI, Django funciona utilizando el "protocolo WSGI", un estándar para servir sitios web usando Python, que PythonAnywhere soporta. La forma de configurar PythonAnywhere para que reconozca nuestro blog Django es editar un fichero de configuración WSGI.

Haz clic en el enlace "WSGI configuration file" (en la sección "Code" en la parte de arriba de la página; se llamará algo parecido a /var/www/<tu-usuario>_pythonanywhere_com_wsgi.py) y te redirigirá al editor, o tambien lo puedes editar desde la consola web, eso está en /var/www

Lo que me ha funcionado es crear un proyecto desde la interfaz web y luego desde la pestaña web modificar las rutas para que apunten al proyecto que clone.

##### Tips #####

- El nombre de usuario que elijamos sera parte de nuestro subdominio en la web, es decir, si mi usuario es dm, el dominio de mi web/applicación sera:
--> dm.pythonanywhere.com es decir, cuando elijas tu nombre de usuario ten en cuenta que la URL de tu blog tendrá la forma nombredeusuario.pythonanywhere.com, así
que o bien elije tu propio apodo o bien un nombre que describa sobre qué trata tu blog.

- En /var/www está el fichero usuario_pythonanywhere_com_wsgi.py para editarlo, lo reemplazamos todo con lo siguiente:

import os
import sys

path = '/home/{mi usuario}/default'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "default.settings")

application = get_wsgi_application()

########################################
##### Graficando modelos de Django #####
########################################

Cuando desarrollas en Django la logica la mandas a los modelos. A veces nos abastraemos de la capa y lo que se escribe en la base de datos, para esto
siempre es bueno poder visualizar de manera gráfica los modelos del proyecto.

Para Django existe una orma de poder graficar los modelos con PyGraphviz, que es un software de visualización.

Para instalar PyGraphviz usaremos pip:

$ pip install pygraphviz

ya instalado la extensión, vamos a nuestro proyecto y ejecutamos:

my_project$ ./manage.py graph_models -a -g -o mi_modelo.png

Lo que nos creará un archivo PNG con el modelo de datos.

Si obtienes un error como

from django.conf import settings; ‘django_extensions’ in settings.INSTALLED_APPS
 
Es porque debes instalar django-extensions con:

$ pip install django django-extensions

Y luego debes agregar django-extensions a las INSTALLED_APPS en tu archivo settings.py de tu proyecto
 

INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)

#############################################
##### Mensajes / messages al hacer post #####
#############################################

- En la views.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import *
from django.contrib.messages.views import SuccessMessageMixin



class PostLista(ListView):
    model = Post



class PostCrear(SuccessMessageMixin,CreateView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se creó la publicación con éxito"



class PostActualizar(SuccessMessageMixin,UpdateView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se actualizó la publicación con éxito"



class PostEliminar(SuccessMessageMixin,DeleteView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se eliminó la publicación con éxito"

- En el template:

{% if messages %}
<ul class="messages">
{% for message in messages %}
<li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
{% endfor %}
</ul>
{% endif %}

ó

{% if messages %}
  {% for message in messages %}
    <div class="alert alert-success" role="alert">
      {% if message.tags %}{% endif %}>
      {{ message }}
    </div>
  {% endfor %}
{% endif %}


### En un render ###

messages = '¡Registro exitoso!'
return render_to_response('base.login.html', {'messages': messages})

En el template:

{% if messages %}
  <div class=" warning">
    {{ messages }}
  </div>
{% endif %}
