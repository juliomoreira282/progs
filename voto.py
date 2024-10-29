idade = int(input("Digite a idade do usuário: "))
if idade >= 16 and idade < 18:
    print("O voto é facultativo.")

elif idade >= 18:
    print("O voto é obrigatório.")

else:
    print("Não pode votar.")