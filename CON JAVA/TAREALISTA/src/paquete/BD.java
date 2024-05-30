package paquete;

import java.io.File;
import java.io.FileNotFoundException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Scanner;


/**
 * @author Manuel
 * @version 1.0
 */

public class BD {
	// Variables propias de la clase
	private static BD miInstancia = null;
	private static boolean permitirInstanciaNueva;

	private Connection conn;
	private Statement stmt;
	private String cadenaConex; // driver@server:puerto:sid
	private String usuario;
	private String pass;

	// Constructor predefinido
	public BD() throws Exception {
		if (!permitirInstanciaNueva) {
			throw new Exception("No se puede crear otro obejto. Usa getIntance()");
		}
	}

	// Metodo para obtener la instancia
	public static BD getInstance() {
		if (miInstancia == null) {
			permitirInstanciaNueva = true;
			try {
				miInstancia = new BD();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			permitirInstanciaNueva = false;
		}
		return miInstancia;
	}

	// GETTERS Y SETTERS
	public Connection getConn() {
		return conn;
	}

	public void setConn(Connection conn) {
		this.conn = conn;
	}

	public Statement getStmt() {
		return stmt;
	}

	public void setStmt(Statement stmt) {
		this.stmt = stmt;
	}

	public String getCadenaConex() {
		return cadenaConex;
	}

	public void setCadenaConex(String cadenaConex) {
		this.cadenaConex = cadenaConex;
	}

	public String getUsuario() {
		return usuario;
	}

	public void setUsuario(String usuario) {
		this.usuario = usuario;
	}

	public String getPass() {
		return pass;
	}

	public void setPass(String pass) {
		this.pass = pass;
	}

	// Metodo para hacer una consulta en la base de datos
	public ResultSet consultaBD(String consulta) {
		ResultSet rset = null;
		try {
			this.conn = DriverManager.getConnection(this.cadenaConex, this.usuario, this.pass);
			this.stmt = conn.createStatement();
			rset = stmt.executeQuery(consulta);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return rset;
	}

	// Metodo para cerrar la consulta
	public void cerrarConsulta() {
		try {
			this.stmt.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	// Metodo para cargar la conexion
	public void cargarConexionXML(String fichero) {
		try {
			Scanner leer = new Scanner(new File(fichero));
			String puerto = "";
			while (leer.hasNext()) {
				String cadena = leer.nextLine();
				if (cadena.contains("CADENA")) {
					puerto = cadena.split(">")[1].split("<")[0];
				}
				if (cadena.contains("USUARIO")) {
					this.usuario = cadena.split(">")[1].split("<")[0];
				}
				if (cadena.contains("CLAVE")) {
					this.pass = cadena.split(">")[1].split("<")[0];
				}
			}
			this.setCadenaConex(puerto);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	// Método para crear una nueva tarea
	public void crearTarea(Tarea t) {
		int idtarea = 0, aux = 0;
		
		BD.getInstance().cargarConexionXML("tar.xml");
		ResultSet rest3 = BD.getInstance().consultaBD("SELECT MAX(IDEN) FROM TAREAS");
		try {
			if(rest3.next()) {
				idtarea = rest3.getInt(1);
				idtarea++;
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		BD.getInstance().cerrarConsulta();
		
		
		if(t.isCompletado() == true) {
			aux = 1;
		}else {
			aux = 0;
		}
		
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("INSERT INTO TAREAS VALUES("+idtarea+", '"+t.getTitulo()+"', '"+t.getDescripcion()+"', "+aux+")");
		BD.getInstance().cerrarConsulta();
		
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("COMMIT");
		BD.getInstance().cerrarConsulta();
	}
	
	// Método para obtener una tarea por el id
	public Tarea obtenerTarea(int id) {
		Tarea pedida = new Tarea();
		BD.getInstance().cargarConexionXML("tar.xml");
		ResultSet rest = BD.getInstance().consultaBD("SELECT * FROM TAREAS WHERE IDEN="+id);
		try {
			while(rest.next()) {
				pedida.setId(rest.getInt(1));
				pedida.setTitulo(rest.getString(2));
				pedida.setDescripcion(rest.getString(3));
				
				if (rest.getInt(4) == 1) {
					pedida.setCompletado(true);
				}else {
					pedida.setCompletado(false);
				}
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return pedida;
	}
	
	// Método para obtener todas las tareas
	public ArrayList<Tarea> todasLasTareas(){
		ArrayList<Tarea> tareas = new ArrayList<Tarea>();
		BD.getInstance().cargarConexionXML("tar.xml");
		ResultSet rest = BD.getInstance().consultaBD("SELECT * FROM TAREAS ORDER BY IDEN");
		try {
			while(rest.next()) {
				Tarea aux = new Tarea();
				aux.setId(rest.getInt(1));
				aux.setTitulo(rest.getString(2));
				aux.setDescripcion(rest.getString(3));
				
				if (rest.getInt(4) == 1) {
					aux.setCompletado(true);
				}else {
					aux.setCompletado(false);
				}
				
				tareas.add(aux);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return tareas;
	}
	
	// Método para actualizar una tarea
	public void actualizarTarea(int id, String nuevo) {
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("UPDATE TAREAS SET DESCRIPCION = '"+nuevo+"' WHERE IDEN="+id);
		BD.getInstance().cerrarConsulta();
		
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("COMMIT");
		BD.getInstance().cerrarConsulta();
	}
	
	// Método para realizar tarea
	public void realizarTarea(int id) {
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("UPDATE TAREAS SET REALIZADO = "+1+" WHERE IDEN="+id);
		BD.getInstance().cerrarConsulta();
		
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("COMMIT");
		BD.getInstance().cerrarConsulta();
	}
	
	// Método para eliminar una tarea por su id
	public void borrarTarea(int id) {
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("DELETE FROM TAREAS WHERE IDEN="+id);
		BD.getInstance().cerrarConsulta();
		
		BD.getInstance().cargarConexionXML("tar.xml");
		BD.getInstance().consultaBD("COMMIT");
		BD.getInstance().cerrarConsulta();
	}
}