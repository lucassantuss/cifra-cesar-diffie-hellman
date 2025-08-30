# \# Projeto de Comunicação Cliente-Servidor TCP com Criptografia

# 

# Este projeto foi desenvolvido como parte da disciplina \*\*Tópicos Avançados de Redes\*\* (10º semestre de Engenharia da Computação).  

# O objetivo é implementar a comunicação entre Cliente e Servidor via \*\*TCP em Python\*\*, evoluindo em três etapas:

# 

# 1\. \*\*Etapa 1\*\* – Comunicação simples entre Cliente e Servidor TCP.  

# 2\. \*\*Etapa 2\*\* – Adição de criptografia simétrica com \*\*Cifra de César\*\*.  

# 3\. \*\*Etapa 3\*\* – Implementação de troca de chaves simétricas via \*\*Diffie-Hellman\*\*, utilizada na cifra.

# 

# ---

# 

# \## 🚀 Estrutura do Projeto

# 

# \- `SimpleTCPServer.py` → Código do Servidor TCP.  

# \- `SimpleTCPClient.py` → Código do Cliente TCP.  

# \- `README.md` → Documentação e análise do projeto.  

# 

# ---

# 

# \## 📌 Etapa 1 – Comunicação TCP

# 

# O \*\*Servidor\*\* abre um socket TCP na porta `1300` e aguarda conexões.  

# O \*\*Cliente\*\* se conecta ao servidor, envia uma frase e recebe a mesma frase convertida para \*\*maiúsculo\*\*.

# 

# \### Fluxo básico:

# 1\. Cliente envia: `"hello"`.  

# 2\. Servidor recebe `"hello"`, processa e envia `"HELLO"`.  

# 3\. Cliente recebe e imprime `"HELLO"`.

# 

# ---

# 

# \## 🔐 Etapa 2 – Cifra de César

# 

# Foi implementada a criptografia com \*\*Cifra de César\*\*, utilizando uma chave de deslocamento (inicialmente fixa em `3`).

# 

# \- \*\*Cliente\*\*: cifra a mensagem antes de enviar.  

# \- \*\*Servidor\*\*: recebe a mensagem, decifra, processa (maiúsculo), cifra a resposta e envia de volta.  

# \- \*\*Cliente\*\*: recebe a resposta cifrada e decifra para exibir.

# 

# Exemplo:  

# 

# \- Cliente digita: `hello`  

# \- Cliente envia (cifrado): `khoor`  

# \- Servidor responde (cifrado): `KHOOR`  

# \- Cliente decifra e exibe: `HELLO`  

# 

# ---

# 

# \## 🔑 Etapa 3 – Diffie-Hellman

# 

# Para não depender de uma chave fixa, foi implementado o \*\*algoritmo Diffie-Hellman\*\* de troca de chaves.  

# 

# \### Funcionamento:

# 1\. Cliente e Servidor acordam sobre dois valores públicos:  

# &nbsp;  - Um número primo `p`.  

# &nbsp;  - Uma base `g`.  

# 

# 2\. Cada lado escolhe uma \*\*chave privada secreta\*\*:  

# &nbsp;  - Cliente: `a`  

# &nbsp;  - Servidor: `b`.  

# 

# 3\. Cada lado calcula uma \*\*chave pública\*\*:  

# &nbsp;  - Cliente envia `A = g^a mod p`.  

# &nbsp;  - Servidor envia `B = g^b mod p`.  

# 

# 4\. Ambos calculam a \*\*chave secreta compartilhada\*\*:  

# &nbsp;  - Cliente: `K = B^a mod p`.  

# &nbsp;  - Servidor: `K = A^b mod p`.  

# 

# Essa chave `K` é usada como \*\*deslocamento da Cifra de César\*\*.  

# 👉 Ela nunca trafega na rede, apenas os valores intermediários (`A`, `B`, `p`, `g`) são transmitidos.

# 

# ---

# 

# \## 📂 Análise do Código

# 

# \### 🔸 Servidor (`SimpleTCPServer.py`)

# \- Cria o socket e escuta na porta `1300`.  

# \- Executa a fase de troca Diffie-Hellman (`p`, `g`, `A`, `B`).  

# \- Calcula a \*\*chave compartilhada\*\* `shared\_key`.  

# \- Para cada mensagem recebida:  

# &nbsp; - Decifra a mensagem usando `shared\_key`.  

# &nbsp; - Converte para maiúsculo.  

# &nbsp; - Cifra novamente com `shared\_key` e envia a resposta.  

# 

# \### 🔸 Cliente (`SimpleTCPClient.py`)

# \- Cria o socket e conecta ao servidor.  

# \- Recebe os valores públicos `p`, `g` e a chave pública do servidor `B`.  

# \- Gera sua chave privada `a`, calcula `A = g^a mod p` e envia ao servidor.  

# \- Calcula a \*\*chave compartilhada\*\* `shared\_key`.  

# \- Para cada mensagem digitada pelo usuário:  

# &nbsp; - Cifra a mensagem com `shared\_key`.  

# &nbsp; - Envia ao servidor.  

# &nbsp; - Recebe a resposta cifrada.  

# &nbsp; - Decifra e exibe no console.  

# 

# ---

# 

# \## 🧪 Testando o Projeto

# 

# 1\. Inicie o servidor:  

# &nbsp;  ```bash

# &nbsp;  python SimpleTCPServer.py



