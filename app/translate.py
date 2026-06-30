from deep_translator import GoogleTranslator
import time

def traduzir_para_frances(texto: str) -> str:
    """
    Traduz texto para francês com retry e fallback.
    """
    texto = (texto or "").strip()
    if not texto:
        return ""

    # Tentativas automáticas
    for tentativa in range(3):
        try:
            return GoogleTranslator(source="auto", target="fr").translate(texto)
        except Exception as e:
            print(f"Tentativa {tentativa+1} falhou: {e}")
            time.sleep(1.5)  # espera antes de tentar de novo

    # Fallback: dividir texto em partes menores
    partes = texto.split(".")
    traduzido_partes = []

    for parte in partes:
        parte = parte.strip()
        if not parte:
            continue
        try:
            traduzido_partes.append(
                GoogleTranslator(source="auto", target="fr").translate(parte)
            )
        except Exception:
            traduzido_partes.append(parte)  # fallback local

    return ". ".join(traduzido_partes)
