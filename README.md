
🪟🤖 Automação de Cortina com LDR + Controle Manual via Python

Este projeto implementa um sistema automatizado de abertura/fechamento de cortina, utilizando um sensor LDR (Light Dependent Resistor) para detectar luminosidade e um servo motor para movimentação mecânica.
Além disso, o sistema conta com uma interface gráfica (GUI) em Python, permitindo controlar a cortina manualmente sempre que desejado.

🌞 Objetivo do Projeto

Automatizar uma cortina de forma que:

Abra automaticamente quando houver luz suficiente.

Feche automaticamente em ambientes escuros.

Permita controle manual através de um painel criado em Tkinter.

Faça comunicação entre Arduino ⇆ Python via porta serial.

🧩 Como o Sistema Funciona

O projeto possui duas partes principais:

1️⃣ Arduino – Leitura do LDR e Movimentação do Servo
📌 Arquivo: código Arduino
#include <Servo.h>

Servo myservo; 

void setup(){
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() {
  int LDR = analogRead(A0);
  Serial.println(LDR);

  if (LDR > 300)
    myservo.write(180);
  else 
    myservo.write(0);
    
  delay(200);
}

📝 Explicação:

O Arduino lê continuamente o valor do LDR conectado ao pino A0.

Envia esse valor pela porta serial para o Python.

O valor do LDR é usado como critério para acionar o servo:

LDR > 300 → muita luz → abre a cortina (180°)

LDR ≤ 300 → pouca luz → fecha a cortina (0°)

Esse é o modo automático padrão.

2️⃣ Interface Python – Controle Automático e Manual 🖥️🐍
📌 Arquivo: interface Python Tkinter

Essa interface permite:

🔄 Modo Automático

O Python apenas lê os valores enviados pelo Arduino.

Mostra o valor do LDR na tela.

O Arduino controla o servo sozinho.

🤝 Modo Manual

O usuário pode clicar em:

Abrir

Fechar

📡 Thread paralela

O Python cria uma thread para ler os valores da serial constantemente, sem travar a interface gráfica.

🖼️ Resumo visual do fluxo:
Arduino ---> envia LDR ----> Python (mostra na tela)
Arduino <--- recebe comando <--- Python (manual/auto)

🛠 Como Executar
✔ Requisitos

Arduino UNO ou similar

Sensor LDR (com resistor de pull-down)

Servo motor

Cabo USB

Python 3

Bibliotecas Python:

pip install pyserial

▶ Passo a Passo
1️⃣ Carregar o código no Arduino

Use a IDE Arduino e faça upload do código.

2️⃣ Verifique a porta serial

Atualize no Python:

PORTA = "COM3"


(Usar a porta correta do seu PC)

3️⃣ Execute o Python
python interface.py


A interface irá abrir e você pode:

📟 Ver o valor do LDR em tempo real

🔄 Alternar entre Automático e Manual

🕹 Controlar o servo manualmente

⚙ Como o Servo Controla a Cortina

O servo pode ser acoplado:

A uma haste

A um rolete

A uma estrutura impressa em 3D

O movimento 0° ↔ 180° pode representar:

Abrir totalmente

Fechar totalmente

🎉 Conclusão

Este projeto demonstra como integrar:

Sensoriamento (LDR)

Atuação (servo motor)

Automação inteligente

Interface de controle próprio (Tkinter)

Um ótimo exemplo de IoT simples e eficiente, unindo hardware e software! 🚀