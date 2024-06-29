import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class RestaurantReservationSystem:
    def __init__(self, root):
        """Inicializa el sistema de reservas."""
        self.root = root
        self.root.title("Sistema de Reservas para un Restaurante")
        
        # Diccionario para almacenar el estado de las mesas (10 mesas inicialmente)
        self.tables = {f"Mesa {i}": None for i in range(1, 11)}

        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de usuario principal."""
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=20)

        tk.Label(self.table_frame, text="Seleccione una mesa:").grid(row=0, column=0, pady=10)

        self.table_var = tk.StringVar()
        self.table_var.set("Seleccione una mesa")
        self.table_menu = tk.OptionMenu(self.table_frame, self.table_var, *self.tables.keys())
        self.table_menu.grid(row=0, column=1)

        tk.Label(self.table_frame, text="Nombre:").grid(row=1, column=0, pady=10)
        self.name_entry = tk.Entry(self.table_frame)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.table_frame, text="Correo electrónico:").grid(row=2, column=0, pady=10)
        self.email_entry = tk.Entry(self.table_frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.table_frame, text="Hora de la reserva:").grid(row=3, column=0, pady=10)
        self.time_entry = tk.Entry(self.table_frame)
        self.time_entry.grid(row=3, column=1)

        self.reserve_button = tk.Button(self.table_frame, text="Reservar", command=self.make_reservation)
        self.reserve_button.grid(row=4, column=0, columnspan=2, pady=20)

        self.admin_button = tk.Button(self.table_frame, text="Panel de Administración", command=self.open_admin_panel)
        self.admin_button.grid(row=5, column=0, columnspan=2, pady=20)

    def make_reservation(self):
        """Realiza una reserva para la mesa seleccionada."""
        table = self.table_var.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        time = self.time_entry.get()

        if table not in self.tables:
            messagebox.showerror("Error", "Por favor, seleccione una mesa válida.")
            return

        if not name or not email or not time:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        if self.tables[table] is not None:
            messagebox.showerror("Error", "Esta mesa ya está reservada.")
            return

        self.tables[table] = {"name": name, "email": email, "time": time}
        self.send_confirmation_email(name, email, table, time)
        messagebox.showinfo("Reservado", f"Reserva confirmada para {table} a las {time}.")
        self.update_table_menu()

    def send_confirmation_email(self, name, email, table, time):
        """Envía un correo electrónico de confirmación de reserva."""
        sender_email = "tuemail@example.com"  # Reemplazar con tu correo electrónico
        sender_password = "tucontraseña"      # Reemplazar con tu contraseña

        subject = "Confirmación de Reserva"
        body = f"Hola {name},\n\nTu reserva para {table} a las {time} ha sido confirmada.\n\nGracias por reservar con nosotros."

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, email, text)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo enviar el correo de confirmación. Error: {str(e)}")

    def update_table_menu(self):
        """Actualiza el menú desplegable de las mesas."""
        self.table_menu['menu'].delete(0, 'end')
        for table in self.tables.keys():
            self.table_menu['menu'].add_command(label=table, command=tk._setit(self.table_var, table))

    def open_admin_panel(self):
        """Abre el panel de administración."""
        AdminPanel(self.root, self.tables)


class AdminPanel:
    def __init__(self, root, tables):
        """Inicializa el panel de administración."""
        self.root = root
        self.tables = tables
        self.admin_window = tk.Toplevel(root)
        self.admin_window.title("Panel de Administración")
        
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de usuario del panel de administración."""
        tk.Label(self.admin_window, text="Gestión de Disponibilidad de Mesas").pack(pady=10)
        
        self.table_listbox = tk.Listbox(self.admin_window)
        self.table_listbox.pack(pady=10)
        self.update_table_listbox()

        self.clear_button = tk.Button(self.admin_window, text="Liberar Mesa", command=self.clear_reservation)
        self.clear_button.pack(pady=10)

    def update_table_listbox(self):
        """Actualiza la lista de mesas y sus reservas en el panel de administración."""
        self.table_listbox.delete(0, tk.END)
        for table, reservation in self.tables.items():
            if reservation:
                self.table_listbox.insert(tk.END, f"{table}: {reservation['name']} at {reservation['time']}")
            else:
                self.table_listbox.insert(tk.END, f"{table}: Libre")

    def clear_reservation(self):
        """Libera la mesa seleccionada en el panel de administración."""
        selected = self.table_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Por favor, seleccione una mesa.")
            return
        
        table = self.table_listbox.get(selected[0]).split(":")[0]
        self.tables[table] = None
        self.update_table_listbox()
        messagebox.showinfo("Mesa Liberada", f"{table} ha sido liberada.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantReservationSystem(root)
    root.mainloop()
