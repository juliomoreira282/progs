import random

acoes = {
    "Rota1": {"Tempo": 10, "Segurança": 5},
    "Rota2": {"Tempo": 12, "Segurança": 8}
}

def calcular_utilidade(acao):
    return acao["Segurança"] - 0.5 * acao["Tempo"]

def agente_utilidade():
    melhores_acoes = max(acoes.values(), key=calcular_utilidade)
    return melhores_acoes

print(agente_utilidade())