# Crie um dicionário estoque com:
# "maçã": 10
# "banana": 5
# "laranja": 8
# Faça o seguinte:
# Adicione "pera" com quantidade 12
# Remova "banana"
# Imprima apenas os nomes dos itens (chaves)

estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}

estoque["pera"] = 12
del estoque["banana"]

print(estoque.keys())