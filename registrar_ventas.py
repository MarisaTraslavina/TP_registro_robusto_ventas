from rich import print

def total_ventas():
    try:
        precio = input("Ingrese el precio del producto: $")
        cantidad = input("Ingrese la cantidad del producto: ")

        #Condiciones para hacer robusto "precio"
        try:
            precio = float(precio)

        except ValueError:
            raise ValueError("[black on red]Debe ingresar un precio válido![/black on red]")
        
        if precio <= 0: raise ValueError("[red]El precio no debe ser negativo ni cero[/red]")
        
        #Condiciones para hacer robusta "cantidad"
        try:
            cantidad = int(cantidad)
        
        except ValueError:
            raise ValueError("[black on red]Debe ingresar una cantidad válida![/black on red]")
        
        if cantidad <= 0: raise ValueError("[black on red]La cantidad no debe ser negativa ni cero[/black on red]")

        #Cálculo del precio de ventas totales
        total = precio * cantidad
        
    except ValueError as error:
        print(f"[magenta]Error: {error}.\nIntente nuevamente.[/magenta]")

    else:
        print(f"\n[green]Venta registrada. Total ${total:.2f}[/green]")

    finally:
        print("Fin del programa.")

total_ventas()