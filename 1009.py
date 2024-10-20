nome = input()
salario = float(input())
totalvendas = float(input())

comisao = totalvendas * 0.15
salariototal = salario + comisao

print(f"TOTAL = R$ {salariototal:.2f}")