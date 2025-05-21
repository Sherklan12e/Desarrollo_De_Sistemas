from Producto import Producto
from GestorStock import GestorStock

# Crear el gestor
gestor = GestorStock()

# Alta de productos
gestor.alta_producto("001", "Leche", 150.0, 30)
gestor.alta_producto("002", "Pan", 100.0, 50)
gestor.alta_producto("001", "Leche Descremada", 170.0, 25)  # error

# Mostrar productos
gestor.mostrar_productos()

# Modificar un producto
gestor.modificar_producto("002", nuevo_nombre="Pan Integral", nueva_cantidad=40)
gestor.modificar_producto("999", nuevo_nombre="No Existe")  # error

# Baja de productos
gestor.baja_producto("001")
gestor.baja_producto("001")  # error: ya dado de baja
gestor.baja_producto("999")  # error: no existe

# Mostrar productos otra vez
gestor.mostrar_productos()
