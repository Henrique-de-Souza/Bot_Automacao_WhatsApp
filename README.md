# Bot_Automacao_WhatsApp 🦾🤖
Desenvolvi utilizando Selenium, WerDriver e Pyperclip, uma automação de envio de mensagens para grupos de WhatsApp, que pode ser facilmente modificado para outras plataformas de chat! 

# Por que? 🤔❔

Venho procurando me especializar em algo dentro da programação e automação de processos é algo que me cativa, 
embora eu ame o desenvolvimento web também.

# Como funciona? 🤔❔

Ao rodar o código, seremos redirecionado para a página web: https://web.whatsapp.com/
onde, nosso usuário deverá fazer o login com o qr code

![image](https://github.com/Henrique-de-Souza/Bot_Automacao_WhatsApp/assets/148600312/95b609d3-dc3b-4859-b077-ee5d540aa619)

Para ficar mais dinânico, integrei a capacidade do usuário receber feedbacks do andamento da automação no terminal,
conforme os processos vão seguindo:

```ruby

# Esperar até 100 segundos para encontrar o elemento do código QR
qr_code_element = WebDriverWait(nav, 100).until(
    EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']"))
    )

# Se o elemento do código QR for encontrado, esperar 30 segundos para o usuário fazer o login
print("Código QR encontrado e escaneado. Aguardando a página carregar completamente...")
# tempo para logar:
time.sleep(20)
print('espera concluída, pronto para iniciar a automação')

```
Como podemos ver, nosso usuário recebe uma mensagem, dizendo que o código encontrou um QR Codde, e agora ele terá 
30 segundos para pegar o celular, abrir o leitor e escaná-lo.

Conforme os eventos vão acontecendo, os feedbacks continuam como por exemplo, quando a autiomação clicar na lupinha de pesquisa, no terminal é printado:

  - Click na lupa de pesquisa......ok
    
ou quando o robo começa a escrever o nome do contato e clica em enviar:

  - Escrevendo nome do contato.....ok
    
e assim por diante....

-----------------------------------------------------------------------------------------------
# Passos da automação 🔄👣

Agora que estamos dentro do WhatsApp Web, o sistema seguirá uma cadeia de eventos:

Sequência dos eventos: 

#### 1º passo: Localizar a lupa de pesquisa de contatos. 🔍📑
    
  ![image](https://github.com/Henrique-de-Souza/Bot_Automacao_WhatsApp/assets/148600312/f408794c-0f64-41b6-9be5-ec3774783a12)

#### 2º passo: Escrever o nome do próprio contato e apertar ENTER 💻

  ![image](https://github.com/Henrique-de-Souza/Bot_Automacao_WhatsApp/assets/148600312/9e4dfad1-e2ef-48e1-99a1-e7db7be714bd)

#### 3º e 4º passo: localizar o campo de inserção da mensagem , colar a mensagem pré definida e enviar 🖱️

 ```ruby

mensagem = '''Olá, essa mensagem e uma desmontração, 
do poder da automação com programação'''

```

![image](https://github.com/Henrique-de-Souza/Bot_Automacao_WhatsApp/assets/148600312/d8b40720-2fe7-4be0-a4db-8c966c4adb4e)


  ![image](https://github.com/Henrique-de-Souza/Bot_Automacao_WhatsApp/assets/148600312/1419a69b-739c-4952-b24d-554d840b3285)

    
#### 5º e 6º passo: Localizar a setinha responsável por abrir a caixa de opçções de eventos e clicar em encaminhar 🖱️📤
    
  ![image](https://github.com/Henrique-de-Souza/Bot_Automacao_WhatsApp/assets/148600312/db3a54fb-9d39-4a45-bb22-cf5dca6fdc4d)
  

  ![image](https://github.com/Henrique-de-Souza/Bot_Automacao_WhatsApp/assets/148600312/29a34dae-d476-40f5-b84f-0be728c94aae)

#  Sobre Segurança 👮🔒🛡️⚔️

Agora entramos numa lógica de segurança para o usuário; Pois sabemos que o aplicativo só permite que encaminhamos mensagens para cada 5 grupos de uma vez, então, se tivermos uma lista com 250 contatos, o sistema vai de 5 em 5, até não restar mais nenhum contato.

Lógica abaixo:

```ruby
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

```
Com isso chegamos na última etapa dos eventos da automação:

#### 7º passo: Escrever o nome dos cinco primeiros contatos, enviar a mensagem e repetir o processo, até ao fim da lista de contatos.


------------------------------------------------------------------------
# Fim da automação 🔚🔚
----------------------------------------------------------------------------
sugestões para mim mesmo: 💡💡💡

  - Importar o pyautogui e adicionar ao fim da automação uma caixa de alerta, avisando que a automação chegou ao fim.
    Assim, o usuário poderá reiniciar a automação com a certeza de que a mensagem foi enviada para todos os grupos.

  - Acrescentar um tratamento de erro, caso algum contato da lista, não tenha recebido, ou não foi encontrado, e salvar o nome
    desse contato em um arquivo.txt, para encaminhar a mensagem manualmente, ou desenvolver uma segunda automação para isso.

E você, o que sugere? 

  - Faça um Fork para eu ver sua sugestão na prática


# Conclusões finais >>> 😎
---------------------------------------------------------------------------
Como dev júnior em fase de obtenção de conhecimento e amadurecimento, me sinto feliz com a minha determinação e vontade de aprender sempre mais.
Sei que haverão dias em que minha motivação será colocada à prova; E espero que nesse dia, eu me recorde do porquê inicie nessa profissão maravilhosa!


--------------------------------------------------
# CONTATOS 🗒️
----------------------------------------------------
- telefone: (14) 9 9626-2918

- email: enriquedesuu@gmail.com

- linkedin: https://www.linkedin.com/in/henrique-de-souza-bezerra-82b3b7269/
    

