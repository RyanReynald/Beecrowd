codigo1, num1, valoruni1 = map(float, input().split())

codigo2, num2, valoruni2 = map(float, input().split())

total = (num1 * valoruni1) + (num2 * valoruni2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))