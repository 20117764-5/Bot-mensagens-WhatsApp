# 🚀 Automação de Envio de Mensagens no WhatsApp Web com Selenium

Este projeto tem como objetivo automatizar o envio de mensagens no WhatsApp Web, utilizando **Python**, **Selenium** e **Pyperclip**. É uma solução simples e eficaz para quem deseja enviar mensagens para múltiplos contatos de forma automatizada.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para o desenvolvimento do script.
- **Selenium**: Ferramenta para automação de navegadores, permitindo interação com o WhatsApp Web.
- **WebDriver Manager**: Para gerenciar o WebDriver do Chrome automaticamente.
- **Pyperclip**: Para copiar e colar mensagens de maneira prática.
  
## ⚙️ Instalação e Configuração

Antes de começar a usar o script, é necessário instalar as dependências do projeto. Basta executar o comando abaixo no seu terminal:

```bash
pip install selenium pyperclip webdriver-manager
```

🎯 **Funcionalidade do Programa**

O script automatiza o processo de envio de mensagens no WhatsApp Web de forma eficiente. Ele segue este fluxo:

1. **Abertura do WhatsApp Web**:  
   O navegador é aberto automaticamente e o WhatsApp Web é carregado.

2. **Aguarda Login**:  
   O script espera até que você faça login no WhatsApp Web.

3. **Envio de Mensagem para Você Mesmo**:  
   O script envia uma mensagem de teste para o seu próprio número, para garantir que a automação está funcionando corretamente.

4. **Encaminhamento da Mensagem**:  
   A mensagem é encaminhada para uma lista de contatos pré-definidos, em blocos de 5 contatos por vez.
