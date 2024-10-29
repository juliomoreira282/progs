import requests

def obter_taxas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

def converterMoedas(valor, moedaOrigem, moedaDestino, taxas):
    if moedaOrigem in taxas and moedaDestino in taxas:
        taxaOrigem = taxas[moedaOrigem]
        taxaDestino = taxas[moedaDestino]
        valorEmUSD = valor / taxaOrigem
        valorConvertido = valorEmUSD / taxaDestino
        return valorConvertido
    else:
        return None

taxaDeCambio = obter_taxas()

valor = float(input("Qual o valor a ser convertido? "))
moedaOrigem = input("Qual é a moeda de origem? ").upper()
moedaDestino = input("Qual a moeda de destino? ").upper()

valorConvertido = converterMoedas(valor, moedaOrigem, moedaDestino, taxaDeCambio)

if valorConvertido is not None:
    print(f"{valor:.2f} {moedaOrigem} equivale a {valorConvertido:.2f} {moedaDestino}. \n")

else:
    print("Moeda não encontrada ou inválida. \n")