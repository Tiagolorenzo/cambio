# Importa biblioteca de converção de moeda.
from forex_python.converter import CurrencyRates

# Recebe valor da moeda a ser convertida
valor = str(input('Informe o valor a ser convertido: '))
valor = float(valor.replace(',', '.'))
moeda_origem = input('Informe a moeda origem: ')
moeda_destino = input('Informe a moeda destino: ')

# Faz converção de acordo com a taxa de câmbio
resultado = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

# Exibe o resultado
print(f'$ {valor:,.2f} {moeda_origem} = $ {resultado:,.2f} {moeda_destino}.')
