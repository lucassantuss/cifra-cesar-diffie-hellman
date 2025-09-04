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

serverName = "10.1.70.33"  # IP do servidor
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase sentence: ")

# Criptografar antes de enviar
encrypted = cifra_cesar_encrypt(sentence)
clientSocket.send(bytes(encrypted, "utf-8"))

# Receber resposta criptografada
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence, "utf-8")

# Decriptar antes de mostrar
decrypted = cifra_cesar_decrypt(text)

print("Received from Server (after decrypt): ", decrypted)
clientSocket.close()
