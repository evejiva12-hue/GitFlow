# Sistema de Inventario - NovaTech Solutions
# Estructura base para el manejo de productos (ID, Nombre, Precio, Categoría, Stock)

inventario = []

def mostrar_menu():
    print("\n--- SISTEMA DE INVENTARIO NOVATECH ---")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Salir")

if __name__ == "__main__":
    print("Sistema inicializado correctamente.")

def crear_producto(inventario):
    print("\n--- Registrar Nuevo Producto ---")
    id_prod = input("Ingrese ID: ")
    nombre = input("Ingrese Nombre: ")
    precio = float(input("Ingrese Precio: "))
    categoria = input("Ingrese Categoría: ")
    stock = int(input("Ingrese Stock: "))
    
    nuevo_producto = {
        "id": id_prod,
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "stock": stock
    }
    inventario.append(nuevo_producto)
    print(f"¡Producto '{nombre}' agregado con éxito!")