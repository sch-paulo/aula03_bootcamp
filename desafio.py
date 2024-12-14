# Desafio - Integre na solução anterior um fluxo de While que repita o fluxo até que
# o usuário insira as informações corretas

nome_bool, salario_bool, bonus_bool = False, False, False

while nome_bool == False:
    nome = input('Qual o seu nome? ').strip().capitalize()
    if len(nome) == 0:
        print('Você não digitou nada')
    elif any(caracter.isdigit() for caracter in nome):
        resposta = input('Você inseriu dígitos no seu nome, tem certeza que está correto? (S/N) ').lower()
        if resposta == 's':
            nome_bool = True
    else:
        nome_bool = True

while salario_bool == False and bonus_bool == False:
    try:
        salario = float(input('Qual o seu salário mensal? '))
        bonus = float(input('E o seu bônus recebido? '))
        if salario <= 0 or bonus <= 0:
            print('O valor do salário e/ou bônus não pode ser zero ou negativo.')
        else:
            salario_bool = True
            bonus_bool = True
    except ValueError:
        print('Insira um valor numérico.')
    except NameError:
        print('Insira um valor.')
    print()
kpi_bonus = 1000 + salario * bonus
kpi_bonus = round(kpi_bonus,2)

print(f'Olá, {nome}! O valor do seu bônus foi de {kpi_bonus} reais!')