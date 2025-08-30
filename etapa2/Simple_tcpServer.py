from socket import *

# --- Funções de Criptografia ---
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# --- Configuração do Servidor ---
serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5)

print("TCP Server com Criptografia\n")
connectionSocket, addr = serverSocket.accept()

# --- Recebe e decripta ---
sentence = connectionSocket.recv(65000)
received = str(sentence, "utf-8")
decrypted = caesar_decrypt(received, 3)  # chave de 3 posições
print("Recebido (criptografado):", received)
print("Decriptado:", decrypted)

# --- Processa ---
capitalizedSentence = decrypted.upper()

# --- Criptografa e envia ---
encryptedResponse = caesar_encrypt(capitalizedSentence, 3)
connectionSocket.send(bytes(encryptedResponse, "utf-8"))

print("Enviado (decriptado):", capitalizedSentence)
print("Enviado (criptografado):", encryptedResponse)

connectionSocket.close()
