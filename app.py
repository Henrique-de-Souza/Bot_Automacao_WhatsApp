# Envio de mensagens automática para grupos de whatsapp
# tecnologias usadas: selenium, piperclip, webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains
import pyperclip
import time

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")

# Esperar até 100 segundos para encontrar o elemento do código QR
qr_code_element = WebDriverWait(nav, 100).until(
    EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']"))
    )

# Se o elemento do código QR for encontrado, esperar 30 segundos para o usuário fazer o login
print("Código QR encontrado e escaneado. Aguardando a página carregar completamente...")
# tempo para logar:
time.sleep(20)
print('espera concluída, pronto para iniciar a automação')

mensagem = '''Olá, essa mensagem e uma desmontração, 
do poder da automação com programação'''

# lista de contatos 
lista_contados = ['EU Pessoal', 'Henrique B.', 'massoterapia', 'Sammy', 'Bruno Bezerra']

# 1º passo - enviar a mensagem para mim mesmo:
# clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
print('click na lupa ..... ok')

# escrever o nome do meu próprio contato
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("Eu Pessoal")
print('Contato encontrado......ok')

# apertar enter
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
print('enter......ok')
time.sleep(5)

# clicar no campo da mensagem
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').click()
print('campo de mensagem encontrado..........ok')

# escrever a mensagem
time.sleep(2)
pyperclip.copy(mensagem)
# colando a mensagem no campo correspondente
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
print('enviando mensagem.....ok')

nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
print('mensagem enviada.......ok')
time.sleep(5)


# 2º passo - encaminhar a mensagem para os grupos
lista_elemento = nav.find_elements('class name', '_2AOIt')

# definindo a quantidade de blocos que encaminhará as mensagens
qtd_contados = len(lista_contados)

if qtd_contados % 5 == 0:
    qtd_blocos = int(qtd_contados / 5)
else:
    qtd_blocos = int(qtd_contados / 5) + 1

for i in range(int(qtd_blocos)):
    
    # rodar o codigo de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5 

    lista_enviar = lista_contados[i_inicial: i_final]

    # selecionar a mensagem para enviar e abrir a caixa de encaminhar
    for item in lista_elemento:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")
        if mensagem in texto:
            elemento = item
            break


    # Selecionar a mensagem para enviar
    ActionChains(nav).move_to_element(elemento).perform()
    # procurar seta que abre a caixa de opções de eventos
    elemento.find_element('class name', '_3u9t-').click()
    print('seta encontrada com sucesso.........ok')
    time.sleep(3)

    # clicar em encaminhar
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    print('botão de encaminhar encontrado..........ok')
    time.sleep(1)
    
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    print('encaminhando................ok')
    time.sleep(3)

    for nome in lista_enviar:
        # selecionar os 5 contatos para enviar
        # escrever o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(1)
        
        # apertar enter
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(1)
        
        # apagar para ir para o proximo
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(5)

input('Para fechar a janela e reiniciar o processo, aprte ENTER ')

nav.quit()
