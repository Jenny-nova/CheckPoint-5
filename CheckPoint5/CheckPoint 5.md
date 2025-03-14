# Documentación para Nuevos Desarrolladores de Python

## ¿Qué es un condicional? ¿Para qué se utiliza?

Los **condicionales** hacen que tu programa sea dinámico, y con eso me refiero a que tu programa puede empezar a tomar decisiones. Básicamente, son simplemente una forma de decir, que si se produce una situación, quiero que como programa realices una tarea, pero si se produce una situación diferente quiero que realices esta otra tarea.   
Puedes pensar en tus condicionales como si tuvieran una respuesta de tipo sí o no. Entonces, si esa condición se cumple, es un sí. Si la condición no se cumple, es un no. Y luego también tienes la capacidad de ramificar y dar condiciones secundarias para hacer que tus sistemas sean aún más especializados.  
En Python, los condicionales se implementan con las siguientes palabras clave:  
- `if`: se usa para verificar la primera condición.  
- `elif`: se usa para verificar condiciones adicionales si la primera no es verdadera.  
- `else`: se usa para ejecutar una acción si ninguna de las condiciones anteriores se cumple.

### Sintaxis

```python

if condición:

   # Código a ejecutar si la condición es verdadera

elif otra_condición:

   # Código a ejecutar si la otra condición es verdadera

else:

   # Código a ejecutar si ninguna de las condiciones anteriores es verdadera

```
#### Ejemplo

```python

edad = 18

if edad < 18:

   print("Eres menor de edad, no puedes conducir")

elif edad > 100:

   print("Eres muy mayor, no puedes conducir")

else:

   print("Puedes conducir.")

```



### También tenemos la posibilidad de realizar condicionales compuestos en Python.

Con ellas puedes tomar decisiones más complejas en tu código. Se utilizan para evaluar múltiples condiciones al mismo tiempo, combinando diferentes expresiones lógicas como `and` , `or` y `not`. Es útil cuando necesitas que se cumplan varias condiciones para ejecutar un bloque de código específico.

#### Ejemplos de condicional compuesto

```python

username = 'jonsnow'

email = 'jon@snow.com'

password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':

   print('Access permitted')

else:

   print('Not allowed')

if username == 'jonsnow' or password == 'thenorth':

   print('Access permitted')

else:

   print('Not allowed')

```

#### Ejemplo  con combinaciones de ***or*** y ***and***

```python
if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':

   print('Access permitted')

else:

   print('Not allowed')

```
---

### ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los bucles son una parte esencial de la programación. En Python, hay dos tipos principales de bucles: `for` y `while`.

### 1. Bucle `for`

Se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena). Como desarrollador, no tienes que llevar un registro ni saber cuántos elementos hay en una lista, tupla o diccionario; puedes simplemente iterarlos. Si hay uno, lo recorrerá una vez; si hay 5000, lo recorrerá 5000 veces.

#### Sintaxis

```python  
for elemento in secuencia:  
   # Código a ejecutar para cada elemento
```
#### Ejemplo

```python

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:

   print(fruta)

   # Se imprimirá una lista con las frutas

```

### 2. Bucle `while`

Continuará tantas veces como quieras que continúe. En otras palabras, si tenemos 250 bolas en un cajón y establezco un bucle while para realizar la tarea de ir sacando dichas bolas pero no le digo al bucle while cuándo detenerse, incluso después de haberlo recorrido y haber girado la ruleta 250 veces para sacar las bolas, el bucle while seguirá ejecutándose. Si no implementas un bucle while correctamente, te encontrarás con lo que se llama un **bucle infinito** donde el programa nunca se detendrá. 

#### Sintaxis

```python

while condición:

   # Código a ejecutar mientras la condición sea verdadera
```
#### Ejemplo

En este ejemplo, el bucle seguirá ejecutándose mientras que el contador sea menor que 5\. Cada vez que se ejecuta el bucle, se imprime el valor actual del contador y luego se incrementa en 1\. Cuando el contador llega a 5, la condición se vuelve falsa y el bucle se detiene.

```python

contador = 0

while contador < 5:

   print(contador)

   contador += 1
```
### ¿Por qué son útiles?

Los **bucles** permiten ejecutar un bloque de código múltiples veces, lo que es esencial para tareas repetitivas, como:

- Procesar elementos en una lista.

- Realizar cálculos hasta que se cumpla una condición específica.

- Realizar tareas repetitivas como buscar en bases de datos o procesar archivos.

Gracias a los bucles, podemos reducir la repetición de código y hacer que nuestros programas sean más eficientes.

---

## ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es una forma concisa de crear listas en Python. Básicamente, eso significa que podemos configurar varios bucles `for-in` para que funcionen en una sola línea de código, y generar listas a partir de esos bucles.

Una de las mejores formas de entender cómo funciona una comprensión de listas es comparándola con la alternativa, es un conjunto de bucles `for-in` y condicionales que pueden colocarse todos dentro de una sola línea de código.

#### Sintaxis y ejemplo

La sintaxis básica de una lista por comprensión es la siguiente:

```python  
[expresión for item in iterable]
```

- ***expresión*** es el valor que deseas obtener (puede incluir operaciones o condiciones).  
- ***item*** es la variable de iterador.  
- ***iterable*** es la secuencia que se va a iterar (puede ser una lista, tupla, rango, etc.).

#### Ejemplo 1: Incrementar valores en una lista

Supongamos que tenemos una lista de números y queremos incrementar cada número en 1\. 

- El primer componente es la expresión que desea ejecutar, es muy importante entender que esta es la variable de iterador. Puede ser cualquier cosa que desees. En este caso es num pero podemos poner X ó Y. 

- La siguiente es la típica expresión for in. 

- Y luego el tercer componente es el contenedor.

```python  
    numbers = [1,2,3,4,5,6]  
    resultado = [num + 1 for num in numbers]  
    	print(resultado)  
```  

#### Ejemplo 2: Elevar al cubo los números en un rango

Aquí se crea una lista numérica donde el rango quiero que sean los números del 1 al 10\. Y mi objetivo para esto, es crear un conjunto de números al cubo, lo que significa que quiero multiplicar cada uno de los elementos en este rango y quiero elevarlos al cubo. Entonces, quiero agregar un exponente de 3 para que devuelva una lista donde cada uno de los elementos se haya elevado al cubo, así que configuraré una variable aquí llamada **cubed_nums**. 

Cuando envuelves esto entre corchetes, esto es lo que le dice a Python que no solo quieres hacer un bucle `for-in` para los elementos cúbicos, sino que también quieres generar dinámicamente una lista. 

```python  
num_list = range(1, 11)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)
```

### ¿Para qué se utiliza?

Las **listas por comprensión** son útiles porque nos permiten: 

- Crear listas de manera más clara y compacta, obteniendo **mayor legibilidad**

- Evitar el uso de bucles explícitos, lo que reduce la cantidad de código proporcionando una **mayor eficiencia**

- Realizar tareas repetitivas en una sola línea de código, mejorando la productividad y consiguiendo una **reducción de código**

Son especialmente útiles cuando necesitas generar listas de manera dinámica, aplicar transformaciones o filtrar elementos sin necesidad de escribir múltiples líneas de código.

---

## ¿Qué es un argumento en Python?

Un **argumento** es un valor que se pasa a una función cuando se llama a esta. Los argumentos son utilizados por la función para realizar su tarea. Los argumentos permiten que las funciones sean más flexibles y reutilizables, ya que se les puede pasar diferentes valores en distintas ocasiones.

#### Sintaxis:

```python
def mi_funcion(argumento1, argumento2):  
    print(argumento1, argumento2)
```
En este caso, argumento1 y argumento2 son los argumentos de la función mi_funcion.

#### Ejemplo:

```python

def saludar(nombre, edad):  
    print(f"Hola {nombre}, tienes {edad} años.")

saludar("Juan", 25)
```
En este ejemplo, la función saludar toma dos argumentos: nombre y edad. Cuando llamamos a la función con saludar("Juan", 25), le estamos pasando "Juan" como el valor de nombre y 25 como el valor de edad. El resultado será: Hola Juan, tienes 25 años.

### Tipos de Argumentos:

1. ***Argumentos Posicionales***: Son aquellos que se pasan en el orden en el que se definen en la función.

#### Ejemplo:

```python  
def sumar(a, b):  
    return a + b

print(sumar(3, 5))  # El resultado de la suma es 8
```

2. ***Argumentos por Nombre***: Puedes especificar el nombre del parámetro al pasar un argumento, lo que hace que el orden no importe.

#### Ejemplo:

```python    
def saludar(nombre, edad):  
    print(f"Hola {nombre}, tienes {edad} años.")

saludar(edad=30, nombre="Ana")  # El resultado es: Hola Ana, tienes 30 años.
```

3. ***Argumentos predeterminados***: Son argumentos que tienen un valor predeterminado. Si no se proporciona un valor al llamar a la función, se utiliza el valor por defecto. Esto, como se ve en el ejemplo, se anula, si al llamar a la función, si que le pasamos un argumento.

#### Ejemplo:

```python  
def saludar(nombre="Mundo"):

   return f"Hola, {nombre}!"

mensaje = saludar()  # El mensaje será: "Hola, Mundo!"

mensaje2 = saludar("Juan")  # El mensaje 2 será: "Hola, Juan!"
```

---

## ¿Qué es una función Lambda en Python?

Una **función lambda** es una función anónima *(sin nombre)* en Python. Se utiliza principalmente cuando se necesita una función pequeña para una operación corta y se prefiere no definir una función convencional con `def`.

#### Sintaxis

```python
lambda argumentos: expresión

```
#### Ejemplo Función lambda para sumar dos números:

```python
suma = lambda x, y: x + y

   print(suma(3, 5))  # Resultado: 8
```

La función lambda toma dos argumentos `x` e `y`, y devuelve la suma de ambos. Puede ser usada como cualquier otra función, pero sin la necesidad de usar la palabra clave `def`.

#### Usos habituales de funciones lamda:

1. Para **operaciones sencillas y rapidas**  que no requieren una función completa.

#### Ejemplo:

```python  
multiplicar = lambda a, b: a * b

   print(multiplicar(4, 6))  # Resultado: 24
```

2. Se pueden usar como **funciones como argumento** usando funciones lambda como argumentos en otras funciones, especialmente cuando se usan con funciones como `map()`, `filter()`, y `sorted()`.

#### Ejemplo de uso con map() donde tenemos una lista de números y queremos multiplicar cada uno por 2:

La función ***map()*** aplica la función lambda a cada elemento de la lista y con ***lambda x: x * 2,***  multiplica cada número por 2.

```python  
numeros = [1, 2, 3, 4, 5]

resultado = map(lambda x: x * 2, numeros)

print(list(resultado))

# Resultado: [2, 4, 6, 8, 10]
```

#### Conclusión:

Las **funciones lambda** son una herramienta poderosa y concisa en Python para realizar operaciones rápidas y para ser utilizadas como argumentos en otras funciones, especialmente cuando se necesita una función pequeña y no es necesario definir una función completa con *def*.

---

## ¿Qué es un paquete pip?

`pip` es el gestor de paquetes oficial de Python. Permite instalar, actualizar y gestionar bibliotecas o paquetes de Python de manera sencilla. Un paquete es una colección de módulos y scripts que amplían las funcionalidades de Python. Puedes usar `pip` para descargar e instalar estos paquetes desde el **Python Package Index (PyPI)**, que es el repositorio oficial de paquetes de Python.

### Instalación de pip

#### ¿Cómo instalar pip?

Si tienes Python 3.4 o superior, `pip` ya debería estar instalado automáticamente. Si necesitas instalarlo o actualizarlo, puedes hacerlo desde la línea de comandos o terminal.

**Para instalar pip (si no lo tienes)**:

1. Descarga el script `get-pip.py` desde [este enlace](https://www.python.org/downloads/).

2. Ejecuta el siguiente comando en la terminal:

	`python get-pip.py`

#### Sintaxis para usar pip:

**Instalar un paquete:**

*pip install nombre_del_paquete*

#### Ejemplo:

`pip install numpy`

Este comando instalará el paquete numpy en tu entorno Python.

**Actualizar un paquete:**

*pip install --upgrade nombre_del_paquete*

#### Ejemplo:

`pip install --upgrade numpy`

**Listar los paquetes instalados:**

`pip list`

Esto mostrará todos los paquetes que tienes instalados en tu entorno Python.

**Desinstalar un paquete:**

*pip uninstall nombre_del_paquete*

#### Ejemplo:

`pip uninstall numpy`

#### Ejemplo de Uso:

Si necesitas trabajar con matemáticas avanzadas, puedes instalar un paquete como numpy:

`pip install numpy`

Una vez instalado, puedes usar numpy en tu código para realizar operaciones matemáticas rápidas.

```python
import numpy as np

# Crear un array/matriz de números:

arr = np.array([1, 2, 3, 4])

print(arr)
```

### ¿Por qué es útil pip?

- Es **fácil de usar**, te permite instalar, actualizar y desinstalar paquetes con simples comandos en la terminal.

- Te permite instalar y usar miles de bibliotecas disponibles en PyPI, por lo que te da **acceso a miles de paquetes**

- Si tu proyecto depende de varios paquetes, pip te ayuda a gestionarlos y actualizarlos.

