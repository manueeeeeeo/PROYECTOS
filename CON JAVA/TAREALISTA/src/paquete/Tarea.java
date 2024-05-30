package paquete;

/**
 * @author Manuel
 * @version 1.0
 */

public class Tarea {
	// Variables propias de la clase
	private int id;
	private String titulo;
	private String descripcion;
	private boolean completado;
	
	// Constructor predefinido
	public Tarea() {
		this.id = 0;
		this.titulo = "";
		this.descripcion = "";
		this.completado = false;
	}

	// Constructor con todos los parametros
	public Tarea(int id, String titulo, String descripcion, boolean completado) {
		this.id = id;
		this.titulo = titulo;
		this.descripcion = descripcion;
		this.completado = completado;
	}

	// Getters y Setters
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public boolean isCompletado() {
		return completado;
	}

	public void setCompletado(boolean completado) {
		this.completado = completado;
	}

	// toString
	@Override
	public String toString() {
		return "Tarea [id=" + id + ", titulo=" + titulo + ", descripcion=" + descripcion + ", completado=" + completado
				+ "]";
	}
}