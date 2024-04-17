# saldo = 1000
# saque = 200
# limite = 100

# x = saldo >= saque and saque <= limite
# print(x)
# x = saldo >= saque or saque <= limite
# print(x)

# contatos_emergencia = []
# x = not 1000 > 1500
# print(x)

# x = not contatos_emergencia
# print(x)

saldo = 1000
saque = 200
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saldo)
print((saldo >= saque and saque <= limite) and (conta_especial and saldo <= saque))