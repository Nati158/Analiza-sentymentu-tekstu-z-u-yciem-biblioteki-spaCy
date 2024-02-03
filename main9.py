import spacy

def analiza_sentymentu(tekst):
    nlp = spacy.load("en_core_web_sm")
    dokument = nlp(tekst)
    
    sentyment = sum([token.sentiment for token in dokument]) / len(dokument)

    if sentyment > 0:
        return "Pozytywny"
    elif sentyment < 0:
        return "Negatywny"
    else:
        return "Neutralny"

if __name__ == "__main__":
    tekst_do_analizy = input("Wprowadź tekst do analizy sentymentu: ")
    wynik = analiza_sentymentu(tekst_do_analizy)
    print(f"Sentyment tekstu: {wynik}")
