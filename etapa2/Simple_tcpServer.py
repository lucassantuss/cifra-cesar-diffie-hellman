from socket import *

def cifra_cesar_encrypt(texto, chave=3):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + chave) % 26 + base)
        else:
            resultado += char
    return resultado

def cifra_cesar_decrypt(texto, chave=3):
    return cifra_cesar_encrypt(texto, -chave)

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("TCP Server com Cifra de César\n")

connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(65000)

# Converter para string
received = str(sentence, "utf-8")

# Decriptar o que veio
decrypted = cifra_cesar_decrypt(received)
print("Received From Client (decrypted): ", decrypted)

# Processar (ex: colocar em maiúsculo)
capitalizedSentence = decrypted.upper()

# Criptografar antes de mandar de volta
encryptedToSend = cifra_cesar_encrypt(capitalizedSentence)
connectionSocket.send(bytes(encryptedToSend, "utf-8"))

print("Sent back to Client (encrypted): ", encryptedToSend)
connectionSocket.close()
