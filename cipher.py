def cifra_cofre_dinamico(texto: str, termo_inicial: int, razao: int, modo: str = 'criptografar') -> str:
    """Implementação da Cifra do Segredo de Cofre."""
    texto_resultado = []
    x_atual = termo_inicial
    contador_letras = 0

    for caractere in texto:
        if caractere.isalpha():
            base = 65 if caractere.isupper() else 97
            x_atual = (x_atual + razao) % 12 + 1
            sinal_giro = 1 if contador_letras % 2 == 0 else -1
            deslocamento = x_atual * sinal_giro
            
            if modo == 'descriptografar':
                deslocamento = -deslocamento
            
            novo_caractere = chr((ord(caractere) - base + deslocamento) % 26 + base)
            texto_resultado.append(novo_caractere)
            contador_letras += 1
        else:
            texto_resultado.append(caractere)
            
    return "".join(texto_resultado)
