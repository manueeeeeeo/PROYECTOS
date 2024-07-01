package paquete;

public class Item {
	// Variables propias de la clase
	private String id;
	private String nombre;
	private double precio;
	
	// Constructor predefinido
	public Item() {
		this.id = "";
		this.nombre = "";
		this.precio = 0.0;
	}

	// Constructor con todos los parametros
	public Item(String id, String nombre, double precio) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.precio = precio;
	}

	// Getters y Setters
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

	// toString
	@Override
	public String toString() {
		return "Item [id=" + id + ", nombre=" + nombre + ", precio=" + precio + "]";
	}
}
