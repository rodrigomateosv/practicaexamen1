import re

def detect_nessie(text):
    # Una lista de las frases que Nessie podría usar para solicitar dinero
    nessie_phrases = ["tree fiddy", "3.50", "three fifty"]
    
    # Recorrer cada frase en la lista
    for phrase in nessie_phrases:
        # Utilizar el método search de la librería re para buscar la frase en el texto dado
        match = re.search(phrase, text)
        # Si se encuentra una coincidencia
        if match:
            # Retorna verdadero
            return True
    # Si no se encuentra ninguna coincidencia, retorna falso
    return False

# Ejemplo de uso
text = "I heard the musician playing and he asked for tree fiddy as a tip"
print(detect_nessie(text)) # Output: True

text = "I was at the lake and saw a big creature, but it didn't ask for any money"
print(detect_nessie(text)) # Output: False
