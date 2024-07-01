package paquete;

import java.time.LocalDateTime;

public class Transaccion {
	// Variables propias de la clase
	private String id;
	private Cliente cliente;
	private Empleado empleado;
	private Item item;
	private String fecha;
	
	// Constructor predefinido
	public Transaccion() {
		this.id = "";
		this.cliente = new Cliente();
		this.empleado = new Empleado();
		this.item = new Item();
		this.fecha = "";
	}

	// Constructor con todos los parametros
	public Transaccion(String id, Cliente cliente, Empleado empleado, Item item, String fecha) {
		super();
		this.id = id;
		this.cliente = cliente;
		this.empleado = empleado;
		this.item = item;
		this.fecha = LocalDateTime.now().toString();
	}

	// Getters y Setters
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	public Empleado getEmpleado() {
		return empleado;
	}

	public void setEmpleado(Empleado empleado) {
		this.empleado = empleado;
	}

	public Item getItem() {
		return item;
	}

	public void setItem(Item item) {
		this.item = item;
	}

	public String getFecha() {
		return fecha;
	}

	public void setFecha(String fecha) {
		this.fecha = fecha;
	}

	// toString
	@Override
	public String toString() {
		return "Transaccion [id=" + id + ", cliente=" + cliente + ", empleado=" + empleado + ", item=" + item
				+ ", fecha=" + fecha + "]";
	}
}
