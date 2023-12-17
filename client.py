import socket
import threading

PORT = 5050 ## mude a porta se quiser
FORMATO = 'utf-8'
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_mensagens():
    while True:
        try:
            msg = client.recv(1024).decode(FORMATO)
            mensagem_splitada = msg.split("=")
            print(mensagem_splitada[1] + ": " + mensagem_splitada[2])
        except ConnectionAbortedError:
            print("Conexão encerrada pelo servidor.")
            break

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))

def enviar_mensagens_usuario():
    print("Bem-vindo ao chat! Digite 'exit' para sair.")
    enviar_nome()

    while True:
        mensagem = input("Digite sua mensagem ('exit' para sair): ")
        if mensagem.lower() == 'exit':
            print("Você saiu do chat.")
            break
        enviar("msg=" + mensagem)

def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=enviar_mensagens_usuario)
    thread1.start()
    thread2.start()

iniciar()
