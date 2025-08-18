def encontrar_letra_do_meio(palavra):
  """
  Encontra a letra do meio de uma palavra com um número ímpar de letras.
  """
  # Obtém o comprimento da palavra
  comprimento = len(palavra)
  # Calcula o índice da letra do meio. Como os índices começam em 0,
  # a fórmula é (comprimento - 1) / 2
  indice_meio = (comprimento - 1) // 2
  # Retorna a letra no índice calculado
  return palavra[indice_meio]

# Sequência do enigma
sequencia_enigma = ["LOSANGO", "ICEBERG", "BRUCUTU", "DOIDICE"]

# Obtém as letras do meio de cada palavra na sequência
letras_do_meio = [encontrar_letra_do_meio(palavra) for palavra in sequencia_enigma]
print(f"Letras do meio da sequência: {letras_do_meio}")

# Converte as letras para seus códigos ASCII para verificar a progressão
codigos_ascii = [ord(letra) for letra in letras_do_meio]
print(f"Códigos ASCII das letras: {codigos_ascii}")

# Verifica se a sequência é uma progressão alfabética
# O próximo código ASCII deve ser o último + 1
proximo_codigo = codigos_ascii[-1] + 1
proxima_letra = chr(proximo_codigo)
print(f"A próxima letra na sequência deve ser: {proxima_letra}")

# Opções de resposta
opcoes = {
    "a": "LEGISTA",
    "b": "PROFANO",
    "c": "SUPIMPA",
    "d": "MARASMO",
    "e": "NOVENTA"
}

# Testando cada opção
print("\n--- Verificando as opções ---")
for chave, palavra in opcoes.items():
  letra_meio_opcao = encontrar_letra_do_meio(palavra)
  if letra_meio_opcao == proxima_letra:
    print(f"A opção correta é '{chave}': '{palavra}'")
    print(f"Letra do meio da opção: '{letra_meio_opcao}'")