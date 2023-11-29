# Apresentação

print('\n\n\t\t-- Tabela De Produtos --')
print('-'*45)

# Entrada c/ Processamento

produto = {
    'Nome':'',
    'Preço':0.0,
    'Quantidade':'',
    'Disponivel':False}

produto['nome'] = str(input('Informe o Produto:'))
produto['Preço'] = float(input('Informe o Preço do Produto:R$'))
produto['Quantidade'] = int(input('Informe a Quantidade do Produto:'))
produto['Disponivel'] = input('O produtos esta disponivel (s/n)?')
print('-'*50)
preçototal =(f'{produto["Preço"] * produto['Quantidade']}')

# saida
print('\n\t\t --Tabela do Produto--')

print(f'Nome do Produto:{produto["nome"]}')
print(f'Preço da UND do Produto:R${produto["Preço"]}')
print(f'Quantidade do Produto:{produto["Quantidade"]} Unidade')
print(f'Preço total:R${preçototal}')

if produto['Disponivel'].lower() == 's':
    print('Produto disponivel!')
else:
    print('Produto indisponivel!')
