from langdetect import detect, DetectorFactory

# Garante que a detecção seja determinística entre execuções
DetectorFactory.seed = 0

def detectar_idioma(texto: str) -> str:
    '''
    Retorna o codigo do idioma detectado (ex: 'en' , 'pt' , 'fr')
    Para textos muito curtos, retorna 'und' (undetermined).
    '''

    texto = (texto or "").strip()
    if len(texto)<20: 
        #textos curtos sao pouco confiaveis para deteccao automatica
        return "und"
    
    try:
        codigo = detect(texto)
    except Exception:
        codigo = "und"
    return codigo
