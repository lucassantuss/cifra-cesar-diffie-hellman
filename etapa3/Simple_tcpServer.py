from socket import *
import random

# Potência modular rápida
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# --- Configuração do Servidor ---
serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
print("Servidor aguardando conexão...\n")

connectionSocket, addr = serverSocket.accept()

# --- Diffie-Hellman ---
p = 23
g = 5
b = random.randint(1, p-2)
B = mod_exp(g, b, p)

# Envia p, g e B para o cliente
connectionSocket.send(f"{p},{g},{B}".encode())

# Recebe A do cliente
A = int(connectionSocket.recv(65000).decode())

# Calcula chave compartilhada
shared_key = mod_exp(A, b, p)
print("Chave compartilhada (Servidor):", shared_key)

# --- Comunicação criptografada ---
while True:
    sentence = connectionSocket.recv(65000).decode()
    if not sentence:
        break
    print("Recebido (cifrado):", sentence)

    # Decripta com chave compartilhada
    decrypted = "".join(chr((ord(c) - 97 - shared_key) % 26 + 97) if c.isalpha() else c for c in sentence)
    print("Decriptado:", decrypted)

    # Processa (maiúsculo)
    capitalized = decrypted.upper()

    # Criptografa para resposta
    encrypted = "".join(chr((ord(c) - 65 + shared_key) % 26 + 65) if c.isalpha() else c for c in capitalized)
    connectionSocket.send(encrypted.encode())
    print("Enviado (cifrado):", encrypted)

connectionSocket.close()
