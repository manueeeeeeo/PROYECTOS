package paquete;

public class Turno {
	// Variables propias de la clase
	private String id;
	private String dia;
	private String horaInicio;
	private String horaFin;
	
	// Constructor predefinido
	public Turno() {
		this.id = "";
		this.dia = "";
		this.horaInicio = "";
		this.horaFin = "";
	}

	// Constructor con todos los parametros
	public Turno(String id, String dia, String horaInicio, String horaFin) {
		super();
		this.id = id;
		this.dia = dia;
		this.horaInicio = horaInicio;
		this.horaFin = horaFin;
	}

	// Getters y Setters
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getDia() {
		return dia;
	}

	public void setDia(String dia) {
		this.dia = dia;
	}

	public String getHoraInicio() {
		return horaInicio;
	}

	public void setHoraInicio(String horaInicio) {
		this.horaInicio = horaInicio;
	}

	public String getHoraFin() {
		return horaFin;
	}

	public void setHoraFin(String horaFin) {
		this.horaFin = horaFin;
	}

	// toString
	@Override
	public String toString() {
		return "Turno [id=" + id + ", dia=" + dia + ", horaInicio=" + horaInicio + ", horaFin=" + horaFin + "]";
	}
}
