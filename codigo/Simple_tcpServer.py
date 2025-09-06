from socket import *
import random
import time

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

# ---------------- Validação de Primo com tempo ----------------
def valida_primo_com_tempo(N):
    start_time = time.time()

    i = 2
    while i < N:
        R = N % i
        if R == 0:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{N} não é primo! (tempo: {execution_time:.6f} segundos)")
            return False, execution_time
        i += 1
    else:
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{N} é primo! (tempo: {execution_time:.6f} segundos)")
        return True, execution_time

# ---------------- Servidor ----------------
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("TCP Server com Diffie-Hellman + Verificação de Primo\n")

connectionSocket, addr = serverSocket.accept()

# receber p, g, A
data = connectionSocket.recv(65000).decode()
p, g, A = map(int, data.split(","))

# validar se p é primo e medir tempo
eh_primo, tempo = valida_primo_com_tempo(p)
if not eh_primo:
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
