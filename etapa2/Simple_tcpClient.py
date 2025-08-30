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

# --- Configuração do Cliente ---
serverName = "10.1.70.33"   # IP do servidor
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# --- Input e criptografia ---
sentence = input("Input lowercase sentence: ")
encrypted = caesar_encrypt(sentence, 3)
clientSocket.send(bytes(encrypted, "utf-8"))

# --- Recebe e decripta ---
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence, "utf-8")
decrypted = caesar_decrypt(text, 3)

print("Received from Server (criptografado):", text)
print("Received from Server (decriptado):", decrypted)

clientSocket.close()
