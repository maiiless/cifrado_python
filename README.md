# Cifrado César

## ¿Qués es el cifrado César?
Es un método de cifrado muy antiguo y basado en la sustitución de caracteres de acuerdo al desplazamiento. Por ejemplo para cifrar HELLO, H es la posición inicial y luego desplazamos 3 caracteres a la derecha en el abecedario dando como resultado la letra K. Repetimos el mismo proceso para el resto de la palabra, obteniendo el texto cifrado KHOOR. Para realizar el descifrado desplazamos la misma cantidad de caracteres pero hacia la izquierda. 

La fórmula matemática que se utiliza es: c = (x + n) % 26. Donde c es el carácter codificado, x es el carácter real, y n es el número de posiciones en las que queremos desplazar el carácter x. Estamos tomando mod con 26 porque hay 26 letras en el alfabeto inglés.

Referencia: https://likegeeks.com/es/cifrado-cesar-python/#¿Que_es_el_cifrado_Cesar

## Cifrado César en Python
Para realizar el cifrado en Python, necesitamos conocer qué es el código ASCII y utilizar las funciones ord() y chr() de Python.
   
### El código ASCII
  
  Es un estándar de codificación de 7 bits para la representación de números, letras y otros caracteres.
  Tabla de código ASCII: https://www.ascii-code.com

### Función ord()
  
  Al proporcionarle una cadena representando un carácter Unicode, retorna un entero que representa el código Unicode de ese carácter.
  Referencia: https://docs.python.org/es/3/library/functions.html#ord
  
### Función chr()
  
  Retorna la cadena que representa un carácter Unicode.
  Referencia: https://docs.python.org/es/3/library/functions.html#chr
