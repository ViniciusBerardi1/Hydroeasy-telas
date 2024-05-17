import tkinter as tk
from tkinter import messagebox

# Função para login
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Bem vindo a Hidroeasy!")
        root_login.destroy()  # Fechar a tela de login após o login bem-sucedido
        criar_tela_menu()
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha incorretos")

# Função para criar a tela de login
def criar_tela_login():
    global root_login
    root_login = tk.Tk()
    root_login.title("Login")
    root_login.geometry("300x200")
    root_login.configure(bg="#3498db")

    frame_login = tk.Frame(root_login, bg="#3498db")
    frame_login.place(relx=0.5, rely=0.5, anchor="center")

    label_usuario = tk.Label(frame_login, text="Usuário:", bg="#3498db", fg="white", font=("Arial", 10, "bold"))
    label_usuario.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    label_senha = tk.Label(frame_login, text="Senha:", bg="#3498db", fg="white", font=("Arial", 10, "bold"))
    label_senha.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    global entry_usuario
    entry_usuario = tk.Entry(frame_login)
    entry_usuario.grid(row=0, column=1, padx=5, pady=5)

    global entry_senha
    entry_senha = tk.Entry(frame_login, show="*")
    entry_senha.grid(row=1, column=1, padx=5, pady=5)

    button_login = tk.Button(frame_login, text="Login", command=login)
    button_login.grid(row=2, columnspan=2, padx=5, pady=5)

    root_login.mainloop()

# Função para criar a tela de menu
def criar_tela_menu():
    menu = tk.Tk()
    menu.title("Menu")
    menu.geometry("600x450")
    menu.configure(bg="#3498db")  # Cor de fundo azul

    label_title = tk.Label(menu, text="Hidroeasy", font=("Arial", 16, "bold"), bg="#3498db", fg="white")
    label_title.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

    criar_botao_planta(menu, "Alface", "13:30", "18:15", "70%", 1)
    criar_botao_planta(menu, "Tomate", "15:20", "Sem agendamentos", "90%", 2)
    criar_botao_planta(menu, "Cebolinha", "09:00", "15:30", "20%", 3)

    button_agendamento = tk.Button(menu, text="Agendamento", width=15, command=abrir_agendamento)
    button_agendamento.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    menu.mainloop()

# Função para criar botões de planta
def criar_botao_planta(menu, planta, ultima_rega, prox_agendamento, umidade, linha):
    button = tk.Button(menu, text=planta, width=10, command=lambda: informacao_planta(planta))
    button.grid(row=linha, column=0, padx=10, pady=10, sticky="e")

    frame_plantacao = tk.Frame(menu, bg="white", bd=2, relief=tk.GROOVE)
    frame_plantacao.grid(row=linha, column=1, padx=10, pady=10, sticky="ew")

    label_info = tk.Label(frame_plantacao, text=f"Plantação de {planta}\nRegado pela última vez: {ultima_rega}\nPróximo agendamento: {prox_agendamento}\nHumidade: {umidade}", bg="white")
    label_info.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    button_sensor = tk.Button(menu, text="Sensores", width=15, command=lambda: mapa_sensores(planta))
    button_sensor.grid(row=linha, column=2, padx=10, pady=10, sticky="w")

# Função para exibir informações da planta
def informacao_planta(planta):
    info = {
        "Alface": "Historioco da plantação Alface: \n- Umidade 70% \n- Proximo agendamento: 18:15 \n- Ultima vez regada 15/03/2024 as 13:30",
        "Tomate": "Historioco da plantação Tomate: \n- Umidade 90% \n- Proximo agendamento: Sem agendamentos \n- Ultima vez regada 15/03/2024 as 16:00",
        "Cebolinha": "Historioco da plantação Cebolinha: \n- Umidade 20% \n- Proximo agendamento: 15:30 \n- Ultima vez regada hoje as 15:00"
    }
    messagebox.showinfo(planta, info[planta])

# Função para abrir a janela de agendamento
def abrir_agendamento():
    agendamento_window = tk.Toplevel()
    agendamento_window.title("Agendamento de Irrigação")
    agendamento_window.geometry("300x230")
    agendamento_window.configure(bg="#3498db")

    label_agendamento = tk.Label(agendamento_window, text="Agendar irrigação:", bg="#3498db", fg="white", font=("Arial", 10, "bold"))
    label_agendamento.pack(pady=10)

    label_horario = tk.Label(agendamento_window, text="Horário (HH:MM):", bg="#3498db", fg="white", font=("Arial", 10, "bold"))
    label_horario.pack(pady=5)

    frame_time = tk.Frame(agendamento_window, bg="#3498db")
    frame_time.pack(pady=5)

    entry_horas = tk.Entry(frame_time, width=5)
    entry_horas.pack(side="left")

    label_colon = tk.Label(frame_time, text=":", bg="#3498db", fg="white", font=("Arial", 10, "bold"))
    label_colon.pack(side="left")

    entry_minutos = tk.Entry(frame_time, width=5)
    entry_minutos.pack(side="left")

    label_planta = tk.Label(agendamento_window, text="Planta:", bg="#3498db", fg="white", font=("Arial", 10, "bold"))
    label_planta.pack(pady=5)

    option_planta = tk.StringVar(agendamento_window)
    option_planta.set("Alface")
    drop_planta = tk.OptionMenu(agendamento_window, option_planta, "Alface", "Tomate", "Cebolinha")
    drop_planta.pack(pady=5)

    button_agendar = tk.Button(agendamento_window, text="Agendar", command=lambda: verificar_horario(option_planta.get(), entry_horas.get(), entry_minutos.get(), agendamento_window))
    button_agendar.pack(pady=5)

# Função para verificar o horário de agendamento
def verificar_horario(planta, horas, minutos, agendamento_window):
    horario = f"{horas}:{minutos}"
    if horas.isdigit() and minutos.isdigit() and 0 <= int(horas) < 24 and 0 <= int(minutos) < 60:
        if not horario_em_intervalo_proibido(horario):
            messagebox.showinfo("Agendamento", f"Irrigação para {planta} agendada para as {horario}!")
            agendamento_window.destroy()
        else:
            messagebox.showerror("Erro de Agendamento", "A irrigação não pode ser agendada para o horário especificado.")
    else:
        messagebox.showerror("Erro de Agendamento", "Por favor, insira um horário válido para agendar a irrigação.")

# Função para verificar se o horário está no intervalo proibido
def horario_em_intervalo_proibido(horario):
    return 10 <= int(horario.split(":")[0]) < 16

# Função para exibir o mapa de sensores
def mapa_sensores(planta):
    sensores_window = tk.Toplevel()
    sensores_window.title("Mapa de Sensores")
    sensores_window.geometry("400x300")
    sensores_window.configure(bg="#3498db")

    label_title = tk.Label(sensores_window, text="Mapa de Sensores", font=("Arial", 14, "bold"), bg="#3498db", fg="white")
    label_title.pack(pady=10)

    for sensor in ["Alface", "Tomate", "Cebolinha"]:
        frame_sensor = tk.Frame(sensores_window, bg="white", bd=2, relief=tk.GROOVE)
        frame_sensor.pack(pady=10, padx=10, fill="x")

        label_sensor = tk.Label(frame_sensor, text=f"Sensor de {sensor}", bg="white", font=("Arial", 10, "bold"))
        label_sensor.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        button_on = tk.Button(frame_sensor, text="On", width=5)
        button_on.grid(row=0, column=1, padx=5, pady=5)

        button_off = tk.Button(frame_sensor, text="Off", width=5)
        button_off.grid(row=0, column=2, padx=5, pady=5)

# Chama a função para criar a tela de login
criar_tela_login()






