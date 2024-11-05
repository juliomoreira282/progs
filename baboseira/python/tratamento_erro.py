meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
try:
    numero = int(input("Digite um número de 1 a 12: \n"))
    if numero < 1 or numero > 12:
        raise IndexError("O número está fora do intervalo.")
    print("O mês correspondente é: "+str(meses[numero - 1]))
except ValueError:
    print("Erro. Use apenas números inteiros. \n")
except IndexError as ie:
    print(f"Erro: {ie}")