from socket import *
import random

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

serverName = "10.1.70.33"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# --- Diffie-Hellman ---
# Recebe p, g, B do servidor
data = clientSocket.recv(65000).decode()
p, g, B = map(int, data.split(","))

a = random.randint(1, p-2)
A = mod_exp(g, a, p)

# Envia A para o servidor
clientSocket.send(str(A).encode())

# Calcula chave compartilhada
shared_key = mod_exp(B, a, p)
print("Chave compartilhada (Cliente):", shared_key)

# --- Comunicação criptografada ---
while True:
    sentence = input("Input lowercase sentence: ")
    if not sentence:
        break

    # Criptografa antes de enviar
    encrypted = "".join(chr((ord(c) - 97 + shared_key) % 26 + 97) if c.isalpha() else c for c in sentence)
    clientSocket.send(encrypted.encode())

    # Recebe resposta cifrada
    response = clientSocket.recv(65000).decode()
    print("Recebido (cifrado):", response)

    # Decripta resposta
    decrypted = "".join(chr((ord(c) - 65 - shared_key) % 26 + 65) if c.isalpha() else c for c in response)
    print("Recebido (decriptado):", decrypted)

clientSocket.close()
