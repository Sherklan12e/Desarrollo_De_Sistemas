
namespace Biblioteca;
public class  Producto
{
    public string Nombre {get; set;}
    public decimal PrecioUnitario {get; set;}
    public int CantidadStock {get; set;}

public Producto(string nombre, decimal precioUnitario,int cantidadStock)
{
    Nombre = nombre;
    PrecioUnitario = precioUnitario;
    CantidadStock = cantidadStock;
}
}