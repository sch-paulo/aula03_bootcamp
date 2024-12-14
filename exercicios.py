# ### Exercício 1: Verificação de Qualidade de Dados
# # Você está analisando um conjunto de dados de vendas e precisa garantir 
# # que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# # Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# # forem positivos ou "Dados inválidos" caso contrário.
# quantidade = 2
# preco = -20
# if (quantidade >= 0) and (preco >= 0):
#     print('Dados válidos')
# else:
#     print('Dados inválidos')
# print()

# ### Exercício 2: Classificação de Dados de Sensor
# # Imagine que você está trabalhando com dados de sensores IoT. 
# # Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# # como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# # Temperatura < 18°C é 'Baixa'
# # Temperatura >= 18°C e <= 26°C é 'Normal'
# # Temperatura > 26°C é 'Alta'
# temperaturas = [10, 20, 30, 40, 50, 25, 28, 23]
# for temp in temperaturas:
#     if temp < 18:
#         print(f'{temp}°C: baixa')
#     elif temp >= 18 and temp <= 26:
#         print(f'{temp}°C: normal')
#     else:
#         print(f'{temp}°C: alta')
# print()

# ### Exercício 3: Filtragem de Logs por Severidade
# # Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# # com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# # como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# # escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# if log['level'] == 'ERROR':
#     print(f'Mensagem de erro: {log['message']}')
# print()

# ### Exercício 4: Validação de Dados de Entrada
# # Antes de processar os dados de usuários em um sistema de recomendação, 
# # você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# # fornecido um email válido. Escreva um programa que valide essas condições 
# # e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# import re
# dados_usuario = {'nome': 'Ronaldo', 'idade': 18, 'e-mail': 'rona$ldo@fenomeno.com'}
# if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", dados_usuario['e-mail']) and \
#     (dados_usuario['idade'] >= 18) and (dados_usuario['idade'] <= 65):
#     print('Dados de usuário válidos.')
# else:
#     print('Dados de usuário inválidos.')
# print()

# ### Exercício 5: Detecção de Anomalias em Dados de Transações
# # Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# # transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# # a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# # Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = {'valor': 20000, 'hora': 10}
# if (transacao['valor'] > 10000) or (transacao['hora'] > 18) or (transacao['hora'] < 9):
#     print('Transação suspeita.')
# else:
#     print('Transação não suspeita.')
# print()

# ### Exercício 6. Contagem de Palavras em Textos
# # Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# texto = 'ronaldo fenomeno é o melhor do do, do do, do do mundo no futebol futebol'
# conjunto_palavras = texto.replace(',', '').replace('.', '').split()
# contagem_palavras = {}
# for palavra in conjunto_palavras:
#     if palavra not in contagem_palavras.keys():
#         contagem_palavras[palavra] = 1
#     else:
#         contagem_palavras[palavra] += 1
# print(contagem_palavras)
# print()

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
lista_num = [2, 3, 2, 2, 2, 4, 5, 6, 7, 50, 25, 12, 100]
lista_normalizados = [(num - min(lista_num)) / (max(lista_num) - min(lista_num)) for num in lista_num]
print(lista_normalizados)
print()

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
lista_usuarios = [
    {'nome': 'Ronaldo', 'idade': 18, 'e-mail': 'rona$ldo@fenomeno.com'},
    {'nome': '', 'idade': 22, 'e-mail': 'rona$ldo@fenomeno.com'},
    {'nome': 'Roberto', 'idade': 26, 'e-mail': ''},
    {'nome': 'Robson', 'idade': 32, 'e-mail': 'rona$ldo@fenomeno.com'},
    {'nome': 'Rodinei', 'idade': 44, 'e-mail': 'rona$ldo@fenomeno.com'}
]
for usuario in lista_usuarios:
    for col in usuario:
        if len(str(usuario[col])) == 0:
            print(usuario)
print()

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
lista_num = [1, 2, 3, 4, 5, 6, 7, 8]
lista_pares = []
for num in lista_num:
    if num % 2 == 0:
        lista_pares.append(num)
print(lista_pares)
print()

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
vendas_agregadas = {}
for registro in vendas:
    if registro['categoria'] not in vendas_agregadas:
        vendas_agregadas[registro['categoria']] = registro['valor']
    else:
        vendas_agregadas[registro['categoria']] += registro['valor']

print(vendas_agregadas)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.