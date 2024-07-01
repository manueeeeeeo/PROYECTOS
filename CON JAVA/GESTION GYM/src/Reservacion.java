package paquete;

import java.time.LocalDateTime;

public class Reservacion {
	// Variables propias de la clase
	private Cliente cliente;
	private Clase clase;
	private String fecha;
	
	// Constructor predefinido
	public Reservacion() {
		this.cliente = new Cliente();
		this.clase = new Clase();
		this.fecha = "";
	}

	// Constructor con todos los parametros
	public Reservacion(Cliente cliente, Clase clase) {
		super();
		this.cliente = cliente;
		this.clase = clase;
		this.fecha = LocalDateTime.now().toString();
	}

	// Getters y Setters
	public Cliente getCliente() {
		return cliente;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	public Clase getClase() {
		return clase;
	}

	public void setClase(Clase clase) {
		this.clase = clase;
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
		return "Reservacion [cliente=" + cliente + ", clase=" + clase + ", fecha=" + fecha + "]";
	}
}
