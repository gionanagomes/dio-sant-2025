conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com uso do cheque especial!")
    else:
        print("não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("saque realizado com sucesso!")
    else:
        print("saldo insuficiente!")

elif conta_especial:
    print("conta especial selecionada!")

else:
    print("sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")