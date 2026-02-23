historico = []

# O usuário visita três sites (PUSH)

historico.append("google.com")
historico.append("youtube.com") 
historico.append("github.com")

print(f"Você está em: {historico[-1]}") # Mostra o topo

# O usuário clica no botão voltar (POP)
print("\n[Clicando no botão Voltar...]")
historico.pop()

print(f"Agora você voltou para: {historico[-1]}")