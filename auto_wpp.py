from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip, time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# Abre uma guia Chorme e inicia o Whatsapp
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)
navegador.get("https://web.whatsapp.com")

# ✅ Aguarda o WhatsApp carregar completamente
try:
    print("Aguardando login no WhatsApp Web...")
    WebDriverWait(navegador, 60).until(
        EC.presence_of_element_located((By.ID, "side"))  # Espera pelo painel lateral
    )
    print("Login detectado! Continuando a execução...")
except:
    print("Erro: Tempo limite excedido para login no WhatsApp Web.")
    navegador.quit()
    exit()

# Mensagem a ser Enviada
mensagem = "Escreva a Mensagem que deseja enviar"

# Todos os Contatos que Deseja enviar a mensagem
lista_contatos = ["Meu contato"] #Escreva seus contatos

# Enviar a mensagem para MEU NUMERO, para depois encaminhar

navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()# Clicar na lupa
navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys("Thiago (Eu)") # Escrever Meu Contato
navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.ENTER) # Dar um Enter
time.sleep(2) 

# Mandar mensagem para meu próprio chat
pyperclip.copy(mensagem)
navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL + "v") # Copia a mensagem e cola na barra de envio de mensagens
time.sleep(1)
navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER) # Aperta ENTER para enviar a mensagem

# Dividir a quantidade de contatos em blocos de 5 em 5
quantidade_contantos = len(lista_contatos)
if quantidade_contantos %5 == 0:
    quantidade_blocos = quantidade_contantos / 5
else:
    quantidade_blocos = int(quantidade_contantos / 5) + 1

 # Rodar o Codigo de encaminhar
for i in range(quantidade_blocos):
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar =lista_contatos[i_inicial:i_final]

    lista_elemento = navegador.find_elements('class name', '_amk4')
    for item in lista_elemento:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")
        if mensagem in texto:
            elemento = item

    # Selecionar a Mensagem para enviar
    ActionChains(navegador).move_to_element(elemento).perform()
    elemento.find_element('class name', '_ahkm').click()
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[5]/div').click() # Clickar no botão encaminhar
    navegador.find_element('xpath', '//*[@id="main"]/span[2]/div/button[2]/span').click() # Clickar na seta de encaminhar
    time.sleep(1)

    # Selecionar o cinco contatos para enviar
    for nome in lista_enviar: 
        # Escrever nome do contato
        navegador.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(nome)
        time.sleep(1)
        # Dar Enter
        navegador.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.ENTER)
        time.sleep(1)
        # Apagar nome do Contato
        navegador.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.BACK_SPACE)
        time.sleep(1)

# ENTER final para enviar as mensagens
navegador.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
time.sleep(3)
