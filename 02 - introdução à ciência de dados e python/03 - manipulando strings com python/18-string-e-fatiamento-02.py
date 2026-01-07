nome = "giovanna"
idade = 26
profissao = "programadora"
linguagem = "python"
saldo = 45.435

dados = {"nome": "giovanna", "idade": 26}

print("nome: %s idade: %d" % (nome, idade))

print("nome: {} idade: {}".format(nome, idade))

print("nome: {1} idade: {0}".format(idade, nome))
print("nome: {1} idade: {0} Nome: {1} {1}".format(idade, nome))

print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("nome: {name} idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("nome: {nome} idade: {idade}".format(**dados))

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:.2f}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.1f}")