from app.translate import traduzir_para_frances

exemplos =[
    "Este é um texto em português para testar a tradução.",
    "This is an English sentence to test translation.",
    "Bonjour, je suis déjà en français"
]

for texto in exemplos:
    traduzido = traduzir_para_frances(texto)
    print(f'Original: {texto}')
    print(f'(traduzido: {traduzido})')
    print('-'*40)