def agente_reativo_simples(percepcao):
    posicao, situacao = percepcao

    if situacao == 'sujeira':
        return "Aspirar"
    elif posicao == 'A':
        return "Direita"
    elif posicao == 'B':
        return "Esquerda"

print(agente_reativo_simples(("A", "Limpo")))
print(agente_reativo_simples(("B", "Sujo")))