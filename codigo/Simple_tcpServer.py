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

# ---------------- Verificador de Primo ----------------
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("TCP Server com Diffie-Hellman + Verificação de Primo\n")

connectionSocket, addr = serverSocket.accept()

# receber p, g, A
data = connectionSocket.recv(65000).decode()
p, g, A = map(int, data.split(","))

# validar se p é primo
if not is_prime(p):
    print(f"Cliente enviou p={p}, mas não é primo! Encerrando...")
    connectionSocket.send("ERRO: p não é primo".encode())
    connectionSocket.close()
    exit()

# chave privada de Bob
b = random.randint(3, p-2)
B = mod_exp(g, b, p)

# enviar B
connectionSocket.send(str(B).encode())

# chave secreta
K = mod_exp(A, b, p)
print(f"Chave secreta (servidor): {K}")

# receber mensagem criptografada
sentence = connectionSocket.recv(65000).decode()
decrypted = cifra_cesar_decrypt(sentence, K)
print("Received From Client (decrypted): ", decrypted)

# processar
capitalizedSentence = decrypted.upper()

# criptografar com chave K e enviar
encryptedToSend = cifra_cesar_encrypt(capitalizedSentence, K)
connectionSocket.send(encryptedToSend.encode())

print("Sent back to Client (encrypted): ", encryptedToSend)
connectionSocket.close()
