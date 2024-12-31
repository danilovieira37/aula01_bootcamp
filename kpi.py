CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input('Por favor digite seu nome: ')

# 2) Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input('Por favor digite seu salário: '))

# 3) Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
porcentagem_bonus = float(input('Por favor digite o Porcentual do bônus: '))

# 4) O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
bonus = float(CONSTANTE_BONUS + salario * porcentagem_bonus)

#5) Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f'Olá {nome_usuario}, o seu bônus foi de R$ {bonus}.')