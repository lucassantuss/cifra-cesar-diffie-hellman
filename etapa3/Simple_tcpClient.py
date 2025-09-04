from socket import *
import random

# ---------------- Cifra de César ----------------
def cifra_cesar_encrypt(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + chave) % 26 + base)
        else:
            resultado += char
    return resultado

def cifra_cesar_decrypt(texto, chave):
    return cifra_cesar_encrypt(texto, -chave)

# ---------------- Potência modular rápida ----------------
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

serverName = "10.1.70.33"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Cliente escolhe p e g
p = int(input("Digite um número primo p: "))
g = int(input("Digite um gerador g: "))

# chave privada de Alice
a = random.randint(3, p-2)
A = mod_exp(g, a, p)

# enviar p, g, A
clientSocket.send(f"{p},{g},{A}".encode())

# receber B
data = clientSocket.recv(65000).decode()
if data == "ERRO: p não é primo":
    print("Servidor rejeitou: p não é primo.")
    clientSocket.close()
    exit()

B = int(data)

# chave secreta
K = mod_exp(B, a, p)
print(f"Chave secreta (cliente): {K}")

sentence = input("Input lowercase sentence: ")

# Criptografar com chave K
encrypted = cifra_cesar_encrypt(sentence, K)
clientSocket.send(encrypted.encode())

# Receber resposta
modifiedSentence = clientSocket.recv(65000).decode()
decrypted = cifra_cesar_decrypt(modifiedSentence, K)

print("Received from Server (after decrypt): ", decrypted)
clientSocket.close()
