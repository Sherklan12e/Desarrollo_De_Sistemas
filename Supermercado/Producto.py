class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo  # único
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.activo = True  # para indicar si está dado de baja o no

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} x {self.cantidad} unidades ({estado})"
