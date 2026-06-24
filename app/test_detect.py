from app.detect_lang import detectar_idioma

exemplos = {
    "pt":"Este é um texto em português para testar a detecção de idioma.",
    "en":"This is an English sentence to test language detection",
    "fr":"Ceci est une phrase en français pour tester la détection de la langue.",
    "short" :"Bonjour"
}

for chave , texto in exemplos.items():
    codigo = detectar_idioma(texto)
    print(f'{chave}: {codigo} -> {texto[:60]}')


'''
DetectorFactory.seed = 0 — fixa a semente para que a função detect produza resultados consistentes entre execuções (útil para testes).

texto = (texto or "").strip() — garante que não vamos passar None e remove espaços extras.

if len(texto) < 20: return "und" — regra prática: textos muito curtos (menos de 20 caracteres) tendem a confundir o detector; marcamos como indeterminado para tratarmos depois.

try/except — captura qualquer erro da biblioteca e devolve "und" em vez de quebrar o programa.
'''


#python -m app.test_detect p/ rodar o codigo