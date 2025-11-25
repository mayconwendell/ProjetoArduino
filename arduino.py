import tkinter as tk
from tkinter import ttk
import serial
import threading
import time

# ============================
# Configuração da Porta Serial
# ============================

PORTA = "COM3"  
BAUD = 9600

try:
    arduino = serial.Serial(PORTA, BAUD, timeout=1)
except:
    arduino = None
    print("⚠ Erro ao conectar ao Arduino!")

# ============================
# Função: Ler dados do Arduino
# ============================

def ler_serial():
    while True:
        if arduino and modo.get() == "AUTO":
            try:
                linha = arduino.readline().decode().strip()
                if linha.isdigit():
                    valor_ldr.set(linha)  # Atualiza na interface
            except:
                pass
        time.sleep(0.1)

# ============================
# Funções de controle
# ============================

def set_automatico():
    if arduino:
        arduino.write(b"AUTO\n")

def set_manual():
    if arduino:
        arduino.write(b"MANUAL\n")

def abrir():
    if arduino:
        arduino.write(b"OPEN\n")

def fechar():
    if arduino:
        arduino.write(b"CLOSE\n")

# ============================
# Criação da Interface Tkinter
# ============================

root = tk.Tk()
root.title("Controle Arduino - Automático/Manual")
root.geometry("300x300")

modo = tk.StringVar(value="AUTO")
valor_ldr = tk.StringVar(value="---")

# ===== Rótulo LDR =====
ttk.Label(root, text="Valor LDR:", font=("Arial", 14)).pack(pady=5)
ttk.Label(root, textvariable=valor_ldr, font=("Arial", 18)).pack()

# ===== Seleção de Modo =====
ttk.Label(root, text="Modo de Operação:", font=("Arial", 12)).pack(pady=10)

ttk.Radiobutton(root, text="Automático", variable=modo, value="AUTO",
                command=set_automatico).pack()
ttk.Radiobutton(root, text="Manual", variable=modo, value="MANUAL",
                command=set_manual).pack()

# ===== Botões Manual =====
frame = ttk.Frame(root)
frame.pack(pady=20)

btn_abrir = ttk.Button(frame, text="Abrir", width=12, command=abrir)
btn_abrir.grid(row=0, column=0, padx=5)

btn_fechar = ttk.Button(frame, text="Fechar", width=12, command=fechar)
btn_fechar.grid(row=0, column=1, padx=5)

# ============================
# Thread para ler serial
# ============================

thread = threading.Thread(target=ler_serial, daemon=True)
thread.start()

# ============================
# Iniciar interface
# ============================
root.mainloop()
