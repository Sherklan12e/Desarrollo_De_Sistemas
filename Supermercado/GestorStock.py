from Producto import Producto
class GestorStock:
    def __init__(self):
        self.productos = {}  # clave: código, valor: objeto Producto

    def alta_producto(self, codigo, nombre, precio, cantidad):
        if codigo in self.productos:
            print(f"❌ Error: El producto con código '{codigo}' ya existe.")
            return
        nuevo = Producto(codigo, nombre, precio, cantidad)
        self.productos[codigo] = nuevo
        print(f"✅ Producto '{nombre}' dado de alta correctamente.")

    def baja_producto(self, codigo):
        producto = self.productos.get(codigo)
        if not producto:
            print(f"❌ Error: No existe un producto con código '{codigo}'.")
            return
        if not producto.activo:
            print(f"⚠️ El producto '{producto.nombre}' ya está dado de baja.")
            return
        producto.activo = False
        print(f"🗑️ Producto '{producto.nombre}' dado de baja correctamente.")

    def modificar_producto(self, codigo, nuevo_nombre=None, nueva_cantidad=None):
        producto = self.productos.get(codigo)
        if not producto:
            print(f"❌ Error: No existe un producto con código '{codigo}'.")
            return
        if nuevo_nombre:
            producto.nombre = nuevo_nombre
        if nueva_cantidad is not None:
            producto.cantidad = nueva_cantidad
        print(f"✏️ Producto '{codigo}' modificado correctamente.")

    def mostrar_productos(self):
        print("\n📦 Lista de productos:")
        for producto in self.productos.values():
            print(producto)
