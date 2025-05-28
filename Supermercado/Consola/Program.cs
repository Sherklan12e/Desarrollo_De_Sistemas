using Biblioteca;
Gestion gestion = new Gestion();
bool seguir = true;
while (seguir)
{
    Console.WriteLine("Hola,Ingrese la operacion que desea hacer: ");
    Console.WriteLine("1 =  Dar de alta ");
    Console.WriteLine("2 =  Dar de baja ");
    Console.WriteLine("3  = Modificar producto ");
    Console.WriteLine("4 = Mostrar la lista de producto");
    Console.WriteLine("Para salir presione cualquier tecla");
    string ingresado = Console.ReadLine();
    switch (ingresado)
    {
        case "1":
            Console.Write("Nombre del producto: ");
            string nombre = Console.ReadLine();
            Console.Write("Precio del producto: ");
            decimal precioUnitario = Convert.ToDecimal(Console.ReadLine());
            Console.Write("Cantidad de Stock: ");
            int cantidadStock = Convert.ToInt32(Console.ReadLine());
            Producto producto1 = new Producto(nombre, precioUnitario, cantidadStock);
            gestion.CrearProductos(producto1);
            break;
        case "2":
            Console.WriteLine("Nombre del producto que desea eliminar");
            nombre = Console.ReadLine();
            gestion.EliminarProducto(nombre);
            break;
        case "3":
            Console.WriteLine("Que producto desea modificar?");
            string NombreModificar = Console.ReadLine();
            if (!   gestion.ExisteProducto(NombreModificar))
            {
                Console.WriteLine("No existe un producto con ese nombre.");
                break;
            }
            Console.WriteLine("Cual sera el nuevo nombre del producto");
            string NombreNuevo = Console.ReadLine();
            Console.WriteLine("Cual sera el nuevo precio del producto");
            int PrecioModificar = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Cual sera el nuevo stock del producto");
            int StockModificar = Convert.ToInt32(Console.ReadLine());
            gestion.ModificarProducto(NombreModificar, NombreNuevo, PrecioModificar, StockModificar);
            break;
        case "4":
            Console.WriteLine("Productos en la tienda");
            gestion.VerProductos();
            break;
            default:
            Console.WriteLine("Saliendo del programa");
            seguir = false;
            break;



    }
}
