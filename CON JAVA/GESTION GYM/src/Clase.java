package paquete;

public class Clase {
	// Variables propias de la clase
	private String id;
	private String nombre;
	private String horario;
	private Empleado instructor;

	// Constructor predefinido
	public Clase() {
		this.id = "";
		this.nombre = "";
		this.horario = "";
		this.instructor = new Empleado();
	}

	// Constructor con todos los parametros
	public Clase(String id, String nombre, String horario, Empleado instructor) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.horario = horario;
		this.instructor = instructor;
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

	public String getHorario() {
		return horario;
	}

	public void setHorario(String horario) {
		this.horario = horario;
	}

	public Empleado getInstructor() {
		return instructor;
	}

	public void setInstructor(Empleado instructor) {
		this.instructor = instructor;
	}

	// toString
	@Override
	public String toString() {
		return "Clase [id=" + id + ", nombre=" + nombre + ", horario=" + horario + ", instructor=" + instructor + "]";
	}
}
