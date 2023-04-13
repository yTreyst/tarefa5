numeros = []  # lista para guardar os números da galera

# lendo os números
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro aí, meu consagrado: "))
    numeros.append(numero)

soma = 0  # aqui vamos armazenar a soma total, que é muito louca!

# somando os valores da lista
for numero in numeros:
    soma += numero  # vamos juntar tudo e fazer uma festa de soma!

# exibindo o resultado
print("A soma dos números que você digitou foi:", soma)