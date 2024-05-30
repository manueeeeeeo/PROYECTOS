package paquete;

import java.util.ArrayList;
import java.util.Scanner;

public class App {
	// Variables propias de la clase
	private ArrayList<Tarea> tareas;
	
	// Constructor predfinido
	public App() {
		this.tareas = new ArrayList<Tarea>();
	}

	// Getters y Setters
	public ArrayList<Tarea> getTareas() {
		return tareas;
	}

	public void setTareas(ArrayList<Tarea> tareas) {
		this.tareas = tareas;
	}
	
	// Método principal
	public static void main(String[] args) {
		// Declaramos las variables
		Scanner sc = new Scanner(System.in);
		App app = new App();
		int op = 0;
		
		while(op!=7) {
			app.menu1();
			op = sc.nextInt();
			boolean resp2 = false;
			String rea = "";
			
			// Dependiendo de la opción hacemos una u otra cosa
			switch(op) {
			case 1: // Ver todas las tareas
				System.out.println("\nEstas son todas las tareas de su lista: ");
				app.verTareas();
				break;
			case 2: // Añadir una nueva tarea
				sc.nextLine();
				System.out.print("\nDigame el título de la tarea: ");
				String tit = sc.nextLine();
				System.out.print("Digame de que consta la tarea: ");
				String des = sc.nextLine();
				boolean var = false;
				while(resp2 == false) {
					System.out.print("¿Está hecha la tarea? S/n ");
					rea = sc.next();
					
					if(rea.equalsIgnoreCase("Si") || rea.equalsIgnoreCase("No")) {
						resp2 = true;
					}else {
						resp2 = false;
					}
					
					if(resp2==true && rea.equalsIgnoreCase("Si")) {
						var = true;
					}else if (resp2==true && rea.equalsIgnoreCase("Si")) {
						var = false;
					}
				}
				Tarea creada = new Tarea(0, tit.toUpperCase(), des, var);
				
				BD.getInstance().crearTarea(creada);
				System.out.println("\nCREANDO LA TAREA.....");
				System.out.println();
				break;
			case 3: // Ver toda la información de x tarea
				app.cargarTa();
				sc.nextLine();
				System.out.print("\nDigame el id de la tarea: ");
				Tarea t = new Tarea();
				int id = sc.nextInt();
				t = BD.getInstance().obtenerTarea(id);
				System.out.println("\nSu tarea:\nID: "+t.getId()+"\nTitulo: "+t.getTitulo()+"\nDescripción: "+t.getDescripcion());
				if(t.isCompletado()==true) {
					System.out.println("¿Completado? SI");
				}else {
					System.out.println("¿Completado? NO");
				}
				System.out.println();
				break;
			case 4: // Modificar una tarea
				app.cargarTa();
				sc.nextLine();
				System.out.print("\nDigame el id de la tarea: ");
				int i = sc.nextInt();
				sc.nextLine();
				System.out.print("Digame la nueva descripción: ");
				String desc = sc.nextLine();
				BD.getInstance().actualizarTarea(i, desc);
				System.out.println("\nTAREA MODIFICADA CORRECTAMENTE...");
				System.out.println();
				break;
			case 5: // Borrar una tarea
				app.cargarTa();
				sc.nextLine();
				System.out.print("\nDigame el ID de la tarea que desea borrar: ");
				int ide = sc.nextInt();
				BD.getInstance().borrarTarea(ide);
				break;
			case 6: // Realizar tarea
				app.cargarTa();
				sc.nextLine();
				System.out.print("\nDigame el id de la tarea: ");
				int ideintifi = sc.nextInt();
				System.out.println("\nMARCANDO ESA TAREA COMO HECHA.......\n");
				BD.getInstance().realizarTarea(ideintifi);
				System.out.println();
				break;
			case 7: // SALIR AUTOMATICAMENTE
				break;
			default: // Opción no posible
				System.out.println("\nLO SENTIMOS, ESA OPCIÓN NO ESTÁ DISPONIBLE\n");
				break;
			}
		}
		System.out.println("\nHASTA PRONTO AMIGO!");
	}

	// Método del menu principal
	public void menu1() {
		System.out.println("====================================================");
		System.out.println("===================LISTA DE TAREAS==================");
		System.out.println("====================================================\n");
		System.out.println("MENU\n");
		System.out.println("1º) Ver Mis Tareas");
		System.out.println("2º) Agregar Nueva Tarea");
		System.out.println("3º) Ver X Tarea");
		System.out.println("4º) Modificar Tarea");
		System.out.println("5º) Borrar Tarea");
		System.out.println("6º) Realizar Tarea");
		System.out.println("7º) Salir");
		System.out.print("Elige una opción: ");
	}
	
	// Método para cargar solo las tareas
	public void cargarTa() {
		this.setTareas(BD.getInstance().todasLasTareas());
	}
	
	// Método para ver todas las tareas
	public void verTareas() {
		// Cargar las tareas
		cargarTa();
		
		// Imprimir todos
		for (Tarea t : this.getTareas()) {
			String mensaje = "";
			if(t.isCompletado()==true) {
				mensaje = "Hecho";
			}else {
				mensaje = "No Hecho";
			}
			
			System.out.println(t.getId()+"\t"+t.getTitulo()+"\t"+mensaje);
		}
		
		// Hacemos el salto de línea
		System.out.println("\n");
	}
}