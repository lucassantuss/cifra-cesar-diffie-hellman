# 🔒 Comunicação Cliente-Servidor TCP com Criptografia (Diffie-Hellman + Cifra de César)

Este projeto implementa uma comunicação **Cliente-Servidor TCP** utilizando:
- **Troca de chaves Diffie-Hellman** para geração de uma chave secreta compartilhada entre cliente e servidor.  
- **Cifra de César** para criptografia e descriptografia de mensagens trocadas.  
- **Verificação de primalidade** no servidor, garantindo que o número primo `p` fornecido pelo cliente seja válido para o protocolo.

---

## 👥 Integrantes do Grupo

- **João Antônio de Brito Moraes** – RA: 081210028
- **Lucas Araujo dos Santos** – RA: 081210009  
- **Natthalie Bohm** – RA: 081210001  
- **Renan Cesar de Araujo** – RA: 081210033

---

## 🚀 Funcionalidades

- **Cliente**
  - Define um número primo `p` e um gerador `g`.
  - Gera sua chave privada `a` e calcula a chave pública `A`.
  - Envia `(p, g, A)` ao servidor.
  - Recebe a chave pública `B` do servidor e calcula a chave secreta compartilhada `K`.
  - Criptografa a mensagem utilizando a cifra de César com deslocamento `K` e envia ao servidor.
  - Recebe a resposta criptografada do servidor e a decriptografa.

- **Servidor**
  - Recebe `(p, g, A)` do cliente.
  - Valida se `p` é primo (caso contrário, encerra a conexão).
  - Gera sua chave privada `b` e calcula a chave pública `B`.
  - Envia `B` ao cliente.
  - Calcula a chave secreta compartilhada `K`.
  - Recebe a mensagem criptografada, decripta com `K`, processa (transformando em maiúsculas) e reenvia a mensagem criptografada novamente.

---

## 📂 Estrutura do Projeto

- `Simple_tcpServer.py` → Código do Servidor TCP.  
- `Simple_tcpClient.py` → Código do Cliente TCP.  
- `README.md` → Documentação e análise do projeto.

---

## ⚙️ Execução

### 1. Inicie o servidor
```bash
python Simple_tcpServer.py
```

### 2. Em outro terminal/máquina, inicie o cliente
```bash
python Simple_tcpClient.py
```
