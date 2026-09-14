# Registro robusto de ventas

## Objetivo del programa

Este programa permite registrar una venta ingresando el **precio unitario de un producto** y la **cantidad vendida**, para luego calcular y mostrar el total de la venta.

El programa utiliza manejo de excepciones para controlar los datos ingresados por el usuario y evitar que el programa finalice inesperadamente ante entradas inválidas.

## Crear el entorno virtual

Desde la carpeta del proyecto, ejecutar:

```bash
python -m venv .venv
```

## Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Una vez activado, aparecerá el nombre del entorno virtual al comienzo de la línea de la terminal.

## Instalar las dependencias

Con el entorno virtual activado, instalar la biblioteca utilizada:

```bash
pip install rich
```
o también:

```bash
pip install -r requirements.txt
```

## Ejecutar el programa

Con el entorno virtual activado, ejecutar:

```bash
python registro_robusto_ventas.py o
py registro_robusto_ventas.py
```

## Situaciones inválidas contempladas

El programa controla las siguientes situaciones:

* El precio ingresado no puede convertirse a `float`, por ejemplo, `"mil quinientos"`.
* La cantidad ingresada no puede convertirse a `int`, por ejemplo, `"quince"`.
* El precio es negativo o cero.
* La cantidad es negativa.
* La cantidad es cero.

Cuando se produce un error, el programa muestra un mensaje indicando el problema y permite finalizar el intento de registro de la venta.

También contempla una venta válida, calculando el total mediante:

```text
precio × cantidad
```

## Biblioteca utilizada

Se utilizó la biblioteca **Rich**, que permite mejorar la presentación de la información en la terminal mediante colores y estilos.

En este proyecto se utiliza para mostrar los mensajes de error y el mensaje de venta registrada de una manera más clara y visual.